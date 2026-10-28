# execute(items:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Instance Method

Generates output data from an array of searchable items from the app’s Spotlight index.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
nonisolated(nonsending)
func execute(items: [SearchableItem]) async throws -> SearchPipelineData
```

## Return Value

A pipeline data structure with data your stage produced. Make sure the output you return matches the output you specified in the [`outputType`](./outputtype.md) property.

## Discussion

If your stage supports searchable items as input, implement this method and use it to generate your stage’s supported output data. Write your code to run in parallel with other instances of your stage and instances of other stages. The best approach is to use only the contents of the `items` parameter and local intermediate values you create to deliver the output data.

## Parameters

- `items`: A set of [`CSSearchableItem`](../cssearchableitem.md) types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/customstage/execute(items:)-2t5wu)*