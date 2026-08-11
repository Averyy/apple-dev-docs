# preferredImageVisibility

**Framework**: AppKit  
**Kind**: property

A menu item’s image visibility determines whether the item’s image is displayed when the menu is open. The default visibility for an item’s image is Automatic. With this value, AppKit determines whether the item’s image is visible based on system configuration. If an item’s image should be visible in all cases, regardless of macOS version or other settings, then set the image visibility to `.visible`.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var preferredImageVisibility: NSMenuItem.ImageVisibility { get set }
```

## See Also

- [var image: NSImage?](nsmenuitem/image.md)
  The menu item’s image.
- [var onStateImage: NSImage!](nsmenuitem/onstateimage.md)
  The image of the menu item that indicates an “on” state.
- [var offStateImage: NSImage?](nsmenuitem/offstateimage.md)
  The image of the menu item that indicates an “off” state.
- [var mixedStateImage: NSImage!](nsmenuitem/mixedstateimage.md)
  The image of the menu item that indicates a “mixed” state, that is, a state neither “on” nor “off.”
- [NSMenuItem.ImageVisibility](nsmenuitem/imagevisibility.md)
  Values for the `preferredImageVisibility` property of NSMenuItem. When a menu item is initialized, the default value for the item’s image visibility is Automatic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/preferredimagevisibility)*