# isBordered

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the color well has a border.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var isBordered: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the color well has a border; if it’s [`false`](https://developer.apple.com/documentation/Swift/false), the color well doesn’t have a border. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

A borderless color well doesn’t display the Colors window when someone clicks it.

## See Also

- [var colorWellStyle: NSColorWell.Style](nscolorwell/colorwellstyle.md)
  The appearance and interaction style to apply to the color well.
- [NSColorWell.Style](nscolorwell/style.md)
  Constants that specify the appearance and interaction modes for a color well.
- [var image: NSImage?](nscolorwell/image.md)
  The image to display on the button portion of a color well that adopts the expanded style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/isbordered)*