# init(horizontal:vertical:)

**Framework**: SwiftUI  
**Kind**: init

Creates a custom alignment value with the specified horizontal and vertical alignment guides.

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
init(horizontal: HorizontalAlignment, vertical: VerticalAlignment)
```

#### Discussion

SwiftUI provides a variety of built-in alignments that combine built-in [`HorizontalAlignment`](horizontalalignment.md) and [`VerticalAlignment`](verticalalignment.md) guides. Use this initializer to create a custom alignment that makes use of a custom horizontal or vertical guide, or both.

For example, you can combine a custom vertical guide called `firstThird` with the built-in [`center`](horizontalalignment/center.md) guide, and use it to configure a [`ZStack`](zstack.md):

```swift
ZStack(alignment: Alignment(horizontal: .center, vertical: .firstThird)) {
    // ...
}
```

For more information about creating custom guides, including the code that creates the custom `firstThird` alignment in the example above, see [`AlignmentID`](alignmentid.md).

## Parameters

- `horizontal`: The alignment on the horizontal axis.
- `vertical`: The alignment on the vertical axis.

## See Also

- [var horizontal: HorizontalAlignment](alignment/horizontal.md)
  The alignment on the horizontal axis.
- [var vertical: VerticalAlignment](alignment/vertical.md)
  The alignment on the vertical axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alignment/init(horizontal:vertical:))*