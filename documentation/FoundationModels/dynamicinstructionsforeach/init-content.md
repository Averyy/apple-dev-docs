# init(_:content:)

**Framework**: Foundation Models  
**Kind**: init

Creates dynamic instructions that produce content for each element of an identifiable collection.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(_ data: Data, @DynamicInstructionsBuilder content: @escaping (Data.Element) -> Content)
```

#### Discussion

Don’t create this type directly. Instead, use [`DynamicInstructions.ForEach`](dynamicinstructions/foreach.md) within the `body` of your [`DynamicInstructions`](dynamicinstructions.md).

## Parameters

- `data`: The collection whose elements each produce content.
- `content`: A builder closure that produces the dynamic instructions for an element.

## See Also

- [init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> Content)](dynamicinstructionsforeach/init(_:id:content:).md)
  Creates dynamic instructions that produce content for each element of a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructionsforeach/init(_:content:))*