# name

**Framework**: Core Data  
**Kind**: property

The entity name of the receiver.

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
var name: String? { get set }
```

#### Discussion

Setting the name raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

- [Core Data Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [var managedObjectModel: NSManagedObjectModel](nsentitydescription/managedobjectmodel.md)
  The managed object model with which the receiver is associated.
- [var managedObjectClassName: String!](nsentitydescription/managedobjectclassname.md)
  The name of the class that represents the receiver’s entity.
- [var renamingIdentifier: String?](nsentitydescription/renamingidentifier.md)
  The renaming identifier for the receiver.
- [var isAbstract: Bool](nsentitydescription/isabstract.md)
  A Boolean value that indicates whether the receiver represents an abstract entity.
- [var userInfo: [AnyHashable : Any]?](nsentitydescription/userinfo.md)
  The user info dictionary of the receiver.
- [var coreSpotlightDisplayNameExpression: NSExpression](nsentitydescription/corespotlightdisplaynameexpression.md)
  The expression that computes the CoreSpotlight display name for instances of the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/name)*