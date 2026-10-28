# SearchPipelineData.Payload

**Framework**: Core Spotlight  
**Kind**: enum  
**Role**: Enumeration

The typed variants of data a pipeline stage can produce.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum Payload
```

## Overview

The [`SearchPipelineData`](../searchpipelinedata.md) type uses this type to wrap the data you provide and store it for handoff to the next stage. The type is `@unchecked Sendable` because [`CSSearchableItem`](../cssearchableitem.md) does not support the [`Sendable`](../../Swift/sendable.md) protocol. Treat the data you store in this type as immutable.

## Topics

### Getting the payload data
- [SearchPipelineData.Payload.items(_:)](./payload-swift.enum/items%28_%29.md)
  The array of searchable items your stage produced.
- [SearchPipelineData.Payload.scoredItems(_:)](./payload-swift.enum/scoreditems%28_%29.md)
  The scored searchable items your stage produced.
- [case groupedItems([SearchableItemAttribute : [SearchableItem]])](./payload-swift.enum/groupeditems%28_%29.md)
  A dictionary that maps searchable attributes to the items that contain them.
- [SearchPipelineData.Payload.text(_:)](./payload-swift.enum/text%28_%29.md)
  An text summary or analysis your stage produced.
- [SearchPipelineData.Payload.count(_:)](./payload-swift.enum/count%28_%29.md)
  A scalar count of items your stage produced.
- [SearchPipelineData.Payload.statistic(name:value:)](./payload-swift.enum/statistic%28name,value%29.md)
  A scalar value with a stastical calculation your stage produced.
- [SearchPipelineData.Payload.table(_:)](./payload-swift.enum/table%28_%29.md)
  Tabulated data your stage produced.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the pipeline data
- [let payload: SearchPipelineData.Payload](./payload-swift.property.md)
  The output data your custom stage produced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedata/payload-swift.enum)*