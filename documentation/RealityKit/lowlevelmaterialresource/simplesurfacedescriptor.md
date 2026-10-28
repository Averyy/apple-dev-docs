# LowLevelMaterialResource.SimpleSurfaceDescriptor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The configuration for a built-in surface shader that applies a tint color, a texture, or both.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct SimpleSurfaceDescriptor
```

## Overview

Pass a `SimpleSurfaceDescriptor` to [`makeSimpleSurfaceShader(descriptor:)`](../lowlevelrendercontext/makesimplesurfaceshader%28descriptor%29-74vhb.md) to compile the corresponding [`LowLevelMaterialResource.SurfaceShader`](./surfaceshader.md) function.

The compiled function’s argument table contains the buffer and texture requirements for the function. Resolve the parameter mappings using the function’s [`LowLevelMaterialParameterMapping`](../lowlevelmaterialparametermapping.md).

## Topics

### Creating a surface descriptor
- [init(useTintColor: Bool, useTexture: Bool, outputChannel: LowLevelMaterialResource.SimpleSurfaceDescriptor.OutputChannel, outputOpacity: Bool)](./simplesurfacedescriptor/init%28usetintcolor,usetexture,outputchannel,outputopacity%29.md)
  Creates a descriptor for the specified combination of inputs and outputs.
### Configuring color sources
- [var useTintColor: Bool](./simplesurfacedescriptor/usetintcolor.md)
  A Boolean value that indicates whether the shader reads a tint color from the argument table and multiplies it with the surface output.
- [var useTexture: Bool](./simplesurfacedescriptor/usetexture.md)
  A Boolean value that indicates whether the shader samples a texture from the argument table and multiplies it with the surface output.
### Configuring the output
- [var outputChannel: LowLevelMaterialResource.SimpleSurfaceDescriptor.OutputChannel](./simplesurfacedescriptor/outputchannel-swift.property.md)
  The surface output channel the shader writes to.
- [LowLevelMaterialResource.SimpleSurfaceDescriptor.OutputChannel](./simplesurfacedescriptor/outputchannel-swift.enum.md)
  The output channel that the simple surface shader writes to.
- [var outputOpacity: Bool](./simplesurfacedescriptor/outputopacity.md)
  A Boolean value that indicates whether the shader also writes the computed alpha to the surface opacity output.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing the material
- [LowLevelMaterialResource.Descriptor](./descriptor.md)
  The geometry modifier, surface shader, and lighting function for a material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/simplesurfacedescriptor)*