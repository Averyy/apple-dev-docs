# newObject()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates and returns a new object of the appropriate class.

**Availability**:
- macOS

## Declaration

```swift
func newObject() -> Any
```

```objc
- (id) newObject;
```

#### Return Value

A new object of the appropriate class. The returned object is implicitly retained, the sender is responsible for releasing it (with either release or autorelease).

#### Discussion

If an entity name is set (see [`entityName`](./entityname.md)), the object created is an instance of the class specified for that entity (and the object is inserted into the receiver’s managed object context). Otherwise the object created is an instance of the class returned by [`objectClass`](./objectclass.md).

This method is called when adding and inserting objects if [`automaticallyPreparesContent`](./automaticallypreparescontent.md) is [`true`](../../Swift/true.md).

The default implementation assumes the class returned by [`objectClass`](./objectclass.md) has a standard  `init` method without arguments. If the object class being controlled is `NSManagedObject` (or a subclass thereof) its designated initializer ([`init(entity:insertInto:)`](../../CoreData/nsmanagedobject/init%28entity,insertinto%29.md)) is called instead, using the entity and managed object context specified for the receiver.

## See Also

### Related Documentation
- [var objectClass: AnyClass!](./objectclass.md)
  The object class to use when creating new objects.
- [var entityName: String?](./entityname.md)
  The entity name used by the receiver to create new objects.
### Managing objects
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
- [var canRemove: Bool](./canremove.md)
  A Boolean value that indicates whether an object can be removed from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/newobject())*