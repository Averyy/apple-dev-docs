# NSRelationshipDescription

**Framework**: Core Data  
**Kind**: class

A description of a relationship between two entities.

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
class NSRelationshipDescription
```

#### Overview

[`NSRelationshipDescription`](nsrelationshipdescription.md) provides additional attributes that are specific to modeling a relationship between two entities. For the common attributes of all property types, see [`NSPropertyDescription`](nspropertydescription.md).

For example, use this class to define a relationship’s  — the number of managed objects the relationship can reference.

- For a to-one relationship, set [`maxCount`](nsrelationshipdescription/maxcount.md) to `1`.
- For a to-many relationship, set [`maxCount`](nsrelationshipdescription/maxcount.md) to a number greater than `1` to impose an upper limit; otherwise, use `0` to allow an unlimited number of referenced objects.

At runtime, you can modify a relationship description until you associate its owning managed object model with a persistent store coordinator.  If you attempt to modify the model after you associate it, Core Data throws an exception. To modify a model that’s in use, create and modify a copy and then discard any objects that belong to the original model.

## Topics

### Configuring the Destination
- [var inverseRelationship: NSRelationshipDescription?](nsrelationshipdescription/inverserelationship.md)
  The relationship that represents the inverse of the current relationship.
- [var destinationEntity: NSEntityDescription?](nsrelationshipdescription/destinationentity.md)
  The type of object the relationship contains.
- [var isOrdered: Bool](nsrelationshipdescription/isordered.md)
  A Boolean value that determines whether the relationship preserves the order of the referenced managed objects.
### Configuring Cardinality
- [var isToMany: Bool](nsrelationshipdescription/istomany.md)
  Returns a Boolean value that indicates whether the relationship can contain many managed objects.
- [var minCount: Int](nsrelationshipdescription/mincount.md)
  The minimum number of managed objects the relationship can reference.
- [var maxCount: Int](nsrelationshipdescription/maxcount.md)
  The maximum number of managed objects the relationship can reference.
### Configuring Delete Behavior
- [var deleteRule: NSDeleteRule](nsrelationshipdescription/deleterule.md)
  The rule to apply when you delete the relationship’s owning managed object.
- [enum NSDeleteRule](nsdeleterule.md)
  Constants that determine what happens when you delete a relationship’s owning managed object.
### Getting Version Data
- [var versionHash: Data](nsrelationshipdescription/versionhash.md)
  The relationship’s unique identity.

## Relationships

### Inherits From
- [NSPropertyDescription](nspropertydescription.md)
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

- [class NSPropertyDescription](nspropertydescription.md)
  A description of a single property belonging to an entity.
- [class NSAttributeDescription](nsattributedescription.md)
  A description of a single attribute belonging to an entity.
- [enum NSAttributeType](nsattributetype.md)
  The types of attribute that Core Data supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsrelationshipdescription)*