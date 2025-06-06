# addObject(_:)

**Framework**: AppKit  
**Kind**: method

Sets the receiver’s content object.

**Availability**:
- macOS ?+

## Declaration

```swift
func addObject(_ object: Any)
```

#### Discussion

If the receiver’s content is bound to another (primary) object or controller through a relationship key, the relationship of the primary object is changed. In a tree-like structure, the object is added after the current selection at the same depth. If there is no selection, the object is appended to the child nodes of the tree’s arranged objects.

## Parameters

- `object`: The content object for the receiver.

## See Also

- [func newObject() -> Any](nsobjectcontroller/newobject.md)
  Creates and returns a new object of the appropriate class.
- [func removeObject(Any)](nsobjectcontroller/removeobject(_:).md)
  Removes a given object from the receiver’s content.
- [func add(Any?)](nsobjectcontroller/add(_:).md)
  Creates a new object and sets it as the receiver’s content object.
- [var canAdd: Bool](nsobjectcontroller/canadd.md)
  A Boolean value that indicates whether an object can be added to the receiver using [`add(_:)`](nsobjectcontroller/add(_:).md).
- [func remove(Any?)](nsobjectcontroller/remove(_:).md)
  Removes the receiver’s content object.
- [var canRemove: Bool](nsobjectcontroller/canremove.md)
  A Boolean value that indicates whether an object can be removed from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/addobject(_:))*