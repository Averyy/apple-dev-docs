# backgroundColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The background color of the matrix (the space between the cells).

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var backgroundColor: NSColor { get set }
```

```objc
@property (copy) NSColor * backgroundColor;
```

## Discussion

The value of this property is the background color used to fill the space between cells or the space behind any non-opaque cells. The default background color is the color returned by the [`NSColor`](../nscolor.md) method [`controlColor`](../nscolor/controlcolor.md).

## See Also

### Modifying Graphics Attributes
- [var cellBackgroundColor: NSColor?](./cellbackgroundcolor.md)
  The background color of the matrix’s cells.
- [var drawsBackground: Bool](./drawsbackground.md)
  A Boolean that indicates whether the matrix draws its background.
- [var drawsCellBackground: Bool](./drawscellbackground.md)
  A Boolean that indicates whether the matrix draws the background within each of its cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/backgroundcolor)*