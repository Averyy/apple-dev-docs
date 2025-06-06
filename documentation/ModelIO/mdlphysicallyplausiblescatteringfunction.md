# MDLPhysicallyPlausibleScatteringFunction

**Framework**: Model I/O  
**Kind**: class

A set of material properties that describes a physically realistic shading model for materials.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLPhysicallyPlausibleScatteringFunction
```

#### Overview

The set of material properties that define a material’s response to lighting is also called the , or BRDF, for surfaces shaded using that MDLMaterial object. The properties defined by this class, along with some properties inherited from the superclass [`MDLScatteringFunction`](mdlscatteringfunction.md), describe a shading model that more closely simulates real-world lighting physics than traditional shading models. (This shading model is similar to those used in recent game engines and feature films.)

The valid range for each material property in this shading function is `0.0` to `1.0`, inclusive. Creating a new scattering function object with the inherited [`init()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/init()) method creates a set of material properties with useful default values for this shading model.

## Topics

### Working with Shading Properties
- [var subsurface: MDLMaterialProperty](mdlphysicallyplausiblescatteringfunction/subsurface.md)
  The degree to which light scatters under the surface of the material.
- [var metallic: MDLMaterialProperty](mdlphysicallyplausiblescatteringfunction/metallic.md)
  The degree to which the material appears as a dielectric surface (lower values) or as a metal (higher values).
- [var specularAmount: MDLMaterialProperty](mdlphysicallyplausiblescatteringfunction/specularamount.md)
  The tendency of the material to generate specular highlights.
- [var specularTint: MDLMaterialProperty](mdlphysicallyplausiblescatteringfunction/speculartint.md)
  The balance of color for specular highlights, between the light color (lower values) and the material’s base color (at higher values).
- [var roughness: MDLMaterialProperty](mdlphysicallyplausiblescatteringfunction/roughness.md)
  The degree to which a material appears smooth, affecting both diffuse and specular response.
- [var anisotropic: MDLMaterialProperty](mdlphysicallyplausiblescatteringfunction/anisotropic.md)
  The degree to which specular highlights elongate in the direction of the local tangent basis.
- [var anisotropicRotation: MDLMaterialProperty](mdlphysicallyplausiblescatteringfunction/anisotropicrotation.md)
  The angle at which anisotropic effects are rotated relative to the local tangent basis.
- [var sheen: MDLMaterialProperty](mdlphysicallyplausiblescatteringfunction/sheen.md)
  The intensity of highlights that appear only at glancing angles on a material’s surface.
- [var sheenTint: MDLMaterialProperty](mdlphysicallyplausiblescatteringfunction/sheentint.md)
  The balance of color for highlights that appear only at glancing angles, between the light color (lower values) and the material’s base color (at higher values).
- [var clearcoat: MDLMaterialProperty](mdlphysicallyplausiblescatteringfunction/clearcoat.md)
  The intensity of a second specular highlight, similar to the gloss that results from a clear coat on an automotive finish.
- [var clearcoatGloss: MDLMaterialProperty](mdlphysicallyplausiblescatteringfunction/clearcoatgloss.md)
  The sharpness of a second specular highlight, similar to the gloss that results from a clear coat on an automotive finish.
### Instance Properties
- [var version: Int](mdlphysicallyplausiblescatteringfunction/version.md)

## Relationships

### Inherits From
- [MDLScatteringFunction](mdlscatteringfunction.md)
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
- [class MDLScatteringFunction](mdlscatteringfunction.md)
  A set of material properties that describes a basic shading model for materials, and the superclass for more complex shading models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblescatteringfunction)*