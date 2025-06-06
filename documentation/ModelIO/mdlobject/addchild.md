# addChild(_:)

**Framework**: Model I/O  
**Kind**: method

Adds a child object to this object, creating a container for the object’s children if necessary.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addChild(_ child: MDLObject)
```

#### Discussion

Many asset formats describe a hierarchy of transforms that model the spatial relationships between meshes, lights, and cameras in the asset. In such formats, hierarchic transforms are [`MDLObject`](mdlobject.md) instances whose [`children`](mdlobject/children.md) property references the objects affected by the transform—and those objects can be other [`MDLObject`](mdlobject.md) instances with children of their own.

If the object’s [`children`](mdlobject/children.md) property is `nil`, this method sets that property to a new [`MDLObjectContainer`](mdlobjectcontainer.md) instance before adding the child object.

## Parameters

- `child`: The child object to add.

## See Also

- [var parent: MDLObject?](mdlobject/parent.md)
  The parent object that contains this object.
- [var children: any MDLObjectContainerComponent](mdlobject/children.md)
  A component that manages this object’s collection of children.
- [func enumerateChildObjects(of: AnyClass, root: MDLObject, using: (MDLObject, UnsafeMutablePointer<ObjCBool>) -> Void, stopPointer: UnsafeMutablePointer<ObjCBool>)](mdlobject/enumeratechildobjects(of:root:using:stoppointer:).md)
  Executes the specified block using each object in this object’s child hierarchy.
- [var path: String](mdlobject/path.md)
  A path that identifies the object in an asset’s object hierarchy using object names.
- [func atPath(String) -> MDLObject](mdlobject/atpath(_:).md)
  Returns the child object at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobject/addchild(_:))*