# removeObject(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes a given object from the receiver’s content.

**Availability**:
- macOS

## Declaration

```swift
func removeObject(_ object: Any)
```

```objc
- (void) removeObject:(id) object;
```

#### Discussion

If `object` is the receiver’s content object, the receiver’s content is set to `nil`. If the receiver’s content is bound to another (primary) object or controller through a relationship key, the relationship of the primary object is cleared.

## Parameters

- `object`: The object to remove from the receiver.

## See Also

### Managing objects
- [func newObject() -> Any](./newobject%28%29.md)
  Creates and returns a new object of the appropriate class.
- [func addObject(Any)](./addobject%28_%29.md)
  Sets the receiver’s content object.
- [func add(Any?)](./add%28_%29.md)
  Creates a new object and sets it as the receiver’s content object.
- [var canAdd: Bool](./canadd.md)
  A Boolean value that indicates whether an object can be added to the receiver using [`add(_:)`](./add%28_%29.md).
- [func remove(Any?)](./remove%28_%29.md)
  Removes the receiver’s content object.
- [var canRemove: Bool](./canremove.md)
  A Boolean value that indicates whether an object can be removed from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/removeobject(_:))*