# NSPropertyDescription

**Framework**: Core Data  
**Kind**: class

A description of a single property belonging to an entity.

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
class NSPropertyDescription
```

#### Overview

A property describes a single value within an object managed by the Core Data Framework. There are different types of property, each represented by a subclass which encapsulates the specific property behavior—see [`NSAttributeDescription`](nsattributedescription.md), [`NSRelationshipDescription`](nsrelationshipdescription.md), and [`NSFetchedPropertyDescription`](nsfetchedpropertydescription.md).

Note that a property name cannot be the same as any no-parameter method name of `NSObject` or `NSManagedObject`. For example, you cannot give a property the name “description”. There are hundreds of methods on `NSObject` which may conflict with property names—and this list can grow without warning from frameworks or other libraries. You should avoid very general words (like “font”, and “color”) and words or phrases which overlap with Cocoa paradigms (such as “isEditing” and “objectSpecifier”).

Properties—relationships as well as attributes—may be transient. A managed object context knows about transient properties and tracks changes made to them. Transient properties are ignored by the persistent store, and not just during saves: you cannot fetch using a predicate based on transients (although you can use transient properties to filter in memory yourself).

##### Editing Property Descriptions

Property descriptions are editable until they are used by an object graph manager (such as a persistent store coordinator). This allows you to create or modify them dynamically. However, once a description is used (when the managed object model to which it belongs is associated with a persistent store coordinator), it  (indeed cannot) be changed. This is enforced at runtime: any attempt to mutate a model or any of its sub-objects after the model is associated with a persistent store coordinator causes an exception to be thrown. If you need to modify a model that is in use, create a copy, modify the copy, and then discard the objects with the old model.

## Topics

### Accessing Features of a Property
- [var entity: NSEntityDescription](nspropertydescription/entity.md)
  The entity description of the receiver.
- [var isIndexed: Bool](nspropertydescription/isindexed.md)
  A Boolean value that indicates whether the receiver should be indexed for searching.
- [var isOptional: Bool](nspropertydescription/isoptional.md)
  A Boolean value that indicates whether the receiver is optional.
- [var isTransient: Bool](nspropertydescription/istransient.md)
  A Boolean value that indicates whether the receiver is transient.
- [var name: String](nspropertydescription/name.md)
  The name of the receiver.
- [var userInfo: [AnyHashable : Any]?](nspropertydescription/userinfo.md)
  The user info dictionary of the receiver.
### Supporting Validation
- [var validationPredicates: [NSPredicate]](nspropertydescription/validationpredicates.md)
  The validation predicates of the receiver.
- [var validationWarnings: [Any]](nspropertydescription/validationwarnings.md)
  The error strings associated with the receiver’s validation predicates.
- [func setValidationPredicates([NSPredicate]?, withValidationWarnings: [String]?)](nspropertydescription/setvalidationpredicates(_:withvalidationwarnings:).md)
  Sets the validation predicates and warnings of the receiver.
### Supporting Versioning
- [var versionHash: Data](nspropertydescription/versionhash.md)
  The version hash for the receiver.
- [var versionHashModifier: String?](nspropertydescription/versionhashmodifier.md)
  The version hash modifier for the receiver.
- [var renamingIdentifier: String?](nspropertydescription/renamingidentifier.md)
  The renaming identifier for the receiver.
### Specifying Spotlight Support
- [var isIndexedBySpotlight: Bool](nspropertydescription/isindexedbyspotlight.md)
  A Boolean value that indicates whether Core Data adds the property’s value to the Core Spotlight index.
- [var isStoredInExternalRecord: Bool](nspropertydescription/isstoredinexternalrecord.md)
  A Boolean value that indicates whether to write the property’s data in an external record file that corresponds to the managed object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSAttributeDescription](nsattributedescription.md)
- [NSExpressionDescription](nsexpressiondescription.md)
- [NSFetchedPropertyDescription](nsfetchedpropertydescription.md)
- [NSRelationshipDescription](nsrelationshipdescription.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSAttributeDescription](nsattributedescription.md)
  A description of a single attribute belonging to an entity.
- [enum NSAttributeType](nsattributetype.md)
  The types of attribute that Core Data supports.
- [class NSRelationshipDescription](nsrelationshipdescription.md)
  A description of a relationship between two entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription)*