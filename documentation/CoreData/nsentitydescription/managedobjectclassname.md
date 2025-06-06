# managedObjectClassName

**Framework**: Core Data  
**Kind**: property

The name of the class that represents the receiver’s entity.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var managedObjectClassName: String! { get set }
```

#### Discussion

The class specified by `name` must [`NSManagedObject`](nsmanagedobject.md) or a subclass of [`NSManagedObject`](nsmanagedobject.md).

##### Special Considerations

Setting the class name raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

- [var name: String?](nsentitydescription/name.md)
  The entity name of the receiver.
- [var managedObjectModel: NSManagedObjectModel](nsentitydescription/managedobjectmodel.md)
  The managed object model with which the receiver is associated.
- [var renamingIdentifier: String?](nsentitydescription/renamingidentifier.md)
  The renaming identifier for the receiver.
- [var isAbstract: Bool](nsentitydescription/isabstract.md)
  A Boolean value that indicates whether the receiver represents an abstract entity.
- [var userInfo: [AnyHashable : Any]?](nsentitydescription/userinfo.md)
  The user info dictionary of the receiver.
- [var coreSpotlightDisplayNameExpression: NSExpression](nsentitydescription/corespotlightdisplaynameexpression.md)
  The expression that computes the CoreSpotlight display name for instances of the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/managedobjectclassname)*