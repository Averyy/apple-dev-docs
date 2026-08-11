# CustomStage

**Framework**: Core Spotlight  
**Kind**: protocol

A custom processing stage the Spotlight search tool uses to identify search results.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol CustomStage : Generable, Decodable, Encodable, Sendable
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Overview

A custom stage is a generable type that implements app-specific data transformations for queries. When using Foundation Models, you can use the Spotlight search tool to find app-specific content related to a prompt. The model uses the Spotlight search tool to create queries, each of which might involve require several steps to deliver the final results. For example, a query might fetch items from your app’s Spotlight index, count the number of items it fetched, and assign relevance scores to each item. Each of these steps is a *stage* in the query pipeline, and a custom stage lets you integrate your app’s custom transformations.

Define custom stages as a generable type, and implement your stage’s behavior using the properties and methods of this protocol. A custom stage includes static properties that the model uses to assess how to apply the stage to queries. It also includes `execute` methods to perform the actual data transformations. Each execute method takes one of the input types your stage supports and delivers the specified output type.

The following example shows an implementation of this type that accepts Spotlight searchable items as input and produces scored items as output. The `execute` method in the implementation uses a custom `SentimentAnalyzer` type to calculate the score for each item, based on whether its content conveys a positive, negative, or neutral tone. The example also includes an extension with a static `sentiment` function, which simplifies the creation of the custom stage later.

```swift
@Generable
struct SentimentStage: CustomStage {
    static var name: String { "sentiment" }
    static var description: String { "Scores search results by sentiment.” }
    static var inputTypes: [SearchPipelineDataType] { [.items] }
    static var outputType: SearchPipelineDataType { .scoredItems }

    @Guide(description: “The sentiment to consider when scoring the text of a search result.”)
    var mode: String

    func execute(items: [SearchableItem]) async throws -> SearchPipelineData {
        let scored = items.map { item in
            ScoredSearchableItem(item: item,
                                   score: SentimentAnalyzer.score(item, mode: mode))
        }
        return .scoredItems(scored)
    }
}

extension CustomStage where Self == SentimentStage {
     static func sentiment(mode: String = "all") -> Self {
         SentimentStage(mode: mode)
     }
}
```

To make your custom stage available to a model, include it in the configuration of the Spotlight search tool you associate with your Foundation model’s session. The following example configures the Spotlight search tool with two separate instances of the sentiment stage from the previous example. The first instance scores items across all sentiments while the second instance scores items only on the positivity scale.

```None
let tool = SpotlightSearchTool(configuration: .init(
      customStages: [.sentiment(), .sentiment(mode: "positive")]
))
```

The model builds tool pipelines dynamically, and can run multiple stages in parallel, so implement custom stage types to run independently. Treat the input data your stage receives as immutable, and don’t consider the state or contents of other stages when making decisions. If you do require additional data to generate results, make sure you access the data in a deterministic way.

## Topics

### Getting the stage metadata
- [static var name: String](customstage/name.md)
  The name of the stage as you want it to appear in the pipeline.
- [static var description: String](customstage/description.md)
  A human-readable description of what this stage does.
- [static var inputTypes: [SearchPipelineDataType]](customstage/inputtypes.md)
  The data types this stage accepts as input.
- [static var outputType: SearchPipelineDataType](customstage/outputtype.md)
  The data type this stage produces as output.
### Performing the stage behavior
- [func execute(items: [SearchableItem]) async throws -> SearchPipelineData](customstage/execute(items:).md)
  Generates output data from an array of searchable items from the app’s Spotlight index.
- [func execute(scoredItems: [ScoredSearchableItem]) async throws -> SearchPipelineData](customstage/execute(scoreditems:).md)
  Generates output data from an array of scored searchable items.
- [func execute(text: String) async throws -> SearchPipelineData](customstage/execute(text:).md)
  Generates output data from the specified input string.
- [func execute(count: Int) async throws -> SearchPipelineData](customstage/execute(count:).md)
  Generates output data from the specified count value.
- [func execute(groupedItems: [SearchableItemAttribute : [SearchableItem]]) async throws -> SearchPipelineData](customstage/execute(groupeditems:).md)
  Generates output data from the specified dictionary of attributes and searchable items.
- [func execute(table: SearchResultsTable) async throws -> SearchPipelineData](customstage/execute(table:).md)
  Generates output data from the specified tabular data.
### Instance Methods
- [func execute(statistic: String, value: Double) async throws -> SearchPipelineData](customstage/execute(statistic:value:).md)
  Generates output data from the specified statistical value.

## Relationships

### Inherits From
- [ConvertibleFromGeneratedContent](../FoundationModels/ConvertibleFromGeneratedContent.md)
- [ConvertibleToGeneratedContent](../FoundationModels/ConvertibleToGeneratedContent.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Generable](../FoundationModels/Generable.md)
- [InstructionsRepresentable](../FoundationModels/InstructionsRepresentable.md)
- [PromptRepresentable](../FoundationModels/PromptRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct SearchPipelineData](searchpipelinedata.md)
  The type you use to store the output from a custom stage.
- [enum SearchPipelineDataType](searchpipelinedatatype.md)
  Data types that a pipeline stage accepts or produces.
- [struct ScoredSearchableItem](scoredsearchableitem.md)
  A searchable item paired with a caller-assigned relevance score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/customstage)*