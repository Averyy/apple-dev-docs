# NSWorkspace.DesktopImageOptionKey

**Framework**: AppKit  
**Kind**: struct

Keys that indicate how to display a new desktop image.

**Availability**:
- macOS ?+

## Declaration

```swift
struct DesktopImageOptionKey
```

#### Discussion

Specify the following keys when calling the [`setDesktopImageURL(_:for:options:)`](nsworkspace/setdesktopimageurl(_:for:options:).md) method.

## Topics

### Option Keys
- [static let imageScaling: NSWorkspace.DesktopImageOptionKey](nsworkspace/desktopimageoptionkey/imagescaling.md)
  A key that contains the behavior to use when scaling the image.
- [static let allowClipping: NSWorkspace.DesktopImageOptionKey](nsworkspace/desktopimageoptionkey/allowclipping.md)
  A key that contains the behavior to use when clipping the image.
- [static let fillColor: NSWorkspace.DesktopImageOptionKey](nsworkspace/desktopimageoptionkey/fillcolor.md)
  A key that contains the behavior to use when filling the empty space around the image.
### Initializers
- [init(rawValue: String)](nsworkspace/desktopimageoptionkey/init(rawvalue:).md)
  Initializes an option key using the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func desktopImageURL(for: NSScreen) -> URL?](nsworkspace/desktopimageurl(for:).md)
  Returns the URL for the desktop image for the given screen.
- [func setDesktopImageURL(URL, for: NSScreen, options: [NSWorkspace.DesktopImageOptionKey : Any]) throws](nsworkspace/setdesktopimageurl(_:for:options:).md)
  Sets the desktop image for the given screen to the image at the specified URL.
- [func desktopImageOptions(for: NSScreen) -> [NSWorkspace.DesktopImageOptionKey : Any]?](nsworkspace/desktopimageoptions(for:).md)
  Returns the desktop image options for the given screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/desktopimageoptionkey)*