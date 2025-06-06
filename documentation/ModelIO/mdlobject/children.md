# children

**Framework**: Modelio  
**Kind**: property

A component that manages this object’s collection of children.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var children: any MDLObjectContainerComponent { get set }
```

#### Discussion

Many asset formats describe a hierarchy of transforms that model the spatial relationships between meshes, lights, and cameras in the asset. In such formats, hierarchic transforms are [`MDLObject`](mdlobject.md) instances whose [`children`](mdlobject/children.md) property references the objects affected by the transform, and those objects can be other [`MDLObject`](mdlobject.md) instances with children of their own.

This property’s value is a component object—either a [`MDLObjectContainer`](mdlobjectcontainer.md) instance, or a custom class that adopts the [`MDLObjectContainerComponent`](mdlobjectcontainercomponent.md) protocol. By default, an object has no container component (that is, this property’s value is `nil`). To add a container component, either write to this property an instance of a container component class or call the [`addChild(_:)`](mdlobject/addchild(_:).md) method to create a default [`MDLObjectContainer`](mdlobjectcontainer.md) instance and add a child object to that container.

> **Note**:  Reading or writing this property is equivalent to calling the [`componentConforming(to:)`](mdlobject/componentconforming(to:).md) or [`setComponent(_:for:)`](mdlobject/setcomponent(_:for:).md) method with the [`MDLObjectContainerComponent`](mdlobjectcontainercomponent.md) protocol.

Container components support fast enumeration and subscripting, so you can treat an object’s children property similarly to an array.

## See Also

- [var parent: MDLObject?](mdlobject/parent.md)
  The parent object that contains this object.
- [func addChild(MDLObject)](mdlobject/addchild(_:).md)
  Adds a child object to this object, creating a container for the object’s children if necessary.
- [func enumerateChildObjects(of: AnyClass, root: MDLObject, using: (MDLObject, UnsafeMutablePointer<ObjCBool>) -> Void, stopPointer: UnsafeMutablePointer<ObjCBool>)](mdlobject/enumeratechildobjects(of:root:using:stoppointer:).md)
  Executes the specified block using each object in this object’s child hierarchy.
- [var path: String](mdlobject/path.md)
  A path that identifies the object in an asset’s object hierarchy using object names.
- [func atPath(String) -> MDLObject](mdlobject/atpath(_:).md)
  Returns the child object at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ModelIO/mdlobject/children)*