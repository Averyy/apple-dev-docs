# vertical

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The alignment on the vertical axis.

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
var vertical: VerticalAlignment
```

#### Discussion

Set this value when you initialize an alignment using the [`init(horizontal:vertical:)`](./init%28horizontal,vertical%29.md) method. Use one of the built-in [`VerticalAlignment`](../verticalalignment.md) guides, like [`center`](../verticalalignment/center.md), or a custom guide that you create.

For information about creating custom guides, see [`AlignmentID`](../alignmentid.md).

## See Also

### Creating a custom alignment
- [init(horizontal: HorizontalAlignment, vertical: VerticalAlignment)](./init%28horizontal,vertical%29.md)
  Creates a custom alignment value with the specified horizontal and vertical alignment guides.
- [var horizontal: HorizontalAlignment](./horizontal.md)
  The alignment on the horizontal axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alignment/vertical)*