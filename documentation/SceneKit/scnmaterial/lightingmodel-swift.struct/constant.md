# constant

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Uniform shading that incorporates ambient lighting only.

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
static let constant: SCNMaterial.LightingModel
```

```c
extern SCNLightingModel const SCNLightingModelConstant;
```

## Discussion

This shading model calculates the color of a point on a surface with the following formula:

```objc
color = ambient * al + diffuse
```

The [`ambient`](../ambient.md) and [`diffuse`](../diffuse.md) terms refer to the material’s properties. The `al` term is the sum of all ambient lights in the scene (a color).

## See Also

### Type Properties
- [static let blinn: SCNMaterial.LightingModel](./blinn.md)
  Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Blinn-Phong  formula.
- [static let lambert: SCNMaterial.LightingModel](./lambert.md)
  Shading that incorporates ambient and diffuse properties only.
- [static let phong: SCNMaterial.LightingModel](./phong.md)
  Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Phong  formula.
- [static let physicallyBased: SCNMaterial.LightingModel](./physicallybased.md)
  Shading based on a realistic abstraction of physical lights and materials.
- [static let shadowOnly: SCNMaterial.LightingModel](./shadowonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/lightingmodel-swift.struct/constant)*