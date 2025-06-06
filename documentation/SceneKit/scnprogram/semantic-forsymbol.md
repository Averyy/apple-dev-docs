# semantic(forSymbol:)

**Framework**: SceneKit  
**Kind**: method

Returns the SceneKit semantic identifiers associated with the specified GLSL vertex attribute or uniform variable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func semantic(forSymbol symbol: String) -> String?
```

#### Return Value

A SceneKit semantic identifier. See Geometry Semantic Identifiers and Rendering Transform Keys for possible values.

## Parameters

- `symbol`: The name declared in the program’s GLSL source code for a vertex attribute or uniform variable semantic.

## See Also

- [func setSemantic(String?, forSymbol: String, options: [String : Any]?)](scnprogram/setsemantic(_:forsymbol:options:).md)
  Associates a SceneKit semantic identifier with the specified GLSL vertex attribute or uniform variable.
- [let SCNProgramMappingChannelKey: String](scnprogrammappingchannelkey.md)
  The mapping channel to be used for a texture coordinate semantic.
- [let SCNModelTransform: String](scnmodeltransform.md)
  A 4 x 4 matrix for transforming coordinates from model space to scene (or world) space.
- [let SCNModelViewProjectionTransform: String](scnmodelviewprojectiontransform.md)
  A 4 x 4 matrix containing the concatenation of the Model, View, and Projection transformations.
- [let SCNModelViewTransform: String](scnmodelviewtransform.md)
  A 4 x 4 matrix containing the concatenation of the Model and View transformations.
- [let SCNNormalTransform: String](scnnormaltransform.md)
  A 4 x 4 matrix for transforming surface normal vectors from model space to view (or eye) space.
- [let SCNProjectionTransform: String](scnprojectiontransform.md)
  A 4 x 4 matrix for transforming coordinates from view (or eye) space to clip space.
- [let SCNViewTransform: String](scnviewtransform.md)
  A 4 x 4 matrix for transforming coordinates from scene (or world) space to view (or eye) space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/semantic(forsymbol:))*