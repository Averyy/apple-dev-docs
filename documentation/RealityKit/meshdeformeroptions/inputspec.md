# inputSpec

**Framework**: RealityKit  
**Kind**: property

The expected vertex buffer input spec for the deformer type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let inputSpec: MeshDeformerVertexOptions
```

#### Discussion

This is used to determine dependencies lower in the deformation stack that may re-trigger this deformation.

## See Also

- [let outputSpec: MeshDeformerVertexOptions](meshdeformeroptions/outputspec.md)
  The expected vertex buffer output spec for the deformer type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformeroptions/inputspec)*