# phong

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Phong  formula.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
static let phong: SCNMaterial.LightingModel
```

```c
extern SCNLightingModel const SCNLightingModelPhong;
```

#### Discussion

The Phong approximation of real-world reflectance calculates the color of a point on a surface using the following formula:

```objc
color = ambient * al + diffuse * max(0, dot(N, L)) + specular * pow(max(0, dot(R, E)), shininess)
```

Some terms refer to the material’s properties: [`ambient`](../ambient.md), [`diffuse`](../diffuse.md), [`specular`](../specular.md), and [`shininess`](../shininess.md). The other terms are as follows:

- **`al`**: The sum of all ambient lights in the scene (a color).
- **`N`**: The surface normal vector at the point being shaded, as supplied by the geometry’s vertex data, interpolated between vertices, and possibly modified by the material’s [`normal`](../normal.md) property.
- **`L`**: The (normalized) vector from the point being shaded to the light source.
- **`E`**: The (normalized) vector from the point being shaded to the viewer.
- **`R`**: The reflection of the light vector `L` across the normal vector `N`.

## See Also

### Type Properties
- [static let blinn: SCNMaterial.LightingModel](./blinn.md)
  Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Blinn-Phong  formula.
- [static let constant: SCNMaterial.LightingModel](./constant.md)
  Uniform shading that incorporates ambient lighting only.
- [static let lambert: SCNMaterial.LightingModel](./lambert.md)
  Shading that incorporates ambient and diffuse properties only.
- [static let physicallyBased: SCNMaterial.LightingModel](./physicallybased.md)
  Shading based on a realistic abstraction of physical lights and materials.
- [static let shadowOnly: SCNMaterial.LightingModel](./shadowonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/lightingmodel-swift.struct/phong)*