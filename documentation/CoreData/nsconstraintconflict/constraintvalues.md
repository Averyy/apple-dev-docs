# constraintValues

**Framework**: Core Data  
**Kind**: property

The values that the conflicting objects had when the conflict was created.

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
var constraintValues: [String : Any] { get }
```

## See Also

- [var conflictingObjects: [NSManagedObject]](nsconstraintconflict/conflictingobjects.md)
  The managed objects that are in conflict.
- [var conflictingSnapshots: [[AnyHashable : Any]]](nsconstraintconflict/conflictingsnapshots.md)
  The original property values of objects in violation of the constraint.
- [var constraint: [String]](nsconstraintconflict/constraint.md)
  The constraint that has been violated.
- [var databaseObject: NSManagedObject?](nsconstraintconflict/databaseobject.md)
  The object whose database row is using constraint values.
- [var databaseSnapshot: [String : Any]?](nsconstraintconflict/databasesnapshot.md)
  The values currently stored in the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsconstraintconflict/constraintvalues)*