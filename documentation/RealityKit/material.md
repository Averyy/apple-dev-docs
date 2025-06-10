# Material

**Framework**: RealityKit  
**Kind**: protocol

A type that describes the material aspects of a mesh, like color and texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
protocol Material
```

## Mentions

- [Adding procedural assets to a scene](adding-procedural-assets-to-a-scene.md)
- [Applying realistic material and lighting effects to entities](applying-realistic-material-and-lighting-effects-to-entities.md)

#### Overview

In RealityKit, a  defines the surface properties of a 3D model. It specifies how RealityKit renders the entity, including its color and whether it’s shiny or reflective. A [`ModelEntity`](modelentity.md) may have one material that defines the way RealityKit renders the entire entity, or it may have several that define the look of different parts of the model.

RealityKit provides several different material structures for different types of rendering, including [`PhysicallyBasedMaterial`](physicallybasedmaterial.md), which is a versatile material capable of simulating real-world objects in a highly realistic manner, and [`UnlitMaterial`](unlitmaterial.md), which RealityKit draws with no lighting effects or shadows.

If you import a model from a USDZ file, RealityKit automatically creates one or more [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) instances from the material properties contained in the file.

## Topics

### Identifying a material
- [var name: String?](material/name.md)
  Name exported with USDz or Reality File asset
### Type Aliases
- [typealias Color](material/color.md)
  An alias for the color type that’s appropriate for the current platform.
- [typealias Parameters](material/parameters.md)
  The parameter type that custom materials uses for properties the framework passes to shader functions.

## Relationships

### Conforming Types
- [CustomMaterial](custommaterial.md)
- [OcclusionMaterial](occlusionmaterial.md)
- [PhysicallyBasedMaterial](physicallybasedmaterial.md)
- [PortalMaterial](portalmaterial.md)
- [ShaderGraphMaterial](shadergraphmaterial.md)
- [SimpleMaterial](simplematerial.md)
- [UnlitMaterial](unlitmaterial.md)
- [VideoMaterial](videomaterial.md)

## See Also

- [typealias Color](material/color.md)
  An alias for the color type that’s appropriate for the current platform.
- [typealias Parameters](material/parameters.md)
  The parameter type that custom materials uses for properties the framework passes to shader functions.
- [struct MaterialParameterTypes](materialparametertypes.md)
  A set of types that material parameters can use.
- [struct MaterialParameters](materialparameters.md)
- [enum MaterialColorParameter](materialcolorparameter.md)
  The color parameter applied to a material.
- [enum MaterialScalarParameter](materialscalarparameter.md)
  The scalar parameter applied to a material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/material)*