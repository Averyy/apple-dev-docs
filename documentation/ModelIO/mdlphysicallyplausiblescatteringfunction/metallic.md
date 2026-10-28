# metallic

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The degree to which the material appears as a dielectric surface (lower values) or as a metal (higher values).

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var metallic: MDLMaterialProperty { get }
```

```objc
@property (nonatomic, retain, readonly) MDLMaterialProperty * metallic;
```

## Discussion

The default value is zero.

## See Also

### Working with Shading Properties
- [var subsurface: MDLMaterialProperty](./subsurface.md)
  The degree to which light scatters under the surface of the material.
- [var specularAmount: MDLMaterialProperty](./specularamount.md)
  The tendency of the material to generate specular highlights.
- [var specularTint: MDLMaterialProperty](./speculartint.md)
  The balance of color for specular highlights, between the light color (lower values) and the material’s base color (at higher values).
- [var roughness: MDLMaterialProperty](./roughness.md)
  The degree to which a material appears smooth, affecting both diffuse and specular response.
- [var anisotropic: MDLMaterialProperty](./anisotropic.md)
  The degree to which specular highlights elongate in the direction of the local tangent basis.
- [var anisotropicRotation: MDLMaterialProperty](./anisotropicrotation.md)
  The angle at which anisotropic effects are rotated relative to the local tangent basis.
- [var sheen: MDLMaterialProperty](./sheen.md)
  The intensity of highlights that appear only at glancing angles on a material’s surface.
- [var sheenTint: MDLMaterialProperty](./sheentint.md)
  The balance of color for highlights that appear only at glancing angles, between the light color (lower values) and the material’s base color (at higher values).
- [var clearcoat: MDLMaterialProperty](./clearcoat.md)
  The intensity of a second specular highlight, similar to the gloss that results from a clear coat on an automotive finish.
- [var clearcoatGloss: MDLMaterialProperty](./clearcoatgloss.md)
  The sharpness of a second specular highlight, similar to the gloss that results from a clear coat on an automotive finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblescatteringfunction/metallic)*