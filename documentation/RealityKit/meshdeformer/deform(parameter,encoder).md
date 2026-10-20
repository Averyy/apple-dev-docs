# deform(parameter:encoder:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

deform the mesh on the GPU (the preferred method)

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func deform(parameter: MeshDeformParameterGPU, encoder: any MTLComputeCommandEncoder)
```

## See Also

- [func deform(parameter: MeshDeformParameterCPU)](meshdeformer/deform(parameter:).md)
  deform the mesh on the CPU (may be useful for debugging), a no-op is allowed, default implementation is provided


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformer/deform(parameter:encoder:))*