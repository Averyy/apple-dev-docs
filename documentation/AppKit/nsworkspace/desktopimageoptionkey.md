# NSWorkspace.DesktopImageOptionKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Keys that indicate how to display a new desktop image.

**Availability**:
- macOS

## Declaration

```swift
struct DesktopImageOptionKey
```

```c
typedef NSString * NSWorkspaceDesktopImageOptionKey;
```

## Discussion

Specify the following keys when calling the [`setDesktopImageURL(_:for:options:)`](./setdesktopimageurl%28_,for,options%29.md) method.

## Topics

### Option Keys
- [static let imageScaling: NSWorkspace.DesktopImageOptionKey](./desktopimageoptionkey/imagescaling.md)
  A key that contains the behavior to use when scaling the image.
- [static let allowClipping: NSWorkspace.DesktopImageOptionKey](./desktopimageoptionkey/allowclipping.md)
  A key that contains the behavior to use when clipping the image.
- [static let fillColor: NSWorkspace.DesktopImageOptionKey](./desktopimageoptionkey/fillcolor.md)
  A key that contains the behavior to use when filling the empty space around the image.
### Initializers
- [init(rawValue: String)](./desktopimageoptionkey/init%28rawvalue%29.md)
  Initializes an option key using the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the Desktop Image
- [func desktopImageURL(for: NSScreen) -> URL?](./desktopimageurl%28for%29.md)
  Returns the URL for the desktop image for the given screen.
- [func setDesktopImageURL(URL, for: NSScreen, options: [NSWorkspace.DesktopImageOptionKey : Any]) throws](./setdesktopimageurl%28_,for,options%29.md)
  Sets the desktop image for the given screen to the image at the specified URL.
- [func desktopImageOptions(for: NSScreen) -> [NSWorkspace.DesktopImageOptionKey : Any]?](./desktopimageoptions%28for%29.md)
  Returns the desktop image options for the given screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/desktopimageoptionkey)*