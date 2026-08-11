# SearchPipelineDataType.scoredItems

**Framework**: Core Spotlight  
**Kind**: case

Searchable items with an assigned score.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case scoredItems
```

#### Discussion

The data for this type is zero or more [`ScoredSearchableItem`](scoredsearchableitem.md) objects, each of whic contains a [`CSSearchableItem`](cssearchableitem.md) and its assigned score.

## See Also

- [SearchPipelineDataType.items](searchpipelinedatatype/items.md)
  Searchable items from the app’s index.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedatatype/scoreditems)*