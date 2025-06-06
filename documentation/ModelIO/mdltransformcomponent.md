# MDLTransformComponent

**Framework**: Model I/O  
**Kind**: protocol

The general interface for classes that manage local coordinate space transforms for 3D objects

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol MDLTransformComponent : MDLComponent
```

#### Overview

Transform information—that is, the combination of an object’s position, orientation, shear, and scale—can be static, or in the case of resources that describe animations, time-based. By default, the [`MDLTransform`](mdltransform.md) class manages transform information for objects loaded from a [`MDLAsset`](mdlasset.md) instance. By providing your own class that adopts this protocol, you can support other ways to associate transform information with objects—for example, when defining a custom asset file format.

## Topics

### Working with Static Transforms
- [var matrix: matrix_float4x4](mdltransformcomponent/matrix.md)
  The transform matrix that defines the local coordinate space relative to a parent coordinate space.
- [func setLocalTransform(matrix_float4x4)](mdltransformcomponent/setlocaltransform(_:).md)
  Sets a new static transform matrix, overriding any time-based transform information.
### Working with Animated Transforms
- [var minimumTime: TimeInterval](mdltransformcomponent/minimumtime.md)
  The timestamp for the first timed data sample in the transform component.
- [var maximumTime: TimeInterval](mdltransformcomponent/maximumtime.md)
  The timestamp for the last timed data sample in the transform component.
- [func localTransform(atTime: TimeInterval) -> matrix_float4x4](mdltransformcomponent/localtransform(attime:).md)
  Returns the local transform matrix as of the specified time sample.
- [func setLocalTransform(matrix_float4x4, forTime: TimeInterval)](mdltransformcomponent/setlocaltransform(_:fortime:).md)
  Sets a new local transform matrix for the specified time sample.
### Deriving a Global Transformation
- [static func globalTransform(with: MDLObject, atTime: TimeInterval) -> matrix_float4x4](mdltransformcomponent/globaltransform(with:attime:).md)
  Returns the absolute coordinate transformation for an object in a transform hierarchy.
### Instance Properties
- [var keyTimes: [NSNumber]](mdltransformcomponent/keytimes.md)
- [var resetsTransform: Bool](mdltransformcomponent/resetstransform.md)

## Relationships

### Inherits From
- [MDLComponent](mdlcomponent.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [MDLTransform](mdltransform.md)
- [MDLTransformStack](mdltransformstack.md)

## See Also

- [protocol MDLComponent](mdlcomponent.md)
  The base protocol for extensible file format support in Model I/O.
- [class MDLObjectContainer](mdlobjectcontainer.md)
  A default implementation for handling object hierarchy relationships in a 3D asset.
- [protocol MDLObjectContainerComponent](mdlobjectcontainercomponent.md)
  The general interface for classes that can act as containers in an object hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransformcomponent)*