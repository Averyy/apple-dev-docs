# onStateImage

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The image of the menu item that indicates an “on” state.

**Availability**:
- macOS

## Declaration

```swift
var onStateImage: NSImage! { get set }
```

```objc
@property (strong, null_resettable) NSImage * onStateImage;
```

## See Also

### Related Documentation
- [var state: NSControl.StateValue](./state.md)
  The state of the menu item.
### Managing the image
- [var image: NSImage?](./image.md)
  The menu item’s image.
- [var offStateImage: NSImage?](./offstateimage.md)
  The image of the menu item that indicates an “off” state.
- [var mixedStateImage: NSImage!](./mixedstateimage.md)
  The image of the menu item that indicates a “mixed” state, that is, a state neither “on” nor “off.”
- [var preferredImageVisibility: NSMenuItem.ImageVisibility](./preferredimagevisibility.md)
  A menu item’s image visibility determines whether the item’s image is displayed when the menu is open. The default visibility for an item’s image is Automatic. With this value, AppKit determines whether the item’s image is visible based on system configuration. If an item’s image should be visible in all cases, regardless of macOS version or other settings, then set the image visibility to `.visible`.
- [NSMenuItem.ImageVisibility](./imagevisibility.md)
  Values for the `preferredImageVisibility` property of NSMenuItem. When a menu item is initialized, the default value for the item’s image visibility is Automatic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/onstateimage)*