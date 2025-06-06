# MDLScatteringFunction

**Framework**: Model I/O  
**Kind**: class

A set of material properties that describes a basic shading model for materials, and the superclass for more complex shading models.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLScatteringFunction
```

#### Overview

The set of material properties that define a material’s response to lighting is also called the , or BRDF, for surfaces shaded using that [`MDLMaterial`](mdlmaterial.md) object. The set of properties defined by the [`MDLScatteringFunction`](mdlscatteringfunction.md) class itself describes a Lambertian shading model with Blinn-Phong specular response; subclasses can define a set of properties for other shading models.

Creating a new scattering function object with the inherited [`init()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/init()) method creates a set of material properties with useful default values for this shading model.

## Topics

### Naming a Scattering Function
- [var name: String](mdlscatteringfunction/name.md)
  A descriptive name for the scattering function.
### Working with Shading Properties
- [var baseColor: MDLMaterialProperty](mdlscatteringfunction/basecolor.md)
  The inherent color of the material, to be used as a modulator during shading.
- [var emission: MDLMaterialProperty](mdlscatteringfunction/emission.md)
  The color emitted as radiance from a material’s surface.
- [var specular: MDLMaterialProperty](mdlscatteringfunction/specular.md)
  The intensity of specular highlights on the material’s surface.
- [var materialIndexOfRefraction: MDLMaterialProperty](mdlscatteringfunction/materialindexofrefraction.md)
  The index of refraction for the medium surrounding a material.
- [var interfaceIndexOfRefraction: MDLMaterialProperty](mdlscatteringfunction/interfaceindexofrefraction.md)
  The index of refraction for a material itself.
- [var normal: MDLMaterialProperty](mdlscatteringfunction/normal.md)
  The variation in the surface normal vectors in a material, relative to model coordinate space.
- [var ambientOcclusion: MDLMaterialProperty](mdlscatteringfunction/ambientocclusion.md)
  The attenuation of ambient light due to local geometry variations on a surface.
- [var ambientOcclusionScale: MDLMaterialProperty](mdlscatteringfunction/ambientocclusionscale.md)
  The scaling factor for ambient occlusion shading.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MDLPhysicallyPlausibleScatteringFunction](mdlphysicallyplausiblescatteringfunction.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLNamed](mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLMaterial](mdlmaterial.md)
  A collection of material properties that together describe the intended surface appearance for rendering a 3D object.
- [class MDLMaterialProperty](mdlmaterialproperty.md)
  A definition for one specific aspect of the rendering parameters for a material.
- [class MDLMaterialPropertyConnection](mdlmaterialpropertyconnection.md)
- [class MDLMaterialPropertyGraph](mdlmaterialpropertygraph.md)
- [class MDLMaterialPropertyNode](mdlmaterialpropertynode.md)
- [class MDLPhysicallyPlausibleScatteringFunction](mdlphysicallyplausiblescatteringfunction.md)
  A set of material properties that describes a physically realistic shading model for materials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlscatteringfunction)*