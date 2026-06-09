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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/preferredimagevisibility)*