# canRemove

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether an object can be removed from the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
var canRemove: Bool { get }
```

#### Discussion

Bindings can use this method to control the enabling of user interface objects.

This property is observable using key-value observing.

## See Also

- [func newObject() -> Any](nsobjectcontroller/newobject.md)
  Creates and returns a new object of the appropriate class.
- [func addObject(Any)](nsobjectcontroller/addobject(_:).md)
  Sets the receiver’s content object.
- [func removeObject(Any)](nsobjectcontroller/removeobject(_:).md)
  Removes a given object from the receiver’s content.
- [func add(Any?)](nsobjectcontroller/add(_:).md)
  Creates a new object and sets it as the receiver’s content object.
- [var canAdd: Bool](nsobjectcontroller/canadd.md)
  A Boolean value that indicates whether an object can be added to the receiver using [`add(_:)`](nsobjectcontroller/add(_:).md).
- [func remove(Any?)](nsobjectcontroller/remove(_:).md)
  Removes the receiver’s content object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/canremove)*