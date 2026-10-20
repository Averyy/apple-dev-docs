# NSMenuItem.ImageVisibility.visible

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The item image should always be visible. Note that in some cases, AppKit may still hide the image, overriding this preference.

**Availability**:
- macOS 27.0+

## Declaration

```swift
case visible
```

```c
NSMenuItemImageVisibilityVisible
```

## See Also

### Getting visibility values
- [NSMenuItem.ImageVisibility.automatic](./automatic.md)
  AppKit should choose whether the item’s image is visible, considering the system configuration.
- [NSMenuItem.ImageVisibility.hidden](./hidden.md)
  The item image should not be visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/imagevisibility/visible)*