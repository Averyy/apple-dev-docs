# atPath(_:)

**Framework**: Model I/O  
**Kind**: method

Returns the child object at the specified path.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func atPath(_ path: String) -> MDLObject
```

#### Return Value

The requested object, or `nil` if no object matching the path can be found.

#### Discussion

See the [`path`](mdlobject/path.md) property for examples of how to construct object paths for searching.

## Parameters

- `path`: A path that identifies the object to be found using object names.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobject/atpath(_:))*