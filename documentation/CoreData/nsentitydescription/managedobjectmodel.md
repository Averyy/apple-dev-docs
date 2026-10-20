# managedObjectModel

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The managed object model with which the receiver is associated.

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
unowned(unsafe) var managedObjectModel: NSManagedObjectModel { get }
```

```objc
@property (assign, readonly) NSManagedObjectModel * managedObjectModel;
```

## See Also

### Related Documentation
- [func setEntities([NSEntityDescription], forConfigurationName: String)](../nsmanagedobjectmodel/setentities%28_,forconfigurationname%29.md)
  Associates the specified entities with the model using the given configuration name.
- [var entities: [NSEntityDescription]](../nsmanagedobjectmodel/entities.md)
  The entities in the model.
### Getting descriptive information
- [var name: String?](./name.md)
  The entity name of the receiver.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/managedobjectmodel)*