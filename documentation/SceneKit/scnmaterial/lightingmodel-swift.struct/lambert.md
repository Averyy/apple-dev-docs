# lambert

**Framework**: SceneKit  
**Kind**: property

Shading that incorporates ambient and diffuse properties only.

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
static let lambert: SCNMaterial.LightingModel
```

#### Discussion

This shading model is based on Lambert’s Law of diffuse reflectance, calculating the color of a point on a surface with the following formula:

```objc
color = ambient * al + diffuse * max(0, dot(N, L))
```

The [`ambient`](scnmaterial/ambient.md) and [`diffuse`](scnmaterial/diffuse.md) terms refer to the material’s properties. The other terms are as follows:

## See Also

- [static let blinn: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/blinn.md)
  Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Blinn-Phong  formula.
- [static let constant: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/constant.md)
  Uniform shading that incorporates ambient lighting only.
- [static let phong: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/phong.md)
  Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Phong  formula.
- [static let physicallyBased: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/physicallybased.md)
  Shading based on a realistic abstraction of physical lights and materials.
- [static let shadowOnly: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/shadowonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/lightingmodel-swift.struct/lambert)*