# add(_:)

**Framework**: AppKit  
**Kind**: method

Creates a new object and sets it as the receiver’s content object.

**Availability**:
- macOS ?+

## Declaration

```swift
@IBAction
@MainActor func add(_ sender: Any?)
```

#### Discussion

Creates a new object of the appropriate entity (specified by [`entityName`](nsobjectcontroller/entityname.md)) or class (specified by [`objectClass`](nsobjectcontroller/objectclass.md))—see [`newObject()`](nsobjectcontroller/newobject().md)—and sets it as the receiver’s content object using [`addObject(_:)`](nsobjectcontroller/addobject(_:).md).

##### Special Considerations

Beginning with OS X v10.4 the result of this method is deferred until the next iteration of the runloop so that the error presentation mechanism can provide feedback as a sheet.

## Parameters

- `sender`: Typically the object that invoked this method.

## See Also

- [func newObject() -> Any](nsobjectcontroller/newobject.md)
  Creates and returns a new object of the appropriate class.
- [func addObject(Any)](nsobjectcontroller/addobject(_:).md)
  Sets the receiver’s content object.
- [func removeObject(Any)](nsobjectcontroller/removeobject(_:).md)
  Removes a given object from the receiver’s content.
- [var canAdd: Bool](nsobjectcontroller/canadd.md)
  A Boolean value that indicates whether an object can be added to the receiver using [`add(_:)`](nsobjectcontroller/add(_:).md).
- [func remove(Any?)](nsobjectcontroller/remove(_:).md)
  Removes the receiver’s content object.
- [var canRemove: Bool](nsobjectcontroller/canremove.md)
  A Boolean value that indicates whether an object can be removed from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/add(_:))*