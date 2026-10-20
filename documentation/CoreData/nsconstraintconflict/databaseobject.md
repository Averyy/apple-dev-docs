# databaseObject

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The object whose database row is using constraint values.

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
var databaseObject: NSManagedObject? { get }
```

```objc
@property (retain, readonly, nullable) NSManagedObject * databaseObject;
```

## See Also

### Inspecting a Conflict
- [var conflictingObjects: [NSManagedObject]](./conflictingobjects.md)
  The managed objects that are in conflict.
- [var conflictingSnapshots: [[AnyHashable : Any]]](./conflictingsnapshots.md)
  The original property values of objects in violation of the constraint.
- [var constraint: [String]](./constraint.md)
  The constraint that has been violated.
- [var constraintValues: [String : Any]](./constraintvalues.md)
  The values that the conflicting objects had when the conflict was created.
- [var databaseSnapshot: [String : Any]?](./databasesnapshot.md)
  The values currently stored in the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsconstraintconflict/databaseobject)*