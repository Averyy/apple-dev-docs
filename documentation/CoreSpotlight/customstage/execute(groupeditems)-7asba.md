# execute(groupedItems:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Instance Method

Generates output data from the specified dictionary of attributes and searchable items.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
nonisolated(nonsending)
func execute(groupedItems: [SearchableItemAttribute : [SearchableItem]]) async throws -> SearchPipelineData
```

## Return Value

A pipeline data structure with data your stage produced. Make sure the output you return matches the output you specified in the [`outputType`](./outputtype.md) property.

## Discussion

If your stage supports a set of searchable items grouped by the keys they support as input, implement this method and use it to generate your stage’s supported output data. Write your code to run in parallel with other instances of your stage and instances of other stages. The best approach is to use only the contents of the `items` parameter and local intermediate values you create to deliver the output data.

## Parameters

- `items`: A dictionary that associates a set of [`CSSearchableItem`](../cssearchableitem.md) objects to an attribute key they all contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/customstage/execute(groupeditems:)-7asba)*