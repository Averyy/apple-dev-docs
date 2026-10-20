# MTKTextureLoader.Origin

**Framework**: MetalKit  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * MTKTextureLoaderOrigin;
```

## Topics

### Creating Texture Origin Options
- [init(rawValue: String)](./origin/init%28rawvalue%29.md)
  Creates a texture origin option from a raw string value.
### Specifying Texture Origin Options
- [static let topLeft: MTKTextureLoader.Origin](./origin/topleft.md)
  An option for specifying images that should be flipped only to put their origin in the top-left corner.
- [static let bottomLeft: MTKTextureLoader.Origin](./origin/bottomleft.md)
  An option for specifying images that should be flipped only to put their origin in the bottom-left corner.
- [static let flippedVertically: MTKTextureLoader.Origin](./origin/flippedvertically.md)
  An option that specifies that images should always be flipped.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying Origin Information
- [static let origin: MTKTextureLoader.Option](./option/origin.md)
  A key used to specify when to flip the pixel coordinates of the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/origin)*