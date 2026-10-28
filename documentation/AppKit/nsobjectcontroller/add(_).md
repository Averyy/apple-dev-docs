# add(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a new object and sets it as the receiver’s content object.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func add(_ sender: Any?)
```

```objc
- (void) add:(id) sender;
```

## Discussion

Creates a new object of the appropriate entity (specified by [`entityName`](./entityname.md)) or class (specified by [`objectClass`](./objectclass.md))—see [`newObject()`](./newobject%28%29.md)—and sets it as the receiver’s content object using [`addObject(_:)`](./addobject%28_%29.md).

### Special Considerations

Beginning with OS X v10.4 the result of this method is deferred until the next iteration of the runloop so that the error presentation mechanism can provide feedback as a sheet.

## Parameters

- `sender`: Typically the object that invoked this method.

## See Also

### Managing objects
- [func newObject() -> Any](./newobject%28%29.md)
  Creates and returns a new object of the appropriate class.
- [func addObject(Any)](./addobject%28_%29.md)
  Sets the receiver’s content object.
- [func removeObject(Any)](./removeobject%28_%29.md)
  Removes a given object from the receiver’s content.
- [var canAdd: Bool](./canadd.md)
  A Boolean value that indicates whether an object can be added to the receiver using [`add(_:)`](./add%28_%29.md).
- [func remove(Any?)](./remove%28_%29.md)
  Removes the receiver’s content object.
- [var canRemove: Bool](./canremove.md)
  A Boolean value that indicates whether an object can be removed from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/add(_:))*