# Making your indexed content available to Foundation Models

**Framework**: Core Spotlight

Make the content you index for Spotlight available to Foundation models to help generate responses to prompts.

#### Overview

The Foundation Models framework provides access to language models that you can use to implement intelligent features in your apps. Language models answer questions on a wide variety of subjects, but they can’t automatically answer questions related to your app’s content. However, you can give those models the ability to answer questions about your content using the Spotlight search tool.

The Spotlight search tool gives models a way to search your app’s content and use the results to answer prompts. When a model requires your app’s data, it uses the search tool to run queries against your app’s Spotlight index or indexed files. The model uses the results as additional context to answer prompts that involve your content.

> **Note**: To use the Spotlight search tool, you first need to index your app’s content. For information about the indexing process and how to perform it on your app’s content, see [`Adding your app’s content to Spotlight indexes`](adding-your-app-s-content-to-spotlight-indexes.md).

##### Configure a Model to Use the Spotlight Search Tool

When configuring a Foundation Models session, you can specify additional tools to handle specific tasks. The [`SpotlightSearchTool`](spotlightsearchtool.md) type implements the framework’s protocols for tools and gives models the ability to query your app’s content. The following example creates a default instance of the tool, uses it to initialize a session, and generates a response to a prompt:

```swift
import CoreSpotlight
import FoundationModels

let tool = SpotlightSearchTool()

let session = LanguageModelSession(tools: [tool])
let response = try await session.respond(to: "Find my notes about the project deadline.")
```

The default configuration of [`SpotlightSearchTool`](spotlightsearchtool.md) performs queries against your app’s Spotlight index using all available search techniques. The tool supports a variety of techniques, some of which might not be relevant to your content. When configuring the tool, provide guidance on which search techniques to use along with other configuration details:

- **Specify where to find your app’s content.** You can tell the tool to search your app’s Spotlight index or search directories containing your app’s files. You can also search multiple sources and combine the results.
- **Tell the tool to fetch specific attributes for each item.** The default tool configuration returns minimal information for each item. Include a list of attributes your items support to make the associated data available to the model.
- **Optimize data retrieval operations.** Focus data retrieval on specific types of content, such as someone’s messages and communications, documents, media, or other data. The tool packages this information in a more compact format suitable for on-device models or models with smaller context windows.
- **Offer guidance on how to search your content.** The Spotlight search tool has many ways to perform searches, but some techniques might not apply to your content. For example, if you only search for textual items, you don’t need to consider searches involving dates or numerical values. Eliminate search options you don’t need to reduce the amount of content the tool sends to the model.

##### Specify Where to Find Your Apps Content

At configuration time, you need to tell the Spotlight search tool where to look for your app’s content. You provide that information using a search source, which is one of the following types:

- The [`CoreSpotlightSource`](corespotlightsource.md) type searches your app’s Spotlight index.
- The [`FileSource`](filesource.md) type searches a set of directories for indexed files.

In addition to telling your app where to search, a search source provides details about how to perform searches of that source. You can specify options such as the maximum number of results to return during a query or which attributes you want to retrieve for each result. For the [`CoreSpotlightSource`](corespotlightsource.md) type, you can also specify a delegate object to generate data for attributes that aren’t in the index. For example, you might use the delegate to supply text content that the indexer transmuted during the indexing process. Configuring these values helps the tool deliver better information for each query.

You can configure the Spotlight search tool with multiple sources, and search your app’s Spotlight index, multiple directories, or both. During a query, the tool searches each source separately and then combines the results before delivering them to the model.

##### Make Searches More Efficient By Optimizing Data Retrieval

At configuration time, provide guidance to help the model optimize the queries it performs using the Spotlight search tool. The search tool supports a variety of search techniques and content types, and your guidance specifies which options you support. Eliminating options that aren’t relevant for your content reduces the amount of information the search tool sends back to the model, freeing up context space for other content.

To specify your guidance options, create the [`SpotlightSearchTool.Configuration`](spotlightsearchtool/configuration-swift.struct.md) structure and add your guidance to the [`guide`](spotlightsearchtool/configuration-swift.struct/guide.md) property. When configuring guidance, you can choose from the following options:

- The [`SpotlightSearchTool.GuidanceLevel.complete`](spotlightsearchtool/guidancelevel/complete.md) option employs all search options to find your content.
- The [`SpotlightSearchTool.GuidanceLevel.focused(_:)`](spotlightsearchtool/guidancelevel/focused(_:).md) option focuses the model on specific types of content.
- The [`SpotlightSearchTool.GuidanceLevel.dynamic(_:)`](spotlightsearchtool/guidancelevel/dynamic(_:).md) option specifies which search techniques make sense for your content.

If you’re using a model with severe token constraints, another way to improve efficiency is to apply the [`SpotlightSearchTool.FormatLevel.compact`](spotlightsearchtool/formatlevel/compact.md) configuration option. When you apply this option to the [`format`](spotlightsearchtool/guide/format.md) property of your guide configuration, the tool outputs results in a compact format. You might choose this option if you’re using a model with a small context window that can’t handle conversations with large amounts of data. You might also use this approach if you anticipate a long conversation and need to save room for additional contextual data later.

##### Help the Model Resolve References to People

People inherently understand the personal pronouns other people use during conversations, but those same pronouns present difficulties for tools and code. If your searchable items contain metadata relating to people, such as author or recipient data, provide a contact resolver to help the model resolve first-person pronouns like “I” and “me”. A contact resolver provides information about the person using your app such as the person’s name, email, or phone details. The model can match this information against the data it encounters in item metadata to resolve first-person references. The following example shows how to add a custom contact resolver to the Spotlight search tool:

```swift
let tool = SpotlightSearchTool(configuration: .init(
    contactResolver: MyContactResolver()
))
let session = LanguageModelSession(tools: [tool])

// "I" is resolved to the user's identity for matching against item authors/senders.
let response = try await session.respond(to: "Show me the documents I shared last week.")
```

To implement a contact resolver, create a type that adopts the [`ContactResolver`](contactresolver.md) protocol.
Your custom type returns a [`ResolvedContact`](resolvedcontact.md) structure with information about the person who owns your app’s data. Fill in the properties of the structure with relevant information about the person who uses your app. For example, a communications app might include the person’s name and the phone number or email associated with their account. The search tool passes this information along to the model to help it reason about references to the person.

##### Customize How the Tool Determines Search Results

When processing complex prompts, a model might run multiple queries to get the results it needs. For each query, the model builds a pipeline of work, where each *stage* of the pipeline is a specific task to run on the data. For example, one stage might retrieve items, another one might count the items, and a third one might assign relevance scores to each item. The Spotlight search tool defines pipeline stages for many common tasks, but you can add custom stages to apply app-specific transformations to the data in the pipeline.

The model builds tool pipelines dynamically and can run stages in parallel, so design your custom stages to run independently with little or no extra data. When you define a custom stage, specify the type of input data you want to receive and the type of output data your stage generates. For example, a stage that creates relevance scores for items might take [`CSSearchableItem`](cssearchableitem.md) objects as input and generate [`ScoredSearchableItem`](scoredsearchableitem.md) objects as outputs. The input and output types, plus other information in your custom stage, help the model determine when to add that stage to a pipeline.

> **Note**: Try to transform input data without any additional data from your app, because custom stages can run on multiple threads simultaneously. If you need additional information, access it in a safe manner using immutable objects, Swift actors, or other deterministic approaches.

To define a custom stage, create a structure that conforms to the [`CustomStage`](customstage.md) protocol. Use the protocol’s API to specify the inputs and output of your stage, and use the [`description`](customstage/description.md) property to provide the model with instructions on how to use your stage. Implement the `execute` method for each type of input you support, and transform the data you receive to the expected output data. The following example shows an implementation of this protocol that ranks each searchable item based on how recently the person viewed it.

```swift
struct RecencyBoostStage: CustomStage {
    static var name: String { "recency_boost" }
    static var description: String { "Boosts recently modified items in the ranking." }
    static var inputTypes: [SearchPipelineDataType] { [.items] }
    static var outputType: SearchPipelineDataType { .scoredItems }

    var recencyWeight: Double

    func execute(items: [CSSearchableItem]) async throws -> SearchPipelineData {
        let now = Date()
        let scored = items.map { item -> ScoredSearchableItem in
            let age = now.timeIntervalSince(item.attributeSet.contentModificationDate ?? .distantPast)
            let recencyScore = max(0, 1.0 - (age / (30 * 86400))) // decay over 30 days
            return ScoredSearchableItem(item: item, score: recencyScore * recencyWeight)
        }
        return .scoredItems(scored)
    }
}
```

To simplify the creation of your custom stage, extend the [`CustomStage`](customstage.md) protocol and add a static function to create your custom structure. You can use this function later to create instances of your stage using dot syntax. The following example defines the `recencyBoost` function that configures and returns a new instance of the `RecencyBoostStage` structure.

```swift
extension CustomStage where Self == RecencyBoostStage {
    static func recencyBoost(weight: Double = 0.3) -> Self {
        RecencyBoostStage(recencyWeight: weight)
    }
}
```

To add your custom stage to the Spotlight search tool, specify it at configuration time as shown in the following example. The code uses dot syntax to take advantage of the custom function from the previous code listing.

```swift
let tool = SpotlightSearchTool(configuration: .init(
    sources: [.coreSpotlight],
    customStages: [.recencyBoost(), .recencyBoost(weight: 0.5)]
))
```

##### Examine Results While a Search Runs

While the Spotlight search tool runs, your app can monitor the search results and any search-related information the tool generates. You might do so to debug your code, to display the search results in your app, or to monitor specific metrics during the search process. To receive these results, set up a task to monitor the asynchronous sequence in the [`searchResults`](spotlightsearchtool/searchresults.md) property of [`SpotlightSearchTool`](spotlightsearchtool.md). This property delivers a series of [`SpotlightSearchTool.SearchReply`](spotlightsearchtool/searchreply.md) structures to your app, which you use to retrieve information.

During prompt resolution, the model might run multiple queries, and each query might require multiple stages to generate the needed data. The [`queryToken`](spotlightsearchtool/searchreply/querytoken-swift.property.md) and [`stageToken`](spotlightsearchtool/searchreply/stagetoken-swift.property.md) properties of each [`SpotlightSearchTool.SearchReply`](spotlightsearchtool/searchreply.md) structure help you correlate each instance to a particular query and stage. Use this information to determine how to organize this information in your app. For example, you might group the results from each query or stage, or refresh the list of results each time a new query starts.

When processing results, use the [`content`](spotlightsearchtool/searchreply/content-swift.property.md) property of the [`SpotlightSearchTool.SearchReply`](spotlightsearchtool/searchreply.md) structure to determine what information the type contains. The following example creates a task and uses a `for await` loop to receive the reply structures asynchronously. With each new structure, the code updates different parts of its interface to show the data. The code shows a progress indicator while it waits for more data from the same query.

```swift
let tool = SpotlightSearchTool()
let session = LanguageModelSession(tools: [tool])

// Start consuming results before the model responds.
Task {
    var currentToken: SpotlightSearchTool.SearchReply.QueryToken?
    for await reply in tool.searchResults {
        if reply.queryToken != currentToken {
            // New query — start a new display section.
            currentToken = reply.queryToken
        }

        switch reply.content {
        case .items(let items):
            displayResultsList(label: reply.label, items: items)

        case .count(let n, let header):
            displayCount(n, header: header ?? reply.label)

        case .table(let table):
            displayTable(table)

        case .statistic(let name, let value, let header):
            displayMetric(name: name, value: value, header: header ?? reply.label)

        case .text(let body, let header):
            displayTextBlock(body, header: header ?? reply.label)
        }

        showProgressIndicator(reply.status == .partial)
    }
}

let response = try await session.respond(to: "Show me recent emails from Shelly.")
```

## See Also

- [Searching indexed content with natural language](searching-indexed-content-with-natural-language.md)
  Give a language model access to your app’s Core Spotlight index to enable natural-language queries over searchable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/making-your-indexed-content-available-to-foundation-models)*