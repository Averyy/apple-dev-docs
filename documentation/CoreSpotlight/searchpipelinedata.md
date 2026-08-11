# SearchPipelineData

**Framework**: Core Spotlight  
**Kind**: struct

The type you use to store the output from a custom stage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SearchPipelineData
```

#### Overview

A custom stage receives data as input and generate a `SearchPipelineData` structure as output. When generating output for a stage in your `execute` methods, build the output data and wrap it with this structure before returning it. This type manages the handoff of your output data to the next stage in the pipeline or to the model.

## Topics

### Configuring the pipeline data
- [init(payload: SearchPipelineData.Payload)](searchpipelinedata/init(payload:).md)
  Initializes the pipeline data with the specified payload value.
- [static func items([SearchableItem]) -> SearchPipelineData](searchpipelinedata/items(_:).md)
  Creates a pipeline data structure from the an array of searchable items.
- [static func scoredItems([ScoredSearchableItem]) -> SearchPipelineData](searchpipelinedata/scoreditems(_:).md)
  Creates a pipeline data structure from the an array of scored searchable items.
- [static func groupedItems([SearchableItemAttribute : [SearchableItem]]) -> SearchPipelineData](searchpipelinedata/groupeditems(_:).md)
  Creates a pipeline data structure from a dictionary of attributes and searchable items.
- [static func text(String) -> SearchPipelineData](searchpipelinedata/text(_:).md)
  Creates a pipeline data structure from a text string.
- [static func count(Int) -> SearchPipelineData](searchpipelinedata/count(_:).md)
  Creates a pipeline data structure from an integer value.
- [static func statistic(name: String, value: Double) -> SearchPipelineData](searchpipelinedata/statistic(name:value:).md)
  Creates a pipeline data structure from statistical information.
- [static func table(SearchResultsTable) -> SearchPipelineData](searchpipelinedata/table(_:).md)
  Creates a pipeline data structure from tabular data.
### Getting the pipeline data
- [let payload: SearchPipelineData.Payload](searchpipelinedata/payload-swift.property.md)
  The output data your custom stage produced.
- [SearchPipelineData.Payload](searchpipelinedata/payload-swift.enum.md)
  The typed variants of data a pipeline stage can produce.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol CustomStage](customstage.md)
  A custom processing stage the Spotlight search tool uses to identify search results.
- [enum SearchPipelineDataType](searchpipelinedatatype.md)
  Data types that a pipeline stage accepts or produces.
- [struct ScoredSearchableItem](scoredsearchableitem.md)
  A searchable item paired with a caller-assigned relevance score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedata)*