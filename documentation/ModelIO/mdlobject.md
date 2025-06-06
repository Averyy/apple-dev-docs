# MDLObject

**Framework**: Model I/O  
**Kind**: class

The base class for objects that are part of a 3D asset, including meshes, cameras, and lights.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLObject
```

#### Overview

When you load content from an asset file using the [`MDLAsset`](mdlasset.md) class, Model I/O creates instances of the [`MDLObject`](mdlobject.md) subclasses [`MDLMesh`](mdlmesh.md), [`MDLCamera`](mdlcamera.md), and [`MDLLight`](mdllight.md). For asset formats that describe a collection of meshes, cameras, and lights organized in a hierarchy of spatial transforms, Model I/O also creates instances of the [`MDLObject`](mdlobject.md) class itself to describe the transform nodes that organize the asset’s visual content. Similarly, you use the [`MDLObject`](mdlobject.md) class and its subclasses when creating an object graph to be exported as an asset file using  the [`MDLAsset`](mdlasset.md) class.

##### Extending Model Io with Components

Model I/O allows you to customize the content and relationships in an object graph with . For each aspect of an object’s functionality, you use a component protocol (extending the [`MDLComponent`](mdlcomponent.md) protocol) to define functionality and a class adopting that protocol to implement it. Then, you can use the [`componentConforming(to:)`](mdlobject/componentconforming(to:).md) and [`setComponent(_:for:)`](mdlobject/setcomponent(_:for:).md) methods to associate those objects with any instance of the [`MDLObject`](mdlobject.md) class or of one of its subclasses. For example, you might define a protocol to add gameplay-related information such as scripting triggers to certain meshes, lights, or cameras in a scene.

Model I/O itself uses this mechanism to handle object hierarchies and spatial transforms: The methods listed in [`Working with Object Hierarchies`](mdlobject#Working-with-Object-Hierarchies.md) use the [`MDLObjectContainerComponent`](mdlobjectcontainercomponent.md) protocol to model hierarchic relationships between objects in an asset, and the methods listed in [`Working with Objects in Space`](mdlobject#Working-with-Objects-in-Space.md) use the [`MDLTransformComponent`](mdltransformcomponent.md) protocol to model coordinate space relationships. To add support for an asset file format or object graph that uses other ways to store or compute these relationships, you can use your own classes that adopt these protocols.

## Topics

### Customizing Objects with Components
- [func componentConforming(to: Protocol) -> (any MDLComponent)?](mdlobject/componentconforming(to:).md)
  Returns the object’s component for the specified protocol.
- [func setComponent(any MDLComponent, for: Protocol)](mdlobject/setcomponent(_:for:).md)
  Associates a component with the object for the specified protocol.
### Working with Object Hierarchies
- [var parent: MDLObject?](mdlobject/parent.md)
  The parent object that contains this object.
- [var children: any MDLObjectContainerComponent](mdlobject/children.md)
  A component that manages this object’s collection of children.
- [func addChild(MDLObject)](mdlobject/addchild(_:).md)
  Adds a child object to this object, creating a container for the object’s children if necessary.
- [func enumerateChildObjects(of: AnyClass, root: MDLObject, using: (MDLObject, UnsafeMutablePointer<ObjCBool>) -> Void, stopPointer: UnsafeMutablePointer<ObjCBool>)](mdlobject/enumeratechildobjects(of:root:using:stoppointer:).md)
  Executes the specified block using each object in this object’s child hierarchy.
- [var path: String](mdlobject/path.md)
  A path that identifies the object in an asset’s object hierarchy using object names.
- [func atPath(String) -> MDLObject](mdlobject/atpath(_:).md)
  Returns the child object at the specified path.
### Working with Objects in Space
- [func boundingBox(atTime: TimeInterval) -> MDLAxisAlignedBoundingBox](mdlobject/boundingbox(attime:).md)
  Returns the minimum region entirely enclosing the object’s contents at the specified time sample.
- [var transform: (any MDLTransformComponent)?](mdlobject/transform.md)
  A component that manages this object’s spatial transform and its changes over time.
### Managing Rendering Intent
- [var hidden: Bool](mdlobject/hidden.md)
  A Boolean value indicating whether this object should be used in rendering.
- [var instance: MDLObject?](mdlobject/instance.md)
  The primary object, if applicable, of which this object is an instance.
- [var path: String](mdlobject/path.md)
  A path that identifies the object in an asset’s object hierarchy using object names.
- [var components: [any MDLComponent]](mdlobject/components.md)
### Object Instancing
- [func atPath(String) -> MDLObject](mdlobject/atpath(_:).md)
  Returns the child object at the specified path.
- [func enumerateChildObjects(of: AnyClass, root: MDLObject, using: (MDLObject, UnsafeMutablePointer<ObjCBool>) -> Void, stopPointer: UnsafeMutablePointer<ObjCBool>)](mdlobject/enumeratechildobjects(of:root:using:stoppointer:).md)
  Executes the specified block using each object in this object’s child hierarchy.
- [subscript(Protocol) -> (any MDLComponent)?](mdlobject/subscript(_:).md)
### Constants
- [struct MDLAxisAlignedBoundingBox](mdlaxisalignedboundingbox.md)
  The minimal volume containing an object, used by the [`boundingBox(atTime:)`](mdlobject/boundingbox(attime:).md) method.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MDLCamera](mdlcamera.md)
- [MDLLight](mdllight.md)
- [MDLMesh](mdlmesh.md)
- [MDLPackedJointAnimation](mdlpackedjointanimation.md)
- [MDLSkeleton](mdlskeleton.md)
- [MDLVoxelArray](mdlvoxelarray.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLNamed](mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLAsset](mdlasset.md)
  An indexed container for 3D objects and associated information, such as transform hierarchies, meshes, cameras, and lights.
- [class MDLTransform](mdltransform.md)
  A description of the local coordinate space transformations for a 3D object.
- [class MDLMesh](mdlmesh.md)
  A container for vertex buffer data to be used in rendering a 3D object.
- [class MDLSubmesh](mdlsubmesh.md)
  A container for index buffer data and material information to be used in rendering all or part of a 3D object.
- [class MDLSubmeshTopology](mdlsubmeshtopology.md)
  A description of how a submesh’s index buffer data is arranged and how that arrangement should be used to produce the submesh’s intended 3D shape.
- [protocol MDLNamed](mdlnamed.md)
  The common interface for Model I/O objects that expose a human-readable name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobject)*