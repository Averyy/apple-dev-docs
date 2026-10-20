# NSMenuItem.ImageVisibility.hidden

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The item image should not be visible.

**Availability**:
- macOS 27.0+

## Declaration

```swift
case hidden
```

```c
NSMenuItemImageVisibilityHidden
```

## See Also

### Getting visibility values
- [NSMenuItem.ImageVisibility.automatic](./automatic.md)
  AppKit should choose whether the item’s image is visible, considering the system configuration.
- [NSMenuItem.ImageVisibility.visible](./visible.md)
  The item image should always be visible. Note that in some cases, AppKit may still hide the image, overriding this preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/imagevisibility/hidden)*