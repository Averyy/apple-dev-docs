# NSMenuItem.ImageVisibility

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Values for the `preferredImageVisibility` property of NSMenuItem. When a menu item is initialized, the default value for the item’s image visibility is Automatic.

**Availability**:
- macOS 27.0+

## Declaration

```swift
enum ImageVisibility
```

```c
enum NSMenuItemImageVisibility : NSInteger;
```

## Topics

### Getting visibility values
- [NSMenuItem.ImageVisibility.automatic](./imagevisibility/automatic.md)
  AppKit should choose whether the item’s image is visible, considering the system configuration.
- [NSMenuItem.ImageVisibility.hidden](./imagevisibility/hidden.md)
  The item image should not be visible.
- [NSMenuItem.ImageVisibility.visible](./imagevisibility/visible.md)
  The item image should always be visible. Note that in some cases, AppKit may still hide the image, overriding this preference.
### Initializers
- [init?(rawValue: Int)](./imagevisibility/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the image
- [var image: NSImage?](./image.md)
  The menu item’s image.
- [var onStateImage: NSImage!](./onstateimage.md)
  The image of the menu item that indicates an “on” state.
- [var offStateImage: NSImage?](./offstateimage.md)
  The image of the menu item that indicates an “off” state.
- [var mixedStateImage: NSImage!](./mixedstateimage.md)
  The image of the menu item that indicates a “mixed” state, that is, a state neither “on” nor “off.”
- [var preferredImageVisibility: NSMenuItem.ImageVisibility](./preferredimagevisibility.md)
  A menu item’s image visibility determines whether the item’s image is displayed when the menu is open. The default visibility for an item’s image is Automatic. With this value, AppKit determines whether the item’s image is visible based on system configuration. If an item’s image should be visible in all cases, regardless of macOS version or other settings, then set the image visibility to `.visible`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/imagevisibility)*