# LowLevelMaterialResource.ShaderGraphOutput

**Framework**: RealityKit  
**Kind**: struct

The compiled Metal shader functions derived from a ShaderGraph.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ShaderGraphOutput
```

#### Overview

Obtain a `ShaderGraphOutput` by calling [`makeShaderGraphFunctions(shaderGraph:constantValues:)`](lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:).md) on [`shaderGraph`](lowlevelrendercontext/shadergraph.md).

## Topics

### Specifying the shaders
- [var surfaceShader: LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/shadergraphoutput/surfaceshader.md)
  The compiled surface shader.
- [var geometryModifier: LowLevelMaterialResource.GeometryModifier?](lowlevelmaterialresource/shadergraphoutput/geometrymodifier.md)
  The compiled geometry modifier, or `nil` if the ShaderGraph does not include one.
### Configuring blending
- [var blending: LowLevelMaterialResource.ShaderGraphOutput.Blending](lowlevelmaterialresource/shadergraphoutput/blending-swift.property.md)
  The blending mode derived from the ShaderGraph material.
- [LowLevelMaterialResource.ShaderGraphOutput.Blending](lowlevelmaterialresource/shadergraphoutput/blending-swift.enum.md)
  Indicates the blending mode of the ShaderGraph material.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/shadergraphoutput)*