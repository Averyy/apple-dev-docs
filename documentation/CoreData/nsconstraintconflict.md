# NSConstraintConflict

**Framework**: Core Data  
**Kind**: class

An encapsulation of conflicts that occur during an attempt to save a managed object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSConstraintConflict
```

#### Overview

A constraint conflict occurs when your data model is using unique constraints and one or more managed objects are violating that constraint.

When this error occurs, the error instance can be interrogated to determine which instance of [`NSManagedObject`](nsmanagedobject.md) is violating the constraint and which property on the [`NSManagedObject`](nsmanagedobject.md) instance is in violation.

## Topics

### Initializing a Conflict
- [init(constraint: [String], database: NSManagedObject?, databaseSnapshot: [AnyHashable : Any]?, conflicting: [NSManagedObject], conflictingSnapshots: [Any])](nsconstraintconflict/init(constraint:database:databasesnapshot:conflicting:conflictingsnapshots:).md)
  Initializes a constraint conflict.
### Inspecting a Conflict
- [var conflictingObjects: [NSManagedObject]](nsconstraintconflict/conflictingobjects.md)
  The managed objects that are in conflict.
- [var conflictingSnapshots: [[AnyHashable : Any]]](nsconstraintconflict/conflictingsnapshots.md)
  The original property values of objects in violation of the constraint.
- [var constraint: [String]](nsconstraintconflict/constraint.md)
  The constraint that has been violated.
- [var constraintValues: [String : Any]](nsconstraintconflict/constraintvalues.md)
  The values that the conflicting objects had when the conflict was created.
- [var databaseObject: NSManagedObject?](nsconstraintconflict/databaseobject.md)
  The object whose database row is using constraint values.
- [var databaseSnapshot: [String : Any]?](nsconstraintconflict/databasesnapshot.md)
  The values currently stored in the database.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSMergeConflict](nsmergeconflict.md)
  An encapsulation of conflicts that occur during an attempt to save changes in a managed object context.
- [class NSMergePolicy](nsmergepolicy.md)
  A policy object that you use to resolve conflicts between the persistent store and in-memory versions of managed objects.
- [class NSQueryGenerationToken](nsquerygenerationtoken.md)
  A token that indicates which generation of the persistent store is being accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsconstraintconflict)*