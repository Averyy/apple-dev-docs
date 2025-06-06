# MeshResource.Model

**Framework**: RealityKit  
**Kind**: struct

A model consists of a list of parts.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct Model
```

## Topics

### Initializers
- [init(id: String, descriptors: [MeshDescriptor]) throws](meshresource/model/init(id:descriptors:).md)
- [init(id: String, parts: [MeshResource.Part])](meshresource/model/init(id:parts:).md)
### Instance Properties
- [var id: String](meshresource/model/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [var parts: MeshPartCollection](meshresource/model/parts.md)
  Table of parts composing this mesh.
### Type Aliases
- [MeshResource.Model.ID](meshresource/model/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [MeshResource.Contents](meshresource/contents-swift.struct.md)
  Value of the contents of the resource.
- [MeshResource.Instance](meshresource/instance.md)
  An object that transforms a model to a location.
- [MeshResource.Part](meshresource/part.md)
  A part of a model consisting of a single material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/model)*