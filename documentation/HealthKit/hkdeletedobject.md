# HKDeletedObject

**Framework**: HealthKit  
**Kind**: class

An object that represents a sample that has been deleted from the HealthKit store.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKDeletedObject
```

## Mentions

- [About the HealthKit framework](about-the-healthkit-framework.md)

#### Overview

Use [`HKAnchoredObjectQuery`](hkanchoredobjectquery.md) queries to generate a list of recently deleted objects. Create a query using the [`init(type:predicate:anchor:limit:resultsHandler:)`](hkanchoredobjectquery/init(type:predicate:anchor:limit:resultshandler:).md)method. When the system calls the result handler, it passes the `deletedObject` parameter an array of [`HKDeletedObject`](hkdeletedobject.md) instances matching the query.

Deleted objects are temporary; the system may remove them from the HealthKit store at any time to free up space. To guarantee that you receive notifications for all deleted objects, create an [`HKObserverQuery`](hkobserverquery.md) and register it for background delivery. The system then wakes your app and calls the observer query’s update handler whenever the matching objects change—including deletions. However, the query does not provide a list of deleted objects. To determine which objects were deleted, use the observer query’s update handler to create an anchored object query for the newly deleted objects.

## Topics

### Identifying Deleted Objects
- [var uuid: UUID](hkdeletedobject/uuid.md)
  The universally unique identifier (UUID) for the HealthKit object that was deleted from the store.
- [var metadata: [String : Any]?](hkdeletedobject/metadata.md)
  The metadata associated with the deleted object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdeletedobject)*