# MDLTransform

**Framework**: Model I/O  
**Kind**: class

A description of the local coordinate space transformations for a 3D object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLTransform
```

#### Overview

Transform information can be static, or in the case of resources that describe animations, time based. You use transform objects to position, orient, shear, and scale the meshes, cameras, lights, and container objects in an asset using their [`transform`](mdlobject/transform.md) property.

## Topics

### Creating a Transform Object
- [convenience init(identity: ())](mdltransform/init(identity:).md)
  Initializes a transform object to the identity transformation.
- [convenience init(matrix: matrix_float4x4)](mdltransform/init(matrix:).md)
  Initializes a transform object with the specified transform matrix.
- [convenience init(transformComponent: any MDLTransformComponent)](mdltransform/init(transformcomponent:).md)
  Initializes a transform object to match the specified transform component.
- [convenience init(matrix: matrix_float4x4, resetsTransform: Bool)](mdltransform/init(matrix:resetstransform:).md)
- [convenience init(transformComponent: any MDLTransformComponent, resetsTransform: Bool)](mdltransform/init(transformcomponent:resetstransform:).md)
### Using Factors of a Static Transform
- [var translation: vector_float3](mdltransform/translation.md)
  The x-, y-, and z-axis offsets of the transform relative to its parent coordinate space.
- [var rotation: vector_float3](mdltransform/rotation.md)
  The orientation, as a vector of Euler angles in radians, of the transform relative to its parent coordinate space.
- [var scale: vector_float3](mdltransform/scale.md)
  The x-, y-, and z-axis scale factors of the transform relative to its parent coordinate space.
- [var shear: vector_float3](mdltransform/shear.md)
  The x-, y-, and z-axis shear factors of the transform relative to its parent coordinate space.
- [func setIdentity()](mdltransform/setidentity.md)
  Sets all factors of the transform to those of the identity transformation.
### Using Factors of an Animated Transform
- [func translation(atTime: TimeInterval) -> vector_float3](mdltransform/translation(attime:).md)
  Returns the x-, y-, and z-axis offsets of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setTranslation(vector_float3, forTime: TimeInterval)](mdltransform/settranslation(_:fortime:).md)
  Sets the x-, y-, and z-axis offsets of the transform for the specified time sample.
- [func rotation(atTime: TimeInterval) -> vector_float3](mdltransform/rotation(attime:).md)
  Returns the orientation of the transform relative to its parent coordinate space, as of the specified time sample.
- [func rotationMatrix(atTime: TimeInterval) -> matrix_float4x4](mdltransform/rotationmatrix(attime:).md)
  Returns the orientation of the transform as a rotation matrix, as of the specified time sample.
- [func setRotation(vector_float3, forTime: TimeInterval)](mdltransform/setrotation(_:fortime:).md)
  Sets the orientation of the transform for the specified time sample.
- [func scale(atTime: TimeInterval) -> vector_float3](mdltransform/scale(attime:).md)
  Returns the x-, y-, and z-axis scale factors of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setScale(vector_float3, forTime: TimeInterval)](mdltransform/setscale(_:fortime:).md)
  Sets the x-, y-, and z-axis scale factors of the transform for the specified time sample.
- [func shear(atTime: TimeInterval) -> vector_float3](mdltransform/shear(attime:).md)
  Returns the x-, y-, and z-axis shear factors of the transform relative to its parent coordinate space, as of the specified time sample.
- [func setShear(vector_float3, forTime: TimeInterval)](mdltransform/setshear(_:fortime:).md)
  Sets the x-, y-, and z-axis shear factors of the transform for the specified time sample.
- [func setMatrix(matrix_float4x4, forTime: TimeInterval)](mdltransform/setmatrix(_:fortime:).md)
### Initializers
- [init()](mdltransform/init.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLComponent](mdlcomponent.md)
- [MDLTransformComponent](mdltransformcomponent.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLAsset](mdlasset.md)
  An indexed container for 3D objects and associated information, such as transform hierarchies, meshes, cameras, and lights.
- [class MDLObject](mdlobject.md)
  The base class for objects that are part of a 3D asset, including meshes, cameras, and lights.
- [class MDLMesh](mdlmesh.md)
  A container for vertex buffer data to be used in rendering a 3D object.
- [class MDLSubmesh](mdlsubmesh.md)
  A container for index buffer data and material information to be used in rendering all or part of a 3D object.
- [class MDLSubmeshTopology](mdlsubmeshtopology.md)
  A description of how a submesh’s index buffer data is arranged and how that arrangement should be used to produce the submesh’s intended 3D shape.
- [protocol MDLNamed](mdlnamed.md)
  The common interface for Model I/O objects that expose a human-readable name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransform)*