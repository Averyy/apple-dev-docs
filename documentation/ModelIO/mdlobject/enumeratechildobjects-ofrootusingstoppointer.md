# enumerateChildObjects(of:root:using:stopPointer:)

**Framework**: Model I/O  
**Kind**: method

Executes the specified block using each object in this object’s child hierarchy.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func enumerateChildObjects(of objectClass: AnyClass, root: MDLObject, using block: @escaping (MDLObject, UnsafeMutablePointer<ObjCBool>) -> Void, stopPointer: UnsafeMutablePointer<ObjCBool>)
```

## Parameters

- `objectClass`: A Model I/O class representing a type of child objects to evaluate. For example, pass the   class to evaluate all 3D objects stored in the asset. Pass the   class to evaluate all child objects regardless of type.
- `root`: The root object at which to begin traversing the child object hierarchy.
- `block`: The block to apply to child objects. This block takes two parameters: the   to be evaluated by the block, and a   pointer that you can set to   to stop further evaluation of the object hierarchy.
- `stopPointer`: Set this pointer’s value to   during enumeration to stop further enumeration of the object hierarchy.

## See Also

- [var parent: MDLObject?](mdlobject/parent.md)
  The parent object that contains this object.
- [var children: any MDLObjectContainerComponent](mdlobject/children.md)
  A component that manages this object’s collection of children.
- [func addChild(MDLObject)](mdlobject/addchild(_:).md)
  Adds a child object to this object, creating a container for the object’s children if necessary.
- [var path: String](mdlobject/path.md)
  A path that identifies the object in an asset’s object hierarchy using object names.
- [func atPath(String) -> MDLObject](mdlobject/atpath(_:).md)
  Returns the child object at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobject/enumeratechildobjects(of:root:using:stoppointer:))*