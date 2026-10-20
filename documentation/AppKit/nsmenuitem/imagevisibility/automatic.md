# NSMenuItem.ImageVisibility.automatic

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

AppKit should choose whether the item’s image is visible, considering the system configuration.

**Availability**:
- macOS 27.0+

## Declaration

```swift
case automatic
```

```c
NSMenuItemImageVisibilityAutomatic
```

## See Also

### Getting visibility values
- [NSMenuItem.ImageVisibility.hidden](./hidden.md)
  The item image should not be visible.
- [NSMenuItem.ImageVisibility.visible](./visible.md)
  The item image should always be visible. Note that in some cases, AppKit may still hide the image, overriding this preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/imagevisibility/automatic)*