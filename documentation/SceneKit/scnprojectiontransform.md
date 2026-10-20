# SCNProjectionTransform

**Framework**: SceneKit  
**Kind**: var  
**Role**: Global Variable

A 4 x 4 matrix for transforming coordinates from view (or eye) space to clip space.

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
let SCNProjectionTransform: String
```

```c
extern NSString * const SCNProjectionTransform;
```

## See Also

### Mapping GLSL Symbols to SceneKit Semantics
- [func setSemantic(String?, forSymbol: String, options: [String : Any]?)](./scnprogram/setsemantic%28_,forsymbol,options%29.md)
  Associates a SceneKit semantic identifier with the specified GLSL vertex attribute or uniform variable.
- [let SCNProgramMappingChannelKey: String](./scnprogrammappingchannelkey.md)
  The mapping channel to be used for a texture coordinate semantic.
- [func semantic(forSymbol: String) -> String?](./scnprogram/semantic%28forsymbol%29.md)
  Returns the SceneKit semantic identifiers associated with the specified GLSL vertex attribute or uniform variable.
- [let SCNModelTransform: String](./scnmodeltransform.md)
  A 4 x 4 matrix for transforming coordinates from model space to scene (or world) space.
- [let SCNModelViewProjectionTransform: String](./scnmodelviewprojectiontransform.md)
  A 4 x 4 matrix containing the concatenation of the Model, View, and Projection transformations.
- [let SCNModelViewTransform: String](./scnmodelviewtransform.md)
  A 4 x 4 matrix containing the concatenation of the Model and View transformations.
- [let SCNNormalTransform: String](./scnnormaltransform.md)
  A 4 x 4 matrix for transforming surface normal vectors from model space to view (or eye) space.
- [let SCNViewTransform: String](./scnviewtransform.md)
  A 4 x 4 matrix for transforming coordinates from scene (or world) space to view (or eye) space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprojectiontransform)*