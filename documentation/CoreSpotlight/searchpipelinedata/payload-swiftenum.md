# SearchPipelineData.Payload

**Framework**: Core Spotlight  
**Kind**: enum

The typed variants of data a pipeline stage can produce or consume.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum Payload
```

#### Overview

`@unchecked Sendable` because `CSSearchableItem` is not `Sendable`. Pipeline stages must not mutate items received from prior stages.

## Topics

### Getting the payload data
- [SearchPipelineData.Payload.items(_:)](searchpipelinedata/payload-swift.enum/items(_:).md)
  Items from a Spotlight query.
- [SearchPipelineData.Payload.scoredItems(_:)](searchpipelinedata/payload-swift.enum/scoreditems(_:).md)
  Items annotated with caller-assigned relevance scores.
- [case groupedItems([SearchableItemAttribute : [CSSearchableItem]])](searchpipelinedata/payload-swift.enum/groupeditems(_:).md)
  Items partitioned by an attribute value (e.g. content type).
- [SearchPipelineData.Payload.text(_:)](searchpipelinedata/payload-swift.enum/text(_:).md)
  LLM-generated text summary or analysis.
- [SearchPipelineData.Payload.count(_:)](searchpipelinedata/payload-swift.enum/count(_:).md)
  A scalar count derived from items (e.g., 47).
- [SearchPipelineData.Payload.statistic(name:value:)](searchpipelinedata/payload-swift.enum/statistic(name:value:).md)
  A scalar statistic (sum, average, max, min, median, stddev).
- [SearchPipelineData.Payload.table(_:)](searchpipelinedata/payload-swift.enum/table(_:).md)
  Tabulated data — rows of labeled values.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let payload: SearchPipelineData.Payload](searchpipelinedata/payload-swift.property.md)
  The result payload produced by a stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedata/payload-swift.enum)*