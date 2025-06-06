# removeObject(_:)

**Framework**: AppKit  
**Kind**: method

Removes a given object from the receiver’s content.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeObject(_ object: Any)
```

#### Discussion

If `object` is the receiver’s content object, the receiver’s content is set to `nil`. If the receiver’s content is bound to another (primary) object or controller through a relationship key, the relationship of the primary object is cleared.

## Parameters

- `object`: The object to remove from the receiver.

## See Also

- [func newObject() -> Any](nsobjectcontroller/newobject.md)
  Creates and returns a new object of the appropriate class.
- [func addObject(Any)](nsobjectcontroller/addobject(_:).md)
  Sets the receiver’s content object.
- [func add(Any?)](nsobjectcontroller/add(_:).md)
  Creates a new object and sets it as the receiver’s content object.
- [var canAdd: Bool](nsobjectcontroller/canadd.md)
  A Boolean value that indicates whether an object can be added to the receiver using [`add(_:)`](nsobjectcontroller/add(_:).md).
- [func remove(Any?)](nsobjectcontroller/remove(_:).md)
  Removes the receiver’s content object.
- [var canRemove: Bool](nsobjectcontroller/canremove.md)
  A Boolean value that indicates whether an object can be removed from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/removeobject(_:))*