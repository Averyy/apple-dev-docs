# fillColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A key that contains the behavior to use when filling the empty space around the image.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static let fillColor: NSWorkspace.DesktopImageOptionKey
```

```c
extern NSWorkspaceDesktopImageOptionKey const NSWorkspaceDesktopImageFillColorKey;
```

#### Discussion

The value is the [`NSColor`](../../nscolor.md) object to use when filling any empty space around the image. If you don’t specify this key, the workspace object uses a default color. Currently, the system supports only colors that use or can be converted to use the [`calibratedRGB`](../../nscolorspacename/calibratedrgb.md) color space. The system also ignores any alpha value in the color you specify.

## See Also

### Option Keys
- [static let imageScaling: NSWorkspace.DesktopImageOptionKey](./imagescaling.md)
  A key that contains the behavior to use when scaling the image.
- [static let allowClipping: NSWorkspace.DesktopImageOptionKey](./allowclipping.md)
  A key that contains the behavior to use when clipping the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/desktopimageoptionkey/fillcolor)*