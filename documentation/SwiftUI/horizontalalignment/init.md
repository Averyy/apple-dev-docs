# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a custom horizontal alignment of the specified type.

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

Use this initializer to create a custom horizontal alignment. Define an [`AlignmentID`](alignmentid.md) type, and then use that type to create a new static property on [`HorizontalAlignment`](horizontalalignment.md):

```swift
private struct OneQuarterAlignment: AlignmentID {
    static func defaultValue(in context: ViewDimensions) -> CGFloat {
        context.width / 4
    }
}

extension HorizontalAlignment {
    static let oneQuarter = HorizontalAlignment(OneQuarterAlignment.self)
}
```

Every horizontal alignment instance that you create needs a unique identifier. For more information, see [`AlignmentID`](alignmentid.md).

## Parameters

- `id`: The type of an identifier that uniquely identifies a   horizontal alignment.

## See Also

- [func combineExplicit<S>(S) -> CGFloat?](horizontalalignment/combineexplicit(_:).md)
  Merges a sequence of explicit alignment values produced by this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/horizontalalignment/init(_:))*