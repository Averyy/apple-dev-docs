# items(_:)

**Framework**: Core Spotlight  
**Kind**: method

Creates a pipeline data structure from the an array of searchable items.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func items(_ items: [SearchableItem]) -> SearchPipelineData
```

## Parameters

- `items`: The searchable items your stage produces.

## See Also

- [init(payload: SearchPipelineData.Payload)](searchpipelinedata/init(payload:).md)
  Initializes the pipeline data with the specified payload value.
- [static func scoredItems([ScoredSearchableItem]) -> SearchPipelineData](searchpipelinedata/scoreditems(_:).md)
  Creates a pipeline data structure from the an array of scored searchable items.
- [static func groupedItems([SearchableItemAttribute : [SearchableItem]]) -> SearchPipelineData](searchpipelinedata/groupeditems(_:).md)
  Creates a pipeline data structure from a dictionary of attributes and searchable items.
- [static func text(String) -> SearchPipelineData](searchpipelinedata/text(_:).md)
  Creates a pipeline data structure from a text string.
- [static func count(Int) -> SearchPipelineData](searchpipelinedata/count(_:).md)
  Creates a pipeline data structure from an integer value.
- [static func statistic(name: String, value: Double) -> SearchPipelineData](searchpipelinedata/statistic(name:value:).md)
  Creates a pipeline data structure from statistical information.
- [static func table(SearchResultsTable) -> SearchPipelineData](searchpipelinedata/table(_:).md)
  Creates a pipeline data structure from tabular data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedata/items(_:))*