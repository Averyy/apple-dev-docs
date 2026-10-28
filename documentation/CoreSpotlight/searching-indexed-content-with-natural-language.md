# Searching indexed content with natural language

**Framework**: Core Spotlight  
**Role**: Sample Code  
**Download**: [SearchingIndexedContentWithNaturalLanguage.zip](https://docs-assets.developer.apple.com/published/799313884e7c/SearchingIndexedContentWithNaturalLanguage.zip)

Give a language model access to your app’s Core Spotlight index to enable natural-language queries over searchable content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- Xcode 27.0+

## Overview

This sample demonstrates [`SpotlightSearchTool`](./spotlightsearchtool.md), a type that connects a Foundation Models language-model session to your app’s Core Spotlight index. Using `SpotlightSearchTool`, the language model can search, filter, and reason about your indexed content, turning a metadata-based index into a conversational search experience.

![A person asks “What hikes are by the ocean?” in the sample app’s search field. Matching trail cards, including Crystal Cove State Park and Lands End Trail, appear above a streamed summary of nearby coastal hikes.](https://developer.apple.com/tutorials/images/com.apple.corespotlight/spotlightsearchtool-hero@2x.png)

The app indexes a collection of hiking trail entries as [`CSSearchableItem`](./cssearchableitem.md) objects, then lets people ask natural-language questions like “Which trails in California have water features?” The language model uses the tool to query the index and streams a response alongside the matching trail results.

> **Note**: This sample code project is associated with WWDC26 session [246: LLM search using Core Spotlight](https://developer.apple.com/wwdc26/246/).

## Configure the sample code project

This sample requires a device that supports Apple Intelligence, running iOS 27 or later.

Before you build and run the sample, turn on Apple Intelligence by opening Settings > Apple Intelligence & Siri.

By default, the sample runs searches on the on-device system language model, so the project builds and runs without additional configuration. For best search performance, route searches to *Private Cloud Compute* (PCC) models designed for Apple Intelligence. For more information, see [Adopt Private Cloud Compute](./searching-indexed-content-with-natural-language.md#Adopt-Private-Cloud-Compute).

## Provide search attributes to the language model

The sample creates a [`SpotlightSearchTool`](./spotlightsearchtool.md) configured with a Core Spotlight source to let the language model search the indexed content. The `fetchAttributes` parameter specifies which item attributes the tool returns to the model, providing the information it uses to answer questions about trails. The sample includes both built-in attributes and a custom distance attribute that the app indexes for each trail:

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
```

## Adopt Private Cloud Compute

By default, the sample searches your app’s Spotlight index using the on-device [`SystemLanguageModel`](../FoundationModels/systemlanguagemodel.md), so the project builds and runs without additional configuration.

The sample’s view model exposes the language model it uses as a `foundationModel` property:

```swift
// Initialize `foundationModel` with an on-device model so the sample works without additional configuration:
let foundationModel = SystemLanguageModel()
// Alternatively, initialize `foundationModel` with a PCC language model.
// let foundationModel = PrivateCloudComputeLanguageModel()
```

For best search performance that takes advantage of server models, route searches through *Private Cloud Compute* (PCC) instead. For eligibility and setup, see [Adding server-side intelligence with Private Cloud Compute](../FoundationModels/adding-server-side-intelligence-with-private-cloud-compute.md).

To adopt PCC, initialize `foundationModel` with [`PrivateCloudComputeLanguageModel`](../FoundationModels/privatecloudcomputelanguagemodel.md). When `foundationModel` is the PCC model, the sample uses the [`SpotlightSearchTool.GuidanceLevel.complete`](./spotlightsearchtool/guidancelevel/complete.md) guide for richer query construction; on device. When `foundationModel` is the on-device model, the sample uses the [`SpotlightSearchTool.GuidanceLevel.focused(_:)`](./spotlightsearchtool/guidancelevel/focused%28_%29.md) guide and provides more explicit search instructions to suit the smaller model.

```swift
// A Boolean value that indicates whether the search tool uses an on-device or PCC model.
private var isOnDevice: Bool {
    type(of: foundationModel) == SystemLanguageModel.self
}

// Initializes the Spotlight search tool and guides it to
// perform a `.focused()` search when using an on-device model and a
// `.complete` search when using Private Cloud Compute models.
private func makeSpotlightTool() -> SpotlightSearchTool {
    SpotlightSearchTool(
        configuration: .init(
            sources: [
                .coreSpotlight(
                    .init(
                        searchableIndexDelegate: SpotlightIndexer.shared,
                        fetchAttributes: Self.fetchAttributes
                    )
                )
            ],
            guide: isOnDevice ? .focused() : .complete
        )
    )
}
```

## Stream responses from the language model

The sample passes the search tool to a [`LanguageModelSession`](../FoundationModels/languagemodelsession.md) along with system instructions that describe the indexed data. When a person submits a query, the session calls the tool to find matching entries and streams a natural-language response. The sample creates a fresh session and tool for each search so every query starts with fresh context:

```swift
let session = LanguageModelSession(
    model: foundationModel,
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

## Display search results alongside the response

The search tool provides an asynchronous stream of search replies as the model processes the query. Each reply’s `content` is a discriminated union: matches arrive as [`SpotlightSearchTool.SearchReply.Content.items(_:)`](./spotlightsearchtool/searchreply/content-swift.enum/items%28_%29.md), [`SpotlightSearchTool.SearchReply.Content.scoredItems(_:)`](./spotlightsearchtool/searchreply/content-swift.enum/scoreditems%28_%29.md), or [`SpotlightSearchTool.SearchReply.Content.groupedItems(_:)`](./spotlightsearchtool/searchreply/content-swift.enum/groupeditems%28_%29.md) that provide wrapped [`SearchableItem`](./searchableitem.md) results. Additionally, the model may also return other [`SpotlightSearchTool.SearchReply.Content`](./spotlightsearchtool/searchreply/content-swift.enum.md) enumeration values as replies, depending on the query.

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

## Index searchable items with Core Spotlight

The sample loads trail data from a property list at launch and indexes each entry as a [`CSSearchableItem`](./cssearchableitem.md). Each item includes attributes like title, location, keywords, and duration. The indexer uses [`beginBatch()`](./cssearchableindex/beginbatch%28%29.md) and [`endBatch(withClientState:completionHandler:)`](./cssearchableindex/endbatch%28withclientstate,completionhandler%29.md) to group the work into a single transaction, and records client state so it can skip reindexing on subsequent launches:

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

The indexer conforms to [`CSSearchableIndexDelegate`](./cssearchableindexdelegate.md) so the system can request full searchable items when needed during hydration, which enriches the generated response.

## See Also

### Essentials
- [Making your indexed content available to Foundation Models](./making-your-indexed-content-available-to-foundation-models.md)
  Make the content you index for Spotlight available to Foundation models to help generate responses to prompts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searching-indexed-content-with-natural-language)*