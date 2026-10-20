# NSToolbar.DisplayMode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate whether the toolbar displays items using a name, icon, or combination of elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
enum DisplayMode
```

```c
enum NSToolbarDisplayMode : NSUInteger;
```

## Topics

### Display modes
- [NSToolbar.DisplayMode.default](./displaymode-swift.enum/default.md)
  The default display mode.
- [NSToolbar.DisplayMode.iconAndLabel](./displaymode-swift.enum/iconandlabel.md)
  The toolbar displays an icon and label for each item.
- [NSToolbar.DisplayMode.iconOnly](./displaymode-swift.enum/icononly.md)
  The toolbar displays only an icon for each item.
- [NSToolbar.DisplayMode.labelOnly](./displaymode-swift.enum/labelonly.md)
  The toolbar displays only a label for each item.
### Initializers
- [init?(rawValue: UInt)](./displaymode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the toolbar’s behavior
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that indicates whether the toolbar is visible.
- [var displayMode: NSToolbar.DisplayMode](./displaymode-swift.property.md)
  A value that indicates whether the toolbar displays items using a name, icon, or combination of elements.
- [var allowsUserCustomization: Bool](./allowsusercustomization.md)
  A Boolean value that indicates whether users can modify the contents of the toolbar.
- [var allowsExtensionItems: Bool](./allowsextensionitems.md)
  A Boolean value that indicates whether the toolbar can add items for Action extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/displaymode-swift.enum)*