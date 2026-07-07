# LowLevelMaterialResource.ShaderGraphOutput

**Framework**: RealityKit  
**Kind**: struct

The compiled shader functions produced by a ShaderGraph compilation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ShaderGraphOutput
```

## Topics

### Specifying the shaders
- [var surfaceShader: LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/shadergraphoutput/surfaceshader.md)
  The compiled surface shader.
- [var geometryModifier: LowLevelMaterialResource.GeometryModifier?](lowlevelmaterialresource/shadergraphoutput/geometrymodifier.md)
  The compiled geometry modifier, or `nil` if the ShaderGraph does not include one.
### Configuring blending
- [var blending: LowLevelMaterialResource.ShaderGraphOutput.Blending](lowlevelmaterialresource/shadergraphoutput/blending-swift.property.md)
  The blending mode recommended by the ShaderGraph compiler.
- [LowLevelMaterialResource.ShaderGraphOutput.Blending](lowlevelmaterialresource/shadergraphoutput/blending-swift.enum.md)
  Indicates whether the ShaderGraph material should be rendered as opaque or transparent.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/shadergraphoutput)*