# NSColorWell.Style

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the appearance and interaction modes for a color well.

**Availability**:
- macOS 13.0+

## Declaration

```swift
enum Style
```

```c
enum NSColorWellStyle : NSInteger;
```

## Topics

### Getting the Style Option
- [NSColorWell.Style.default](./style/default.md)
  The default style for color wells.
- [NSColorWell.Style.minimal](./style/minimal.md)
  A style that adds minimal adornments to the color well.
- [NSColorWell.Style.expanded](./style/expanded.md)
  A style that supports a color picker popover for fast interactions, and adds a dedicated button to display the color panel.
### Initializers
- [init?(rawValue: Int)](./style/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the appearance
- [var colorWellStyle: NSColorWell.Style](./colorwellstyle.md)
  The appearance and interaction style to apply to the color well.
- [var image: NSImage?](./image.md)
  The image to display on the button portion of a color well that adopts the expanded style.
- [var isBordered: Bool](./isbordered.md)
  A Boolean value that determines whether the color well has a border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/style)*