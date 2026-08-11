# SearchPipelineDataType.items

**Framework**: Core Spotlight  
**Kind**: case

Searchable items from the app’s index.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case items
```

#### Discussion

The data for this type is zero or more [`CSSearchableItem`](cssearchableitem.md) objects.

## See Also

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
- [SearchPipelineDataType.table](searchpipelinedatatype/table.md)
  Data suitable for a table or chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedatatype/items)*