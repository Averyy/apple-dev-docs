# drawsCellBackground

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the matrix draws the background within each of its cells.

**Availability**:
- macOS

## Declaration

```swift
var drawsCellBackground: Bool { get set }
```

```objc
@property BOOL drawsCellBackground;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the matrix draws the cell background.

## See Also

### Modifying Graphics Attributes
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The background color of the matrix (the space between the cells).
- [var cellBackgroundColor: NSColor?](./cellbackgroundcolor.md)
  The background color of the matrix’s cells.
- [var drawsBackground: Bool](./drawsbackground.md)
  A Boolean that indicates whether the matrix draws its background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/drawscellbackground)*