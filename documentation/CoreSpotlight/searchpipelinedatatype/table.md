# SearchPipelineDataType.table

**Framework**: Core Spotlight  
**Kind**: case

Data suitable for a table or chart.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case table
```

#### Discussion

The data for this type is a [`SearchResultsTable`](searchresultstable.md) structure, which contains row and column data.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedatatype/table)*