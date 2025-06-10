# SCNMaterial.LightingModel

**Framework**: SceneKit  
**Kind**: struct

Constants specifying the lighting and shading algorithm to use for rendering a material.

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
struct LightingModel
```

#### Discussion

![None](https://docs-assets.developer.apple.com/published/a1b3893bc30880a4d37b9f6536e168ee/media-2929794%402x.png)

## Topics

### Type Properties
- [static let blinn: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/blinn.md)
  Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Blinn-Phong  formula.
- [static let constant: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/constant.md)
  Uniform shading that incorporates ambient lighting only.
- [static let lambert: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/lambert.md)
  Shading that incorporates ambient and diffuse properties only.
- [static let phong: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/phong.md)
  Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Phong  formula.
- [static let physicallyBased: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/physicallybased.md)
  Shading based on a realistic abstraction of physical lights and materials.
- [static let shadowOnly: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct/shadowonly.md)
### Initializers
- [init(rawValue: String)](scnmaterial/lightingmodel-swift.struct/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var lightingModel: SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.property.md)
  The lighting formula that SceneKit uses to render the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/lightingmodel-swift.struct)*