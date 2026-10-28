# isBordered

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the color well has a border.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

> **Deprecated**: This property will be deprecated in a future release.

## Declaration

```swift
var isBordered: Bool { get set }
```

```objc
@property (getter=isBordered) BOOL bordered;
```

## Discussion

If the value of this property is [`true`](../../Swift/true.md), the color well has a border; if it’s [`false`](../../Swift/false.md), the color well doesn’t have a border. The default value of this property is [`true`](../../Swift/true.md).

A borderless color well doesn’t display the Colors window when someone clicks it.

## See Also

### Configuring the appearance
- [var colorWellStyle: NSColorWell.Style](./colorwellstyle.md)
  The appearance and interaction style to apply to the color well.
- [NSColorWell.Style](./style.md)
  Constants that specify the appearance and interaction modes for a color well.
- [var image: NSImage?](./image.md)
  The image to display on the button portion of a color well that adopts the expanded style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/isbordered)*