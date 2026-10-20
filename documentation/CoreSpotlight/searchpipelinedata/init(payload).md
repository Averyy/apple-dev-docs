# init(payload:)

**Framework**: Core Spotlight  
**Kind**: init  
**Role**: Initializer

Initializes the pipeline data with the specified payload value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(payload: SearchPipelineData.Payload)
```

## Parameters

- `payload`: The data your custom stage produced as its output. Use the [`SearchPipelineData.Payload`](./payload-swift.enum.md) type to construct this value.

## See Also

### Configuring the pipeline data
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
- [static func statistic(name: String, value: Double) -> SearchPipelineData](./statistic%28name,value%29.md)
  Creates a pipeline data structure from statistical information.
- [static func table(SearchResultsTable) -> SearchPipelineData](./table%28_%29.md)
  Creates a pipeline data structure from tabular data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedata/init(payload:))*