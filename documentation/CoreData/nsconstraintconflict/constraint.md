# constraint

**Framework**: Core Data  
**Kind**: property

The constraint that has been violated.

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
var constraint: [String] { get }
```

## See Also

- [var conflictingObjects: [NSManagedObject]](nsconstraintconflict/conflictingobjects.md)
  The managed objects that are in conflict.
- [var conflictingSnapshots: [[AnyHashable : Any]]](nsconstraintconflict/conflictingsnapshots.md)
  The original property values of objects in violation of the constraint.
- [var constraintValues: [String : Any]](nsconstraintconflict/constraintvalues.md)
  The values that the conflicting objects had when the conflict was created.
- [var databaseObject: NSManagedObject?](nsconstraintconflict/databaseobject.md)
  The object whose database row is using constraint values.
- [var databaseSnapshot: [String : Any]?](nsconstraintconflict/databasesnapshot.md)
  The values currently stored in the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsconstraintconflict/constraint)*