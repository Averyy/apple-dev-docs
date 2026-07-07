# NSMenuItem.ImageVisibility

**Framework**: AppKit  
**Kind**: enum

Values for the `preferredImageVisibility` property of NSMenuItem. When a menu item is initialized, the default value for the item’s image visibility is Automatic.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
enum ImageVisibility
```

## Topics

### Enumeration Cases
- [NSMenuItem.ImageVisibility.automatic](nsmenuitem/imagevisibility/automatic.md)
  AppKit should choose whether the item’s image is visible, considering the system configuration.
- [NSMenuItem.ImageVisibility.hidden](nsmenuitem/imagevisibility/hidden.md)
  The item image should not be visible.
- [NSMenuItem.ImageVisibility.visible](nsmenuitem/imagevisibility/visible.md)
  The item image should always be visible. Note that in some cases, AppKit may still hide the image, overriding this preference.
### Initializers
- [init?(rawValue: Int)](nsmenuitem/imagevisibility/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/imagevisibility)*