# CustomStage

**Framework**: Core Spotlight  
**Kind**: protocol

A custom processing stage in a Spotlight search pipeline.

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

Conform your struct to this protocol to add a processing stage that the pipeline can select and execute.

Declare the payload types your stage handles via [`inputTypes`](customstage/inputtypes.md), then implement only the typed `execute` overload(s) that match. The framework routes each incoming payload to the correct overload; unimplemented overloads throw `fatalError` by default. Stages may run in parallel — do not depend on execution order.

Use the static member lookup pattern so stages can be configured with leading dot syntax:

```swift
struct SentimentStage: CustomStage {
    static var name: String { "sentiment" }
    static var description: String { "Scores search results by sentiment" }
    static var inputTypes: [SearchPipelineDataType] { [.items] }
    static var outputTypes: [SearchPipelineDataType] { [.scoredItems] }

    var mode: String

    func execute(items: [CSSearchableItem]) async throws -> SearchPipelineData {
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

// Usage:
let tool = SpotlightSearchTool(configuration: .init(
    customStages: [.sentiment(), .sentiment(mode: "positive")]
))
```

## Topics

### Getting the stage metadata
- [static var name: String](customstage/name.md)
  The stage type name as it appears in the pipeline (e.g., “sentiment”).
- [static var description: String](customstage/description.md)
  A human-readable description of what this stage does.
- [static var inputTypes: [SearchPipelineDataType]](customstage/inputtypes.md)
  The data types this stage accepts as input.
- [static var outputTypes: [SearchPipelineDataType]](customstage/outputtypes.md)
  The data types this stage produces as output.
### Performing the stage behavior
- [func execute(items: [CSSearchableItem]) async throws -> SearchPipelineData](customstage/execute(items:).md)
- [func execute(scoredItems: [ScoredSearchableItem]) async throws -> SearchPipelineData](customstage/execute(scoreditems:).md)
- [func execute(text: String) async throws -> SearchPipelineData](customstage/execute(text:).md)
- [func execute(count: Int) async throws -> SearchPipelineData](customstage/execute(count:).md)
- [func execute(groupedItems: [SearchableItemAttribute : [CSSearchableItem]]) async throws -> SearchPipelineData](customstage/execute(groupeditems:).md)
- [func execute(statisticName: String, value: Double) async throws -> SearchPipelineData](customstage/execute(statisticname:value:).md)
- [func execute(table: SearchResultsTable) async throws -> SearchPipelineData](customstage/execute(table:).md)

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
  The value that flows between pipeline stages, carrying a typed payload.
- [enum SearchPipelineDataType](searchpipelinedatatype.md)
  Declares the kind of data a pipeline stage accepts or produces.
- [struct ScoredSearchableItem](scoredsearchableitem.md)
  A searchable item paired with a caller-assigned relevance score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/customstage)*