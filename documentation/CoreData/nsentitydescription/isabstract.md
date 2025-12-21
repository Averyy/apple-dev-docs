# isAbstract

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether the receiver represents an abstract entity.

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
var isAbstract: Bool { get set }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver represents an abstract entity, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver represents an abstract entity, otherwise [`false`](https://developer.apple.com/documentation/Swift/false). An abstract entity might be Shape, with concrete sub-entities such as Rectangle, Triangle, and Circle.

##### Special Considerations

Setting whether an entity is abstract raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

- [var name: String?](nsentitydescription/name.md)
  The entity name of the receiver.
- [var managedObjectModel: NSManagedObjectModel](nsentitydescription/managedobjectmodel.md)
  The managed object model with which the receiver is associated.
- [var managedObjectClassName: String!](nsentitydescription/managedobjectclassname.md)
  The name of the class that represents the receiver’s entity.
- [var renamingIdentifier: String?](nsentitydescription/renamingidentifier.md)
  The renaming identifier for the receiver.
- [var userInfo: [AnyHashable : Any]?](nsentitydescription/userinfo.md)
  The user info dictionary of the receiver.
- [var coreSpotlightDisplayNameExpression: NSExpression](nsentitydescription/corespotlightdisplaynameexpression.md)
  The expression that computes the CoreSpotlight display name for instances of the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/isabstract)*