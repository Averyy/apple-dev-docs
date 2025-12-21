# MeshResource.Instance

**Framework**: RealityKit  
**Kind**: struct

An object that transforms a model to a location.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct Instance
```

## Topics

### Initializers
- [init(id: String, model: String, at: simd_float4x4?)](meshresource/instance/init(id:model:at:).md)
### Instance Properties
- [var model: String](meshresource/instance/model.md)
  Name of the model to instance.
- [var transform: simd_float4x4](meshresource/instance/transform.md)
  Transform for the instance.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [MeshResource.Contents](meshresource/contents-swift.struct.md)
  Value of the contents of the resource.
- [MeshResource.Model](meshresource/model.md)
  A model consists of a list of parts.
- [MeshResource.Part](meshresource/part.md)
  A part of a model consisting of a single material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/instance)*