# SearchPipelineData.Payload.text(_:)

**Framework**: Core Spotlight  
**Kind**: case

An text summary or analysis your stage produced.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case text(String)
```

## See Also

- [SearchPipelineData.Payload.items(_:)](searchpipelinedata/payload-swift.enum/items(_:).md)
  The array of searchable items your stage produced.
- [SearchPipelineData.Payload.scoredItems(_:)](searchpipelinedata/payload-swift.enum/scoreditems(_:).md)
  The scored searchable items your stage produced.
- [case groupedItems([SearchableItemAttribute : [SearchableItem]])](searchpipelinedata/payload-swift.enum/groupeditems(_:).md)
  A dictionary that maps searchable attributes to the items that contain them.
- [SearchPipelineData.Payload.count(_:)](searchpipelinedata/payload-swift.enum/count(_:).md)
  A scalar count of items your stage produced.
- [SearchPipelineData.Payload.statistic(name:value:)](searchpipelinedata/payload-swift.enum/statistic(name:value:).md)
  A scalar value with a stastical calculation your stage produced.
- [SearchPipelineData.Payload.table(_:)](searchpipelinedata/payload-swift.enum/table(_:).md)
  Tabulated data your stage produced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedata/payload-swift.enum/text(_:))*