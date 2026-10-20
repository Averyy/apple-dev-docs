# updatedObjects

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The objects that were modified in the calling context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var updatedObjects: Set<NSManagedObject>? { get }
```

```objc
@property (strong, readonly, nullable) NSSet<__kindof NSManagedObject *> * updatedObjects;
```

## See Also

### Getting Information about a Request
- [var insertedObjects: Set<NSManagedObject>?](./insertedobjects.md)
  The objects that were inserted into the calling context.
- [var deletedObjects: Set<NSManagedObject>?](./deletedobjects.md)
  The objects that were deleted in the calling context.
- [var lockedObjects: Set<NSManagedObject>?](./lockedobjects.md)
  The objects that were flagged for optimistic locking on the calling context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nssavechangesrequest/updatedobjects)*