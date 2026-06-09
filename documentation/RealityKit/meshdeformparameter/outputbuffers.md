# outputBuffers

**Framework**: RealityKit  
**Kind**: property

The specified output vertex data for the deformer function.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var outputBuffers: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<OutputBuffer>
```

## See Also

- [var inputBuffers: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<InputBuffer>](meshdeformparameter/inputbuffers.md)
  The specified input vertex data for the deformer function.
- [MeshDeformParameter.VertexBuffers](meshdeformparameter/vertexbuffers.md)
  The vertices requested by the developer when they defined their custom deformations. These will be passed into their custom deformation functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformparameter/outputbuffers)*