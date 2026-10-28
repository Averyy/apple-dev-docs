# image

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The image that the button displays.

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

The combo button scales the image to fit within its bounds. Use the [`imageScaling`](./imagescaling.md) property to specify the scaling behavior to use with your image.

## See Also

### Configuring the Button Appearance
- [var style: NSComboButton.Style](./style-swift.property.md)
  The appearance setting that determines how the button presents its menu .
- [NSComboButton.Style](./style-swift.enum.md)
  Constants that indicate how a combo button presents its menu.
- [var title: String](./title.md)
  The localized string that the button displays.
- [var imageScaling: NSImageScaling](./imagescaling.md)
  The scaling behavior to apply to the button’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobutton/image)*