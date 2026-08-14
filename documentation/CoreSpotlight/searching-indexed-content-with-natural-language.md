# Searching indexed content with natural language

**Framework**: Core Spotlight

Give a language model access to your app’s Core Spotlight index to enable natural-language queries over searchable content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

This sample demonstrates [`SpotlightSearchTool`](spotlightsearchtool.md), a type that connects a Foundation Models language-model session to your app’s Core Spotlight index. Using `SpotlightSearchTool`, the language model can search, filter, and reason about your indexed content, turning a metadata-based index into a conversational search experience.

![A person asks “What hikes are by the ocean?” in the sample app’s search field. Matching trail cards, including Crystal Cove State Park and Lands End Trail, appear above a streamed summary of nearby coastal hikes.](/images/com.apple.corespotlight/spotlightsearchtool-hero@2x.png)

The app indexes a collection of hiking trail entries as [`CSSearchableItem`](cssearchableitem.md) objects, then lets people ask natural-language questions like “Which trails in California have water features?” The language model uses the tool to query the index and streams a response alongside the matching trail results.

> **Note**: This sample code project is associated with WWDC26 session [`246: LLM search using Core Spotlight`](https://developer.apple.comhttps://developer.apple.com/wwdc26/246/).

#### Configure the Sample Code Project

This sample requires a device that supports Apple Intelligence, running iOS 27 or later.

Before you build and run the sample, turn on Apple Intelligence by opening Settings > Apple Intelligence & Siri.

By default, the sample runs searches on the on-device, so the project builds and runs without additional configuration. For best performance, route searches through Private Cloud Compute (PCC). For additional information, see [`Adopt Private Cloud Compute`](searching-indexed-content-with-natural-language#Adopt-Private-Cloud-Compute.md).

#### Create a Search Tool for the Language Model

The sample creates a [`SpotlightSearchTool`](spotlightsearchtool.md) configured with a Core Spotlight source to let the language model search the indexed content. The `fetchAttributes` parameter specifies which item attributes the tool returns to the model, providing the information it uses to answer questions about trails. The sample includes both built-in attributes and a custom distance attribute that the app indexes for each trail:

```swift
let fetchAttributes: [SearchableItemAttribute] = [
    .title,
    .contentDescription,
    .namedLocation,
    .stateOrProvince,
    .keywords,
    .latitude,
    .longitude,
    .rating,
    .duration,
    .contentCreationDate,
    .completionDate,
    SearchableItemAttribute(rawValue: distanceAttributeKey.keyName)
]

let tool = SpotlightSearchTool(
    configuration: .init(
        sources: [
            .coreSpotlight(
                .init(
                    searchableIndexDelegate: SpotlightIndexer.shared,
                    fetchAttributes: fetchAttributes
                )
            )
        ],
        guide: .focused()
    )
)
```

#### Adopt Private Cloud Compute

By default, the sample runs searches on the on-device [`SystemLanguageModel`](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel), so the project builds and runs without additional configuration. The view model exposes the model it uses as a `serverModel` property:

```swift
let serverModel = SystemLanguageModel()
```

To route searches through Private Cloud Compute (PCC) instead, initialize `serverModel` with [`PrivateCloudComputeLanguageModel`](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel). When `serverModel` is the PCC model, the search tool uses the [`SpotlightSearchTool.GuidanceLevel.complete`](spotlightsearchtool/guidancelevel/complete.md) guide for richer query construction; on device, it uses [`SpotlightSearchTool.GuidanceLevel.focused(_:)`](spotlightsearchtool/guidancelevel/focused(_:).md) and provides more explicit search instructions to suit the smaller model. For eligibility and setup, see [`Adding server-side intelligence with Private Cloud Compute`](https://developer.apple.com/documentation/foundationmodels/adding-server-side-intelligence-with-private-cloud-compute).

#### Stream Responses From the Language Model

The sample passes the search tool to a [`LanguageModelSession`](https://developer.apple.com/documentation/foundationmodels/languagemodelsession) along with system instructions that describe the indexed data. When a person submits a query, the session calls the tool to find matching entries and streams a natural-language response. The sample creates a fresh session and tool for each search so every query starts with fresh context:

```swift
let session = LanguageModelSession(
    model: serverModel,
    tools: [tool],
    instructions: instructions
)

do {
    for try await chunk in session.streamResponse(to: prompt) {
        response = chunk.content
    }
} catch {
    self.error = error.localizedDescription
}
```

#### Display Search Results Alongside the Response

The search tool provides an asynchronous stream of search replies as the model processes the query. Each reply’s `content` is a discriminated union: matches arrive as [`SpotlightSearchTool.SearchReply.Content.items(_:)`](spotlightsearchtool/searchreply/content-swift.enum/items(_:).md), [`SpotlightSearchTool.SearchReply.Content.scoredItems(_:)`](spotlightsearchtool/searchreply/content-swift.enum/scoreditems(_:).md), or [`SpotlightSearchTool.SearchReply.Content.groupedItems(_:)`](spotlightsearchtool/searchreply/content-swift.enum/groupeditems(_:).md) that provide wrapped [`SearchableItem`](searchableitem.md) results. Additionally, the model may also return other [`SpotlightSearchTool.SearchReply.Content`](spotlightsearchtool/searchreply/content-swift.enum.md) enumeration values as replies, depending on the query.

The sample listens for results on this stream and updates the UI as items arrive, so trail cards appear before the model finishes generating its text summary. Because the model can issue multiple queries while refining results, the sample deduplicates by `uniqueIdentifier` to avoid showing the same trail twice. The sample unwraps each `SearchableItem` to the underlying `CSSearchableItem` at this boundary, and the rest of the UI works directly with Core Spotlight’s own item type:

```swift
private func listenForSearchResults(from tool: SpotlightSearchTool) -> Task<Void, Never> {
    Task { @MainActor in
        var seen: Set<String> = []
        for await reply in tool.searchResults {
            let items: [CSSearchableItem]
            switch reply.content {
            case .items(let searchItems):
                items = searchItems.map(\.item)
            case .scoredItems(let scored):
                items = scored.map(\.item.item)
            case .groupedItems(let groups):
                items = groups.values.flatMap { $0 }.map(\.item)
            case .count, .table, .statistic, .text:
                continue
            @unknown default:
                continue
            }
            let newItems = items.filter { seen.insert($0.uniqueIdentifier).inserted }
            self.results.append(contentsOf: newItems)
        }
    }
}
```

#### Index Searchable Items with Core Spotlight

The sample loads trail data from a property list at launch and indexes each entry as a [`CSSearchableItem`](cssearchableitem.md). Each item includes attributes like title, location, keywords, and duration. The indexer uses [`beginBatch()`](cssearchableindex/beginbatch().md) and [`endBatch(withClientState:completionHandler:)`](cssearchableindex/endbatch(withclientstate:completionhandler:).md) to group the work into a single transaction, and records client state so it can skip reindexing on subsequent launches:

```swift
func indexAllItems() async {
    let items = createSearchableItems()
    guard !items.isEmpty else { return }

    var isIndexed = true
    let newState = Data(bytes: &isIndexed, count: MemoryLayout.size(ofValue: isIndexed))

    do {
        index.beginBatch()
        try await index.indexSearchableItems(items)
        try await index.endBatch(withClientState: newState)
    } catch {
        print("Batch index failed: \(error.localizedDescription)")
    }
}
```

The indexer conforms to [`CSSearchableIndexDelegate`](cssearchableindexdelegate.md) so the system can request full searchable items when needed during hydration, which enriches the generated response.

## See Also

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)
  Make the content you index for Spotlight available to Foundation models to help generate responses to prompts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searching-indexed-content-with-natural-language)*