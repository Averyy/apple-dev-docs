# SearchPipelineData.Payload

**Framework**: Core Spotlight  
**Kind**: enum

The typed variants of data a pipeline stage can produce.

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

The [`SearchPipelineData`](searchpipelinedata.md) type uses this type to wrap the data you provide and store it for handoff to the next stage. The type is `@unchecked Sendable` because [`CSSearchableItem`](cssearchableitem.md) does not support the [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable) protocol. Treat the data you store in this type as immutable.

## Topics

### Getting the payload data
- [SearchPipelineData.Payload.items(_:)](searchpipelinedata/payload-swift.enum/items(_:).md)
  The array of searchable items your stage produced.
- [SearchPipelineData.Payload.scoredItems(_:)](searchpipelinedata/payload-swift.enum/scoreditems(_:).md)
  The scored searchable items your stage produced.
- [case groupedItems([SearchableItemAttribute : [SearchableItem]])](searchpipelinedata/payload-swift.enum/groupeditems(_:).md)
  A dictionary that maps searchable attributes to the items that contain them.
- [SearchPipelineData.Payload.text(_:)](searchpipelinedata/payload-swift.enum/text(_:).md)
  An text summary or analysis your stage produced.
- [SearchPipelineData.Payload.count(_:)](searchpipelinedata/payload-swift.enum/count(_:).md)
  A scalar count of items your stage produced.
- [SearchPipelineData.Payload.statistic(name:value:)](searchpipelinedata/payload-swift.enum/statistic(name:value:).md)
  A scalar value with a stastical calculation your stage produced.
- [SearchPipelineData.Payload.table(_:)](searchpipelinedata/payload-swift.enum/table(_:).md)
  Tabulated data your stage produced.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let payload: SearchPipelineData.Payload](searchpipelinedata/payload-swift.property.md)
  The output data your custom stage produced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedata/payload-swift.enum)*