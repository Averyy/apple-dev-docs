# deform(parameter:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

deform the mesh on the CPU (may be useful for debugging), a no-op is allowed, default implementation is provided

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func deform(parameter: MeshDeformParameterCPU)
```

## See Also

- [func deform(parameter: MeshDeformParameterGPU, encoder: any MTLComputeCommandEncoder)](meshdeformer/deform(parameter:encoder:).md)
  deform the mesh on the GPU (the preferred method)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformer/deform(parameter:))*