# NSColorWell.Style

**Framework**: AppKit  
**Kind**: enum

Constants that specify the appearance and interaction modes for a color well.

**Availability**:
- macOS 13.0+

## Declaration

```swift
enum Style
```

## Topics

### Getting the Style Option
- [NSColorWell.Style.default](nscolorwell/style/default.md)
  The default style for color wells.
- [NSColorWell.Style.minimal](nscolorwell/style/minimal.md)
  A style that adds minimal adornments to the color well.
- [NSColorWell.Style.expanded](nscolorwell/style/expanded.md)
  A style that supports a color picker popover for fast interactions, and adds a dedicated button to display the color panel.
### Initializers
- [init?(rawValue: Int)](nscolorwell/style/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var colorWellStyle: NSColorWell.Style](nscolorwell/colorwellstyle.md)
  The appearance and interaction style to apply to the color well.
- [var image: NSImage?](nscolorwell/image.md)
  The image to display on the button portion of a color well that adopts the expanded style.
- [var isBordered: Bool](nscolorwell/isbordered.md)
  A Boolean value that determines whether the color well has a border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/style)*