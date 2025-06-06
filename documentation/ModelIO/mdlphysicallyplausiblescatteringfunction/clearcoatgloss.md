# clearcoatGloss

**Framework**: Model I/O  
**Kind**: property

The sharpness of a second specular highlight, similar to the gloss that results from a clear coat on an automotive finish.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var clearcoatGloss: MDLMaterialProperty { get }
```

#### Discussion

The default value is zero—secondary specular highlights appear blurry.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblescatteringfunction/clearcoatgloss)*