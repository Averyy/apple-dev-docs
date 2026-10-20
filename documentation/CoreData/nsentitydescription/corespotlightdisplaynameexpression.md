# coreSpotlightDisplayNameExpression

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The expression that computes the CoreSpotlight display name for instances of the entity.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var coreSpotlightDisplayNameExpression: NSExpression { get set }
```

```objc
@property (nonatomic, retain) NSExpression * coreSpotlightDisplayNameExpression;
```

## See Also

### Getting descriptive information
- [var name: String?](./name.md)
  The entity name of the receiver.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/corespotlightdisplaynameexpression)*