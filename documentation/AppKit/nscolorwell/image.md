# image

**Framework**: AppKit  
**Kind**: property

The image to display on the button portion of a color well that adopts the expanded style.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
var image: NSImage? { get set }
```

#### Discussion

The color well applies the image only when the [`colorWellStyle`](nscolorwell/colorwellstyle.md) property is set to [`NSColorWell.Style.expanded`](nscolorwell/style/expanded.md).

## See Also

- [var colorWellStyle: NSColorWell.Style](nscolorwell/colorwellstyle.md)
  The appearance and interaction style to apply to the color well.
- [NSColorWell.Style](nscolorwell/style.md)
  Constants that specify the appearance and interaction modes for a color well.
- [var isBordered: Bool](nscolorwell/isbordered.md)
  A Boolean value that determines whether the color well has a border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/image)*