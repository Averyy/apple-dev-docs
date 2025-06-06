# renamingIdentifier

**Framework**: Core Data  
**Kind**: property

The renaming identifier for the receiver.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var renamingIdentifier: String? { get set }
```

#### Discussion

The renaming identifier is used to resolve naming conflicts between models. When creating a mapping model between two managed object models, a source entity and a destination entity that share the same identifier indicate that an entity mapping should be configured to migrate from the source to the destination.

If you do not set this value, the identifier will return the entity’s name.

## See Also

- [var name: String?](nsentitydescription/name.md)
  The entity name of the receiver.
- [var managedObjectModel: NSManagedObjectModel](nsentitydescription/managedobjectmodel.md)
  The managed object model with which the receiver is associated.
- [var managedObjectClassName: String!](nsentitydescription/managedobjectclassname.md)
  The name of the class that represents the receiver’s entity.
- [var isAbstract: Bool](nsentitydescription/isabstract.md)
  A Boolean value that indicates whether the receiver represents an abstract entity.
- [var userInfo: [AnyHashable : Any]?](nsentitydescription/userinfo.md)
  The user info dictionary of the receiver.
- [var coreSpotlightDisplayNameExpression: NSExpression](nsentitydescription/corespotlightdisplaynameexpression.md)
  The expression that computes the CoreSpotlight display name for instances of the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/renamingidentifier)*