# canRemove

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether an object can be removed from the receiver.

**Availability**:
- macOS

## Declaration

```swift
var canRemove: Bool { get }
```

```objc
@property (readonly) BOOL canRemove;
```

#### Discussion

Bindings can use this method to control the enabling of user interface objects.

This property is observable using key-value observing.

## See Also

### Managing objects
- [func newObject() -> Any](./newobject%28%29.md)
  Creates and returns a new object of the appropriate class.
- [func addObject(Any)](./addobject%28_%29.md)
  Sets the receiver’s content object.
- [func removeObject(Any)](./removeobject%28_%29.md)
  Removes a given object from the receiver’s content.
- [func add(Any?)](./add%28_%29.md)
  Creates a new object and sets it as the receiver’s content object.
- [var canAdd: Bool](./canadd.md)
  A Boolean value that indicates whether an object can be added to the receiver using [`add(_:)`](./add%28_%29.md).
- [func remove(Any?)](./remove%28_%29.md)
  Removes the receiver’s content object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/canremove)*