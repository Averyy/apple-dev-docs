# MDLObjectContainer

**Framework**: Model I/O  
**Kind**: class

A default implementation for handling object hierarchy relationships in a 3D asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLObjectContainer
```

#### Overview

Model I/O uses the [`MDLObjectContainerComponent`](mdlobjectcontainercomponent.md) protocol to create object hierarchy relationships for meshes, lights, cameras, and containers loaded from a [`MDLAsset`](mdlasset.md) instance. To create your own containers—for example, to reference in-memory representations, offline databases, or custom asset file formats—create [`MDLObjectContainer`](mdlobjectcontainer.md) subclasses and add them to a [`MDLObject`](mdlobject.md) instance using its [`setComponent(_:for:)`](mdlobject/setcomponent(_:for:).md) method.

All methods of this class are defined by the [`MDLObjectContainerComponent`](mdlobjectcontainercomponent.md) protocol. For discussion of these methods, see [`MDLObjectContainerComponent`](mdlobjectcontainercomponent.md).

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [MDLComponent](mdlcomponent.md)
- [MDLObjectContainerComponent](mdlobjectcontainercomponent.md)
- [NSFastEnumeration](../foundation/nsfastenumeration.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [protocol MDLComponent](mdlcomponent.md)
  The base protocol for extensible file format support in Model I/O.
- [protocol MDLObjectContainerComponent](mdlobjectcontainercomponent.md)
  The general interface for classes that can act as containers in an object hierarchy.
- [protocol MDLTransformComponent](mdltransformcomponent.md)
  The general interface for classes that manage local coordinate space transforms for 3D objects


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobjectcontainer)*