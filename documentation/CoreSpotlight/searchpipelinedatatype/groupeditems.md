# SearchPipelineDataType.groupedItems

**Framework**: Core Spotlight  
**Kind**: case

A dictionary that maps searchable items to the attributes they contain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case groupedItems
```

#### Discussion

The keys of the dictionary are `SearchableItemAtttribute` values. The value for each key is an array of [`CSSearchableItem`](cssearchableitem.md) types that contain a value for the key.

## See Also

- [SearchPipelineDataType.items](searchpipelinedatatype/items.md)
  Searchable items from the app’s index.
- [SearchPipelineDataType.scoredItems](searchpipelinedatatype/scoreditems.md)
  Searchable items with an assigned score.
- [SearchPipelineDataType.text](searchpipelinedatatype/text.md)
  An LLM-generated text summary or analysis.
- [SearchPipelineDataType.count](searchpipelinedatatype/count.md)
  A scalar count of the number of items.
- [SearchPipelineDataType.statistic](searchpipelinedatatype/statistic.md)
  A scalar value that reflects a stastical calculation such as an average, minimum, or maximum.
- [SearchPipelineDataType.table](searchpipelinedatatype/table.md)
  Data suitable for a table or chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedatatype/groupeditems)*