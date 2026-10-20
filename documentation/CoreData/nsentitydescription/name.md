# name

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The entity name of the receiver.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String? { get set }
```

```objc
@property (copy, nullable) NSString * name;
```

#### Discussion

Setting the name raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Related Documentation
- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
### Getting descriptive information
- [var managedObjectModel: NSManagedObjectModel](./managedobjectmodel.md)
  The managed object model with which the receiver is associated.
- [var managedObjectClassName: String!](./managedobjectclassname.md)
  The name of the class that represents the receiver’s entity.
- [var renamingIdentifier: String?](./renamingidentifier.md)
  The renaming identifier for the receiver.
- [var isAbstract: Bool](./isabstract.md)
  A Boolean value that indicates whether the receiver represents an abstract entity.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  The user info dictionary of the receiver.
- [var coreSpotlightDisplayNameExpression: NSExpression](./corespotlightdisplaynameexpression.md)
  The expression that computes the CoreSpotlight display name for instances of the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/name)*