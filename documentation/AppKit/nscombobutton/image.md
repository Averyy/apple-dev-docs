# image

**Framework**: AppKit  
**Kind**: property

The image that the button displays.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
var image: NSImage? { get set }
```

#### Discussion

The combo button scales the image to fit within its bounds. Use the [`imageScaling`](nscombobutton/imagescaling.md) property to specify the scaling behavior to use with your image.

## See Also

- [var style: NSComboButton.Style](nscombobutton/style-swift.property.md)
  The appearance setting that determines how the button presents its menu .
- [NSComboButton.Style](nscombobutton/style-swift.enum.md)
  Constants that indicate how a combo button presents its menu.
- [var title: String](nscombobutton/title.md)
  The localized string that the button displays.
- [var imageScaling: NSImageScaling](nscombobutton/imagescaling.md)
  The scaling behavior to apply to the button’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobutton/image)*