# SCNMaterial.LightingModel

**Framework**: SceneKit  
**Kind**: struct  
**Role**: Structure

Constants specifying the lighting and shading algorithm to use for rendering a material.

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
struct LightingModel
```

```c
typedef NSString * SCNLightingModel;
```

## Discussion

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2929794@2x.png)

## Topics

### Type Properties
- [static let blinn: SCNMaterial.LightingModel](./lightingmodel-swift.struct/blinn.md)
  Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Blinn-Phong  formula.
- [static let constant: SCNMaterial.LightingModel](./lightingmodel-swift.struct/constant.md)
  Uniform shading that incorporates ambient lighting only.
- [static let lambert: SCNMaterial.LightingModel](./lightingmodel-swift.struct/lambert.md)
  Shading that incorporates ambient and diffuse properties only.
- [static let phong: SCNMaterial.LightingModel](./lightingmodel-swift.struct/phong.md)
  Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Phong  formula.
- [static let physicallyBased: SCNMaterial.LightingModel](./lightingmodel-swift.struct/physicallybased.md)
  Shading based on a realistic abstraction of physical lights and materials.
- [static let shadowOnly: SCNMaterial.LightingModel](./lightingmodel-swift.struct/shadowonly.md)
### Initializers
- [init(rawValue: String)](./lightingmodel-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Choosing a Shading Model
- [var lightingModel: SCNMaterial.LightingModel](./lightingmodel-swift.property.md)
  The lighting formula that SceneKit uses to render the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/lightingmodel-swift.struct)*