# conflictingSnapshots

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The original property values of objects in violation of the constraint.

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
var conflictingSnapshots: [[AnyHashable : Any]] { get }
```

```objc
@property (copy, readonly) NSArray<NSDictionary *> * conflictingSnapshots;
```

## See Also

### Inspecting a Conflict
- [var conflictingObjects: [NSManagedObject]](./conflictingobjects.md)
  The managed objects that are in conflict.
- [var constraint: [String]](./constraint.md)
  The constraint that has been violated.
- [var constraintValues: [String : Any]](./constraintvalues.md)
  The values that the conflicting objects had when the conflict was created.
- [var databaseObject: NSManagedObject?](./databaseobject.md)
  The object whose database row is using constraint values.
- [var databaseSnapshot: [String : Any]?](./databasesnapshot.md)
  The values currently stored in the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsconstraintconflict/conflictingsnapshots)*