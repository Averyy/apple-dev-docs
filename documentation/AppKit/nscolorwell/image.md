# image

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The image to display on the button portion of a color well that adopts the expanded style.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var image: NSImage? { get set }
```

```objc
@property (strong, nullable) NSImage * image;
```

## Discussion

The color well applies the image only when the [`colorWellStyle`](./colorwellstyle.md) property is set to [`NSColorWell.Style.expanded`](./style/expanded.md).

## See Also

### Configuring the appearance
- [var colorWellStyle: NSColorWell.Style](./colorwellstyle.md)
  The appearance and interaction style to apply to the color well.
- [NSColorWell.Style](./style.md)
  Constants that specify the appearance and interaction modes for a color well.
- [var isBordered: Bool](./isbordered.md)
  A Boolean value that determines whether the color well has a border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/image)*