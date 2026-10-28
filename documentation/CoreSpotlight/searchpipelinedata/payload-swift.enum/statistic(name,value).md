# SearchPipelineData.Payload.statistic(name:value:)

**Framework**: Core Spotlight  
**Kind**: case  
**Role**: Case

A scalar value with a stastical calculation your stage produced.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case statistic(name: String, value: Double)
```

## Discussion

Use this type to specify summation, average, minimum, maximum, median, or standard deviation values. Specify the name of the statistic you generated together with the numerical value.

## See Also

### Getting the payload data
- [SearchPipelineData.Payload.items(_:)](./items%28_%29.md)
  The array of searchable items your stage produced.
- [SearchPipelineData.Payload.scoredItems(_:)](./scoreditems%28_%29.md)
  The scored searchable items your stage produced.
- [case groupedItems([SearchableItemAttribute : [SearchableItem]])](./groupeditems%28_%29.md)
  A dictionary that maps searchable attributes to the items that contain them.
- [SearchPipelineData.Payload.text(_:)](./text%28_%29.md)
  An text summary or analysis your stage produced.
- [SearchPipelineData.Payload.count(_:)](./count%28_%29.md)
  A scalar count of items your stage produced.
- [SearchPipelineData.Payload.table(_:)](./table%28_%29.md)
  Tabulated data your stage produced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedata/payload-swift.enum/statistic(name:value:))*