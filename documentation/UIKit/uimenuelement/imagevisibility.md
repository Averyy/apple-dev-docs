# UIMenuElement.ImageVisibility

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Visibility options for a menu element’s image.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum ImageVisibility
```

```c
enum UIMenuElementImageVisibility : NSInteger;
```

## Topics

### Enumeration Cases
- [UIMenuElement.ImageVisibility.automatic](./imagevisibility/automatic.md)
  The element’s image visibility is determined by the platform and context.
- [UIMenuElement.ImageVisibility.hidden](./imagevisibility/hidden.md)
  The element prefers its image to be hidden, even in contexts where images are shown by default.
- [UIMenuElement.ImageVisibility.visible](./imagevisibility/visible.md)
  The element prefers its image to be visible, even in contexts where images are not shown by default.
### Initializers
- [init?(rawValue: Int)](./imagevisibility/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuelement/imagevisibility)*