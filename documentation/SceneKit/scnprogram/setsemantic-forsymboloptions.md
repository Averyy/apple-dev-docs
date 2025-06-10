# setSemantic(_:forSymbol:options:)

**Framework**: SceneKit  
**Kind**: method

Associates a SceneKit semantic identifier with the specified GLSL vertex attribute or uniform variable.

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
func setSemantic(_ semantic: String?, forSymbol symbol: String, options: [String : Any]? = nil)
```

#### Discussion

Use this method to provide inputs managed by SceneKit to your GLSL program.

To use vertex attributes provided by [`SCNGeometry`](scngeometry.md) objects, use the constants listed in Geometry Semantic Identifiers.

To use the coordinate transformations defined by the scene’s node hierarchy and point-of-view camera, use the constants listed in Rendering Transform Keys.

## Parameters

- `semantic`: A SceneKit semantic identifier. See Geometry Semantic Identifiers and Rendering Transform Keys for possible values.
- `symbol`: The name declared in the program’s GLSL source code for the vertex attribute or uniform variable to be associated with the semantic.
- `options`: A dictionary of options affecting the semantic. See   for applicable keys and values.

## See Also

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
- [let SCNNormalTransform: String](scnnormaltransform.md)
  A 4 x 4 matrix for transforming surface normal vectors from model space to view (or eye) space.
- [let SCNProjectionTransform: String](scnprojectiontransform.md)
  A 4 x 4 matrix for transforming coordinates from view (or eye) space to clip space.
- [let SCNViewTransform: String](scnviewtransform.md)
  A 4 x 4 matrix for transforming coordinates from scene (or world) space to view (or eye) space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/setsemantic(_:forsymbol:options:))*