# outputTextureMaps

**Framework**: RealityKit  
**Kind**: property

The set of texture maps to create in the model.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
var outputTextureMaps: PhotogrammetrySession.Configuration.CustomDetailSpecification.TextureMapOutputs
```

#### Discussion

This setting can reduce model size by only requesting maps that will be used on the target renderer. Example to get just color and normal maps:

```None
var detailSpec = PhotogrammetrySession.Request.Detail.Specification()
detailSpec.outputTextureMaps = [.diffuseColor, .normal]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/configuration-swift.struct/customdetailspecification-swift.struct/outputtexturemaps)*