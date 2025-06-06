# lockedObjects

**Framework**: Core Data  
**Kind**: property

The objects that were flagged for optimistic locking on the calling context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var lockedObjects: Set<NSManagedObject>? { get }
```

#### Discussion

Objects are flagged for optimistic locking with [`detectConflicts(for:)`](nsmanagedobjectcontext/detectconflicts(for:).md).

## See Also

- [var insertedObjects: Set<NSManagedObject>?](nssavechangesrequest/insertedobjects.md)
  The objects that were inserted into the calling context.
- [var updatedObjects: Set<NSManagedObject>?](nssavechangesrequest/updatedobjects.md)
  The objects that were modified in the calling context.
- [var deletedObjects: Set<NSManagedObject>?](nssavechangesrequest/deletedobjects.md)
  The objects that were deleted in the calling context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nssavechangesrequest/lockedobjects)*