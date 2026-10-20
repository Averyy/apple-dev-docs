# outputBuffers

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The specified output vertex data for the deformer function.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var outputBuffers: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<OutputBuffer>
```

## See Also

### Accessing deformation buffers
- [var inputBuffers: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<InputBuffer>](./inputbuffers.md)
  The specified input vertex data for the deformer function.
- [MeshDeformParameter.VertexBuffers](./vertexbuffers.md)
  The vertices requested by the developer when they defined their custom deformations. These will be passed into their custom deformation functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformparameter/outputbuffers)*