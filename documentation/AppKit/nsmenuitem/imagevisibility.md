# NSMenuItem.ImageVisibility

**Framework**: AppKit  
**Kind**: enum

Values for the `preferredImageVisibility` property of NSMenuItem. When a menu item is initialized, the default value for the item’s image visibility is Automatic.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
enum ImageVisibility
```

## Topics

### Getting visibility values
- [NSMenuItem.ImageVisibility.automatic](nsmenuitem/imagevisibility/automatic.md)
  AppKit should choose whether the item’s image is visible, considering the system configuration.
- [NSMenuItem.ImageVisibility.hidden](nsmenuitem/imagevisibility/hidden.md)
  The item image should not be visible.
- [NSMenuItem.ImageVisibility.visible](nsmenuitem/imagevisibility/visible.md)
  The item image should always be visible. Note that in some cases, AppKit may still hide the image, overriding this preference.
### Initializers
- [init?(rawValue: Int)](nsmenuitem/imagevisibility/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var image: NSImage?](nsmenuitem/image.md)
  The menu item’s image.
- [var onStateImage: NSImage!](nsmenuitem/onstateimage.md)
  The image of the menu item that indicates an “on” state.
- [var offStateImage: NSImage?](nsmenuitem/offstateimage.md)
  The image of the menu item that indicates an “off” state.
- [var mixedStateImage: NSImage!](nsmenuitem/mixedstateimage.md)
  The image of the menu item that indicates a “mixed” state, that is, a state neither “on” nor “off.”
- [var preferredImageVisibility: NSMenuItem.ImageVisibility](nsmenuitem/preferredimagevisibility.md)
  A menu item’s image visibility determines whether the item’s image is displayed when the menu is open. The default visibility for an item’s image is Automatic. With this value, AppKit determines whether the item’s image is visible based on system configuration. If an item’s image should be visible in all cases, regardless of macOS version or other settings, then set the image visibility to `.visible`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/imagevisibility)*