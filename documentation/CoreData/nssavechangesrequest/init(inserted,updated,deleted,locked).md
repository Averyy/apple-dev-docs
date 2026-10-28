# init(inserted:updated:deleted:locked:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Initializes a save changes request with collections of given changes.

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
init(inserted insertedObjects: Set<NSManagedObject>?, updated updatedObjects: Set<NSManagedObject>?, deleted deletedObjects: Set<NSManagedObject>?, locked lockedObjects: Set<NSManagedObject>?)
```

```objc
- (instancetype) initWithInsertedObjects:(NSSet<NSManagedObject *> *) insertedObjects updatedObjects:(NSSet<NSManagedObject *> *) updatedObjects deletedObjects:(NSSet<NSManagedObject *> *) deletedObjects lockedObjects:(NSSet<NSManagedObject *> *) lockedObjects;
```

## Return Value

A save changes request initialized with the given changes.

## Parameters

- `insertedObjects`: Objects that were inserted into the calling context.
- `updatedObjects`: Objects that were updated in the calling context.
- `deletedObjects`: Objects that were deleted in the calling context.
- `lockedObjects`: Objects that were flagged for optimistic locking on the calling context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nssavechangesrequest/init(inserted:updated:deleted:locked:))*