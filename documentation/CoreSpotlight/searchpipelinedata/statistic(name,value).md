# statistic(name:value:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Type Method

Creates a pipeline data structure from statistical information.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func statistic(name: String, value: Double) -> SearchPipelineData
```

## Parameters

- `name`: The name of the statistic your stage produced. Specify strings like “average”, “max”, “min”, “sum”, “median”, or “stddev”.
- `value`: The statistical value you generated.

## See Also

### Configuring the pipeline data
- [init(payload: SearchPipelineData.Payload)](./init%28payload%29.md)
  Initializes the pipeline data with the specified payload value.
- [static func items([SearchableItem]) -> SearchPipelineData](./items%28_%29.md)
  Creates a pipeline data structure from the an array of searchable items.
- [static func scoredItems([ScoredSearchableItem]) -> SearchPipelineData](./scoreditems%28_%29.md)
  Creates a pipeline data structure from the an array of scored searchable items.
- [static func groupedItems([SearchableItemAttribute : [SearchableItem]]) -> SearchPipelineData](./groupeditems%28_%29.md)
  Creates a pipeline data structure from a dictionary of attributes and searchable items.
- [static func text(String) -> SearchPipelineData](./text%28_%29.md)
  Creates a pipeline data structure from a text string.
- [static func count(Int) -> SearchPipelineData](./count%28_%29.md)
  Creates a pipeline data structure from an integer value.
- [static func table(SearchResultsTable) -> SearchPipelineData](./table%28_%29.md)
  Creates a pipeline data structure from tabular data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedata/statistic(name:value:))*