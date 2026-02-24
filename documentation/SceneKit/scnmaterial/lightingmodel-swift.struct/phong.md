# phong

**Framework**: SceneKit  
**Kind**: property

Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Phong  formula.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let phong: SCNMaterial.LightingModel
```

#### Discussion

The Phong approximation of real-world reflectance calculates the color of a point on a surface using the following formula:

```objc
color = ambient * al + diffuse * max(0, dot(N, L)) + specular * pow(max(0, dot(R, E)), shininess)
```

Some terms refer to the material’s properties: [`ambient`](scnmaterial/ambient.md), [`diffuse`](scnmaterial/diffuse.md), [`specular`](scnmaterial/specular.md), and [`shininess`](scnmaterial/shininess.md). The other terms are as follows:

- **`al`**: The sum of all ambient lights in the scene (a color).
- **`N`**: The surface normal vector at the point being shaded, as supplied by the geometry’s vertex data, interpolated between vertices, and possibly modified by the material’s [`normal`](scnmaterial/normal.md) property.
- **`L`**: The (normalized) vector from the point being shaded to the light source.
- **`E`**: The (normalized) vector from the point being shaded to the viewer.
- **`R`**: The reflection of the light vector `L` across the normal vector `N`.

## See Also

- [static let blinn: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/blinn.md)
  Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Blinn-Phong  formula.
- [static let constant: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/constant.md)
  Uniform shading that incorporates ambient lighting only.
- [static let lambert: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/lambert.md)
  Shading that incorporates ambient and diffuse properties only.
- [static let physicallyBased: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/physicallybased.md)
  Shading based on a realistic abstraction of physical lights and materials.
- [static let shadowOnly: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/shadowonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/lightingmodel-swift.struct/phong)*