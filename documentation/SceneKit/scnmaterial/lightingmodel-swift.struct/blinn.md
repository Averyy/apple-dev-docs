# blinn

**Framework**: SceneKit  
**Kind**: property

Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Blinn-Phong  formula.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static let blinn: SCNMaterial.LightingModel
```

#### Discussion

The Blinn-Phong approximation of real-world reflectance calculates the color of a point on a surface using the following formula:

```objc
color = ambient * al + diffuse * max(0, dot(N, L)) + specular * pow(max(0, dot(H, N)), shininess)
```

Some terms refer to the material’s properties: [`ambient`](scnmaterial/ambient.md), [`diffuse`](scnmaterial/diffuse.md), [`specular`](scnmaterial/specular.md), and [`shininess`](scnmaterial/shininess.md). The other terms are as follows:

## See Also

- [static let constant: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/constant.md)
  Uniform shading that incorporates ambient lighting only.
- [static let lambert: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/lambert.md)
  Shading that incorporates ambient and diffuse properties only.
- [static let phong: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/phong.md)
  Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Phong  formula.
- [static let physicallyBased: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/physicallybased.md)
  Shading based on a realistic abstraction of physical lights and materials.
- [static let shadowOnly: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/shadowonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/lightingmodel-swift.struct/blinn)*