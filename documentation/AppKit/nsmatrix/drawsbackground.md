# drawsBackground

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the matrix draws its background.

**Availability**:
- macOS

## Declaration

```swift
var drawsBackground: Bool { get set }
```

```objc
@property BOOL drawsBackground;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the matrix draws its background (the space between the cells).

## See Also

### Modifying Graphics Attributes
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The background color of the matrix (the space between the cells).
- [var cellBackgroundColor: NSColor?](./cellbackgroundcolor.md)
  The background color of the matrix’s cells.
- [var drawsCellBackground: Bool](./drawscellbackground.md)
  A Boolean that indicates whether the matrix draws the background within each of its cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/drawsbackground)*