# execute(groupedItems:)

**Framework**: Core Spotlight  
**Kind**: method  
**Required**: Yes

Generates output data from the specified dictionary of attributes and searchable items.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func execute(groupedItems: [SearchableItemAttribute : [SearchableItem]]) async throws -> SearchPipelineData
```

#### Return Value

A pipeline data structure with data your stage produced. Make sure the output you return matches the output you specified in the [`outputType`](customstage/outputtype.md) property.

#### Discussion

If your stage supports a set of searchable items grouped by the keys they support as input, implement this method and use it to generate your stage’s supported output data. Write your code to run in parallel with other instances of your stage and instances of other stages. The best approach is to use only the contents of the `items` parameter and local intermediate values you create to deliver the output data.

## Parameters

- `items`: A dictionary that associates a set of [`CSSearchableItem`](cssearchableitem.md) objects to an attribute key they all contain.

## See Also

- [func execute(items: [SearchableItem]) async throws -> SearchPipelineData](customstage/execute(items:).md)
  Generates output data from an array of searchable items from the app’s Spotlight index.
- [func execute(scoredItems: [ScoredSearchableItem]) async throws -> SearchPipelineData](customstage/execute(scoreditems:).md)
  Generates output data from an array of scored searchable items.
- [func execute(text: String) async throws -> SearchPipelineData](customstage/execute(text:).md)
  Generates output data from the specified input string.
- [func execute(count: Int) async throws -> SearchPipelineData](customstage/execute(count:).md)
  Generates output data from the specified count value.
- [func execute(table: SearchResultsTable) async throws -> SearchPipelineData](customstage/execute(table:).md)
  Generates output data from the specified tabular data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/customstage/execute(groupeditems:))*