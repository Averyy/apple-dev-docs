# init(_:id:content:)

**Framework**: Foundation Models  
**Kind**: init

Creates dynamic instructions that produce content for each element of a collection.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(_ data: Data, id: KeyPath<Data.Element, ID>, @DynamicInstructionsBuilder content: @escaping (Data.Element) -> Content)
```

#### Discussion

Don’t create this type directly. Instead, use [`DynamicInstructions.ForEach`](dynamicinstructions/foreach.md) within the `body` of your [`DynamicInstructions`](dynamicinstructions.md).

## Parameters

- `data`: The collection whose elements each produce content.
- `id`: A key path to a property that uniquely identifies each element.
- `content`: A builder closure that produces the dynamic instructions for an element.

## See Also

- [init(Data, content: (Data.Element) -> Content)](dynamicinstructionsforeach/init(_:content:).md)
  Creates dynamic instructions that produce content for each element of an identifiable collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructionsforeach/init(_:id:content:))*