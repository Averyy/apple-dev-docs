# MeshResource.Model

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A model consists of a list of parts.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct Model
```

## Topics

### Initializers
- [init(id: String, descriptors: [MeshDescriptor]) throws](./model/init%28id,descriptors%29.md)
- [init(id: String, parts: [MeshResource.Part])](./model/init%28id,parts%29.md)
### Instance Properties
- [var parts: MeshPartCollection](./model/parts.md)
  Table of parts composing this mesh.

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)

## See Also

### Mesh resource data
- [MeshResource.Contents](./contents-swift.struct.md)
  Value of the contents of the resource.
- [MeshResource.Instance](./instance.md)
  An object that transforms a model to a location.
- [MeshResource.Part](./part.md)
  A part of a model consisting of a single material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/model)*