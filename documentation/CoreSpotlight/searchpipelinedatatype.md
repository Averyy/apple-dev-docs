# SearchPipelineDataType

**Framework**: Core Spotlight  
**Kind**: enum

Declares the kind of data a pipeline stage accepts or produces.

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

Use these values to describe the expected input and output shapes of a [`CustomStage`](customstage.md). The pipeline runtime uses them to validate wiring between stages.

## Topics

### Getting the pipeline data type
- [SearchPipelineDataType.items](searchpipelinedatatype/items.md)
  [`CSSearchableItem`](cssearchableitem.md) results.
- [SearchPipelineDataType.scoredItems](searchpipelinedatatype/scoreditems.md)
  [`CSSearchableItem`](cssearchableitem.md) results with caller-assigned scores.
- [SearchPipelineDataType.groupedItems](searchpipelinedatatype/groupeditems.md)
  Items partitioned into named groups.
- [SearchPipelineDataType.text](searchpipelinedatatype/text.md)
  LLM-generated text summary or analysis.
- [SearchPipelineDataType.count](searchpipelinedatatype/count.md)
  A scalar count (e.g., “47 emails from John”).
- [SearchPipelineDataType.statistic](searchpipelinedatatype/statistic.md)
  A scalar statistic (sum, average, max, min, median, stddev).
- [SearchPipelineDataType.table](searchpipelinedatatype/table.md)
  Tabulated data suitable for a table or chart.

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
  A custom processing stage in a Spotlight search pipeline.
- [struct SearchPipelineData](searchpipelinedata.md)
  The value that flows between pipeline stages, carrying a typed payload.
- [struct ScoredSearchableItem](scoredsearchableitem.md)
  A searchable item paired with a caller-assigned relevance score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedatatype)*