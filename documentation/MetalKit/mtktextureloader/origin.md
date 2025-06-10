# MTKTextureLoader.Origin

**Framework**: MetalKit  
**Kind**: struct

Options for specifying when to flip the pixel coordinates of the texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct Origin
```

## Topics

### Creating Texture Origin Options
- [init(rawValue: String)](mtktextureloader/origin/init(rawvalue:).md)
  Creates a texture origin option from a raw string value.
### Specifying Texture Origin Options
- [static let topLeft: MTKTextureLoader.Origin](mtktextureloader/origin/topleft.md)
  An option for specifying images that should be flipped only to put their origin in the top-left corner.
- [static let bottomLeft: MTKTextureLoader.Origin](mtktextureloader/origin/bottomleft.md)
  An option for specifying images that should be flipped only to put their origin in the bottom-left corner.
- [static let flippedVertically: MTKTextureLoader.Origin](mtktextureloader/origin/flippedvertically.md)
  An option that specifies that images should always be flipped.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static let origin: MTKTextureLoader.Option](mtktextureloader/option/origin.md)
  A key used to specify when to flip the pixel coordinates of the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/origin)*