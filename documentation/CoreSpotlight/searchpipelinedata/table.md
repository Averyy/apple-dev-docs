# table(_:)

**Framework**: Core Spotlight  
**Kind**: method

Creates a pipeline data structure from tabular data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func table(_ t: SearchResultsTable) -> SearchPipelineData
```

## Parameters

- `t`: The column and row data your stage produced.

## See Also

- [init(payload: SearchPipelineData.Payload)](searchpipelinedata/init(payload:).md)
  Initializes the pipeline data with the specified payload value.
- [static func items([SearchableItem]) -> SearchPipelineData](searchpipelinedata/items(_:).md)
  Creates a pipeline data structure from the an array of searchable items.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedata/table(_:))*