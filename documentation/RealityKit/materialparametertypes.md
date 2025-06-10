# MaterialParameterTypes

**Framework**: RealityKit  
**Kind**: struct

A set of types that material parameters can use.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct MaterialParameterTypes
```

#### Overview

This class contains many nested types used to specify various properties of material.

Many material properties support more than one type of data. For example, you can specify [`baseColor`](physicallybasedmaterial/basecolor-swift.property.md) using either a single `Float`, or a UV mapped image texture. MaterialParameterTypes and its nested symbols implement the ability to accept different data types for the same property.

## Topics

### Structures
- [MaterialParameterTypes.TextureCoordinateTransform](materialparametertypes/texturecoordinatetransform.md)
  An object that defines a transformation the framework applies to a material’s UV-mapped textures.
### Enumerations
- [MaterialParameterTypes.BlendMode](materialparametertypes/blendmode.md)
  Modes that describe how materials should be blended with content behind them.
- [MaterialParameterTypes.FaceCulling](materialparametertypes/faceculling.md)
  An object that defines how the system removes polygons before rendering a scene.
- [MaterialParameterTypes.TriangleFillMode](materialparametertypes/trianglefillmode.md)
  An object that defines how the system rasterizes triangles and triangle strips

## See Also

- [protocol Material](material.md)
  A type that describes the material aspects of a mesh, like color and texture.
- [typealias Color](material/color.md)
  An alias for the color type that’s appropriate for the current platform.
- [typealias Parameters](material/parameters.md)
  The parameter type that custom materials uses for properties the framework passes to shader functions.
- [struct MaterialParameters](materialparameters.md)
- [enum MaterialColorParameter](materialcolorparameter.md)
  The color parameter applied to a material.
- [enum MaterialScalarParameter](materialscalarparameter.md)
  The scalar parameter applied to a material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/materialparametertypes)*