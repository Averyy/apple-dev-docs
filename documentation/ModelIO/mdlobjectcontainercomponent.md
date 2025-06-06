# MDLObjectContainerComponent

**Framework**: Model I/O  
**Kind**: protocol

The general interface for classes that can act as containers in an object hierarchy.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol MDLObjectContainerComponent : NSFastEnumeration, MDLComponent
```

#### Overview

Model I/O uses this interface to represent content loaded from an asset file. Various asset file formats define collections of information to describe their contents, such as a hierarchy of transforms to model the spatial relationships between models, lights, and meshes contained in an asset. When Model I/O imports such asset formats, the contents of the asset are objects implementing this protocol. You can also adopt this protocol in your own classes to describe your own custom asset formats—for example, one that includes collections of scripts and their triggers associated with the objects in a scene.

## Topics

### Working with Child Objects
- [var objects: [MDLObject]](mdlobjectcontainercomponent/objects.md)
  This object’s array of child objects.
- [func add(MDLObject)](mdlobjectcontainercomponent/add(_:).md)
  Adds the specified object as a child of this object.
- [func remove(MDLObject)](mdlobjectcontainercomponent/remove(_:).md)
  Removes the specified object from this object’s array of children.
### Instance Properties
- [var count: Int](mdlobjectcontainercomponent/count.md)
### Subscripts
- [subscript(Int) -> MDLObject](mdlobjectcontainercomponent/subscript(_:).md)

## Relationships

### Inherits From
- [MDLComponent](mdlcomponent.md)
- [NSFastEnumeration](../Foundation/NSFastEnumeration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [MDLObjectContainer](mdlobjectcontainer.md)

## See Also

- [protocol MDLComponent](mdlcomponent.md)
  The base protocol for extensible file format support in Model I/O.
- [class MDLObjectContainer](mdlobjectcontainer.md)
  A default implementation for handling object hierarchy relationships in a 3D asset.
- [protocol MDLTransformComponent](mdltransformcomponent.md)
  The general interface for classes that manage local coordinate space transforms for 3D objects


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobjectcontainercomponent)*