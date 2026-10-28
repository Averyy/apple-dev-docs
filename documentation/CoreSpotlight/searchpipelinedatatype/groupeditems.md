# SearchPipelineDataType.groupedItems

**Framework**: Core Spotlight  
**Kind**: case  
**Role**: Case

A dictionary that maps searchable items to the attributes they contain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case groupedItems
```

## Discussion

The keys of the dictionary are `SearchableItemAtttribute` values. The value for each key is an array of [`CSSearchableItem`](../cssearchableitem.md) types that contain a value for the key.

## See Also

### Getting the pipeline data type
- [SearchPipelineDataType.items](./items.md)
  Searchable items from the app’s index.
- [SearchPipelineDataType.scoredItems](./scoreditems.md)
  Searchable items with an assigned score.
- [SearchPipelineDataType.text](./text.md)
  An LLM-generated text summary or analysis.
- [SearchPipelineDataType.count](./count.md)
  A scalar count of the number of items.
- [SearchPipelineDataType.statistic](./statistic.md)
  A scalar value that reflects a stastical calculation such as an average, minimum, or maximum.
- [SearchPipelineDataType.table](./table.md)
  Data suitable for a table or chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedatatype/groupeditems)*