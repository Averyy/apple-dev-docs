# style

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The appearance setting that determines how the button presents its menu .

**Availability**:
- macOS 13.0+

## Declaration

```swift
var style: NSComboButton.Style { get set }
```

```objc
@property NSComboButtonStyle style;
```

#### Discussion

The default value of this property is [`NSComboButton.Style.split`](./style-swift.enum/split.md).

## See Also

### Configuring the Button Appearance
- [NSComboButton.Style](./style-swift.enum.md)
  Constants that indicate how a combo button presents its menu.
- [var title: String](./title.md)
  The localized string that the button displays.
- [var image: NSImage?](./image.md)
  The image that the button displays.
- [var imageScaling: NSImageScaling](./imagescaling.md)
  The scaling behavior to apply to the button’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobutton/style-swift.property)*