# MTKTextureLoader.CubeLayout

**Framework**: MetalKit  
**Kind**: struct  
**Role**: Structure

Options for specifying how cube texture data is arranged in the source image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct CubeLayout
```

```c
typedef NSString * MTKTextureLoaderCubeLayout;
```

## Topics

### Creating Cube Texture Layout Options
- [init(rawValue: String)](./cubelayout/init%28rawvalue%29.md)
  Creates a cube layout option from a raw string value.
### Specifying Cube Texture Layout Options
- [static let vertical: MTKTextureLoader.CubeLayout](./cubelayout/vertical.md)
  Specifies that the source 2D image is a vertical arrangement of six cube faces.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying Cube Layout
- [static let cubeLayout: MTKTextureLoader.Option](./option/cubelayout.md)
  A key used to specify how cube texture data is arranged in the source image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/cubelayout)*