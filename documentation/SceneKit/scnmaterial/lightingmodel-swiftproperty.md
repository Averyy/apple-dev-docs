# lightingModel

**Framework**: SceneKit  
**Kind**: property

The lighting formula that SceneKit uses to render the material.

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
var lightingModel: SCNMaterial.LightingModel { get set }
```

#### Discussion

SceneKit provides several different lighting models, each of which combines information from a material’s visual properties with the lights and other contents of a scene. For details on how each lighting model affects rendering, see `Lighting Models`. For details on the contribution from each visual property, see Visual Properties for Special Effects.

## See Also

- [SCNMaterial.LightingModel](scnmaterial/lightingmodel-swift.struct.md)
  Constants specifying the lighting and shading algorithm to use for rendering a material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/lightingmodel-swift.property)*