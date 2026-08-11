# SearchPipelineDataType

**Framework**: Core Spotlight  
**Kind**: enum

Data types that a pipeline stage accepts or produces.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum SearchPipelineDataType
```

#### Overview

Use this type to specify the input and output values your [`CustomStage`](customstage.md) supports. Foundation models use this information to validate that data can pass from one stage to the next.

## Topics

### Getting the pipeline data type
- [SearchPipelineDataType.items](searchpipelinedatatype/items.md)
  Searchable items from the app’s index.
- [SearchPipelineDataType.scoredItems](searchpipelinedatatype/scoreditems.md)
  Searchable items with an assigned score.
- [SearchPipelineDataType.groupedItems](searchpipelinedatatype/groupeditems.md)
  A dictionary that maps searchable items to the attributes they contain.
- [SearchPipelineDataType.text](searchpipelinedatatype/text.md)
  An LLM-generated text summary or analysis.
- [SearchPipelineDataType.count](searchpipelinedatatype/count.md)
  A scalar count of the number of items.
- [SearchPipelineDataType.statistic](searchpipelinedatatype/statistic.md)
  A scalar value that reflects a stastical calculation such as an average, minimum, or maximum.
- [SearchPipelineDataType.table](searchpipelinedatatype/table.md)
  Data suitable for a table or chart.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol CustomStage](customstage.md)
  A custom processing stage the Spotlight search tool uses to identify search results.
- [struct SearchPipelineData](searchpipelinedata.md)
  The type you use to store the output from a custom stage.
- [struct ScoredSearchableItem](scoredsearchableitem.md)
  A searchable item paired with a caller-assigned relevance score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedatatype)*