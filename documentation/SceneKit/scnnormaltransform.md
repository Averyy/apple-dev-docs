# SCNNormalTransform

**Framework**: SceneKit  
**Kind**: var

A 4 x 4 matrix for transforming surface normal vectors from model space to view (or eye) space.

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
let SCNNormalTransform: String
```

## See Also

- [func setSemantic(String?, forSymbol: String, options: [String : Any]?)](scnprogram/setsemantic(_:forsymbol:options:).md)
  Associates a SceneKit semantic identifier with the specified GLSL vertex attribute or uniform variable.
- [let SCNProgramMappingChannelKey: String](scnprogrammappingchannelkey.md)
  The mapping channel to be used for a texture coordinate semantic.
- [func semantic(forSymbol: String) -> String?](scnprogram/semantic(forsymbol:).md)
  Returns the SceneKit semantic identifiers associated with the specified GLSL vertex attribute or uniform variable.
- [let SCNModelTransform: String](scnmodeltransform.md)
  A 4 x 4 matrix for transforming coordinates from model space to scene (or world) space.
- [let SCNModelViewProjectionTransform: String](scnmodelviewprojectiontransform.md)
  A 4 x 4 matrix containing the concatenation of the Model, View, and Projection transformations.
- [let SCNModelViewTransform: String](scnmodelviewtransform.md)
  A 4 x 4 matrix containing the concatenation of the Model and View transformations.
- [let SCNProjectionTransform: String](scnprojectiontransform.md)
  A 4 x 4 matrix for transforming coordinates from view (or eye) space to clip space.
- [let SCNViewTransform: String](scnviewtransform.md)
  A 4 x 4 matrix for transforming coordinates from scene (or world) space to view (or eye) space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnormaltransform)*