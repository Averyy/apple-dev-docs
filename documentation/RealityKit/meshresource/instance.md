# MeshResource.Instance

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that transforms a model to a location.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct Instance
```

## Topics

### Initializers
- [init(id: String, model: String, at: simd_float4x4?)](./instance/init%28id,model,at%29.md)
### Instance Properties
- [var model: String](./instance/model.md)
  Name of the model to instance.
- [var transform: simd_float4x4](./instance/transform.md)
  Transform for the instance.

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)

## See Also

### Mesh resource data
- [MeshResource.Contents](./contents-swift.struct.md)
  Value of the contents of the resource.
- [MeshResource.Model](./model.md)
  A model consists of a list of parts.
- [MeshResource.Part](./part.md)
  A part of a model consisting of a single material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/instance)*