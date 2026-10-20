# NSComboButton.Style

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate how a combo button presents its menu.

**Availability**:
- macOS 13.0+

## Declaration

```swift
enum Style
```

```c
enum NSComboButtonStyle : NSInteger;
```

## Topics

### Getting the Combo Button Styles
- [NSComboButton.Style.split](./style-swift.enum/split.md)
  A style that separates the button’s title and image from the menu indicator people use to activate the button.
- [NSComboButton.Style.unified](./style-swift.enum/unified.md)
  A style that unifies the button’s title and image with the menu indicator.
### Initializers
- [init?(rawValue: Int)](./style-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the Button Appearance
- [var style: NSComboButton.Style](./style-swift.property.md)
  The appearance setting that determines how the button presents its menu .
- [var title: String](./title.md)
  The localized string that the button displays.
- [var image: NSImage?](./image.md)
  The image that the button displays.
- [var imageScaling: NSImageScaling](./imagescaling.md)
  The scaling behavior to apply to the button’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobutton/style-swift.enum)*