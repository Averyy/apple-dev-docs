# image

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The menu item’s image.

**Availability**:
- macOS

## Declaration

```swift
var image: NSImage? { get set }
```

```objc
@property (strong, nullable) NSImage * image;
```

## Discussion

The menu item’s image is not affected by changes in its state.

## See Also

### Managing the image
- [var onStateImage: NSImage!](./onstateimage.md)
  The image of the menu item that indicates an “on” state.
- [var offStateImage: NSImage?](./offstateimage.md)
  The image of the menu item that indicates an “off” state.
- [var mixedStateImage: NSImage!](./mixedstateimage.md)
  The image of the menu item that indicates a “mixed” state, that is, a state neither “on” nor “off.”
- [var preferredImageVisibility: NSMenuItem.ImageVisibility](./preferredimagevisibility.md)
  A menu item’s image visibility determines whether the item’s image is displayed when the menu is open. The default visibility for an item’s image is Automatic. With this value, AppKit determines whether the item’s image is visible based on system configuration. If an item’s image should be visible in all cases, regardless of macOS version or other settings, then set the image visibility to `.visible`.
- [NSMenuItem.ImageVisibility](./imagevisibility.md)
  Values for the `preferredImageVisibility` property of NSMenuItem. When a menu item is initialized, the default value for the item’s image visibility is Automatic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/image)*