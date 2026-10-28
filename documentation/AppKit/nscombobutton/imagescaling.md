# imageScaling

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scaling behavior to apply to the button’s image.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var imageScaling: NSImageScaling { get set }
```

```objc
@property NSImageScaling imageScaling;
```

## Discussion

The default value of this property is [`NSImageScaling.scaleProportionallyDown`](../nsimagescaling/scaleproportionallydown.md).

## See Also

### Configuring the Button Appearance
- [var style: NSComboButton.Style](./style-swift.property.md)
  The appearance setting that determines how the button presents its menu .
- [NSComboButton.Style](./style-swift.enum.md)
  Constants that indicate how a combo button presents its menu.
- [var title: String](./title.md)
  The localized string that the button displays.
- [var image: NSImage?](./image.md)
  The image that the button displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobutton/imagescaling)*