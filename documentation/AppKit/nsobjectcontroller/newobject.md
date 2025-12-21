# newObject()

**Framework**: AppKit  
**Kind**: method

Creates and returns a new object of the appropriate class.

**Availability**:
- macOS ?+

## Declaration

```swift
func newObject() -> Any
```

#### Return Value

A new object of the appropriate class. The returned object is implicitly retained, the sender is responsible for releasing it (with either release or autorelease).

#### Discussion

If an entity name is set (see [`entityName`](nsobjectcontroller/entityname.md)), the object created is an instance of the class specified for that entity (and the object is inserted into the receiver’s managed object context). Otherwise the object created is an instance of the class returned by [`objectClass`](nsobjectcontroller/objectclass.md).

This method is called when adding and inserting objects if [`automaticallyPreparesContent`](nsobjectcontroller/automaticallypreparescontent.md) is [`true`](https://developer.apple.com/documentation/Swift/true).

The default implementation assumes the class returned by [`objectClass`](nsobjectcontroller/objectclass.md) has a standard  `init` method without arguments. If the object class being controlled is `NSManagedObject` (or a subclass thereof) its designated initializer ([`init(entity:insertInto:)`](https://developer.apple.com/documentation/CoreData/NSManagedObject/init(entity:insertInto:))) is called instead, using the entity and managed object context specified for the receiver.

## See Also

- [var objectClass: AnyClass!](nsobjectcontroller/objectclass.md)
  The object class to use when creating new objects.
- [var entityName: String?](nsobjectcontroller/entityname.md)
  The entity name used by the receiver to create new objects.
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
- [var canRemove: Bool](nsobjectcontroller/canremove.md)
  A Boolean value that indicates whether an object can be removed from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/newobject())*