# CKDatabaseOperation

**Framework**: CloudKit  
**Kind**: class

The abstract base class for operations that act upon databases in CloudKit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class CKDatabaseOperation
```

#### Overview

Database operations typically involve fetching and saving records and other database objects, as well as executing queries on the contents of the database. Use this class’s [`database`](ckdatabaseoperation/database.md) property to tell the operation which database to use when you execute it. Don’t subclass this class or create instances of it. Instead, create instances of one of its concrete subclasses.

## Topics

### Accessing the Database
- [var database: CKDatabase?](ckdatabaseoperation/database.md)
  The database that the operation uses.

## Relationships

### Inherits From
- [CKOperation](ckoperation.md)
### Inherited By
- [CKFetchDatabaseChangesOperation](ckfetchdatabasechangesoperation.md)
- [CKFetchRecordChangesOperation](ckfetchrecordchangesoperation.md)
- [CKFetchRecordZoneChangesOperation](ckfetchrecordzonechangesoperation.md)
- [CKFetchRecordZonesOperation](ckfetchrecordzonesoperation.md)
- [CKFetchRecordsOperation](ckfetchrecordsoperation.md)
- [CKFetchSubscriptionsOperation](ckfetchsubscriptionsoperation.md)
- [CKFetchWebAuthTokenOperation](ckfetchwebauthtokenoperation.md)
- [CKModifyRecordZonesOperation](ckmodifyrecordzonesoperation.md)
- [CKModifyRecordsOperation](ckmodifyrecordsoperation.md)
- [CKModifySubscriptionsOperation](ckmodifysubscriptionsoperation.md)
- [CKQueryOperation](ckqueryoperation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabaseoperation)*