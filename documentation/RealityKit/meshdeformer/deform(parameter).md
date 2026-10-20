# deform(parameter:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

deform the mesh on the CPU (may be useful for debugging), a no-op is allowed, default implementation is provided

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func deform(parameter: MeshDeformParameterCPU)
```

## Default Implementations

### MeshDeformer Implementations
- [func deform(parameter: MeshDeformParameterCPU)](./deform%28parameter%29-32cx7.md)
  default, no-op implementaiton for `cpu` version of `deform` as its primary intention is to aid debugging

## See Also

### Deforming the mesh
- [func deform(parameter: MeshDeformParameterGPU, encoder: any MTLComputeCommandEncoder)](./deform%28parameter,encoder%29.md)
  deform the mesh on the GPU (the preferred method)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformer/deform(parameter:))*