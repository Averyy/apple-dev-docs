# horizontal

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The alignment on the horizontal axis.

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
var horizontal: HorizontalAlignment
```

#### Discussion

Set this value when you initialize an alignment using the [`init(horizontal:vertical:)`](./init%28horizontal,vertical%29.md) method. Use one of the built-in [`HorizontalAlignment`](../horizontalalignment.md) guides, like [`center`](../horizontalalignment/center.md), or a custom guide that you create.

For information about creating custom guides, see [`AlignmentID`](../alignmentid.md).

## See Also

### Creating a custom alignment
- [init(horizontal: HorizontalAlignment, vertical: VerticalAlignment)](./init%28horizontal,vertical%29.md)
  Creates a custom alignment value with the specified horizontal and vertical alignment guides.
- [var vertical: VerticalAlignment](./vertical.md)
  The alignment on the vertical axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alignment/horizontal)*