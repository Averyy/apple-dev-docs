# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a custom vertical alignment of the specified type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(_ id: any AlignmentID.Type)
```

#### Discussion

Use this initializer to create a custom vertical alignment. Define an [`AlignmentID`](alignmentid.md) type, and then use that type to create a new static property on [`VerticalAlignment`](verticalalignment.md):

```swift
private struct FirstThirdAlignment: AlignmentID {
    static func defaultValue(in context: ViewDimensions) -> CGFloat {
        context.height / 3
    }
}

extension VerticalAlignment {
    static let firstThird = VerticalAlignment(FirstThirdAlignment.self)
}
```

Every vertical alignment instance that you create needs a unique identifier. For more information, see [`AlignmentID`](alignmentid.md).

## Parameters

- `id`: The type of an identifier that uniquely identifies a   vertical alignment.

## See Also

- [func combineExplicit<S>(S) -> CGFloat?](verticalalignment/combineexplicit(_:).md)
  Merges a sequence of explicit alignment values produced by this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/verticalalignment/init(_:))*