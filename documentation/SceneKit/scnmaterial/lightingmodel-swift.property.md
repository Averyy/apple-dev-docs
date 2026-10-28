# lightingModel

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The lighting formula that SceneKit uses to render the material.

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
var lightingModel: SCNMaterial.LightingModel { get set }
```

```objc
@property (nonatomic, copy) SCNLightingModel lightingModelName;
```

## Discussion

SceneKit provides several different lighting models, each of which combines information from a material’s visual properties with the lights and other contents of a scene. For details on how each lighting model affects rendering, see `Lighting Models`. For details on the contribution from each visual property, see Visual Properties for Special Effects.

## See Also

### Choosing a Shading Model
- [SCNMaterial.LightingModel](./lightingmodel-swift.struct.md)
  Constants specifying the lighting and shading algorithm to use for rendering a material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/lightingmodel-swift.property)*