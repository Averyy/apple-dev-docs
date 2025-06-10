# CKFetchRecordsOperation

**Framework**: CloudKit  
**Kind**: class

An operation for retrieving records from a database.

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
class CKFetchRecordsOperation
```

## Mentions

- [Encrypting User Data](encrypting-user-data.md)

#### Overview

Use this operation to retrieve the entire contents of each record or only a subset of its contained values. As records become available, the operation object reports progress about the state of the operation to several different blocks, which you can use to process the results.

Fetching records is a common use of CloudKit, even if your app doesn’t cache record IDs locally. For example, when you fetch a record related to the current record through a [`CKRecord.Reference`](ckrecord/reference.md) object, you use the ID in the reference to perform the fetch.

The handlers you assign to process the fetched records execute serially on an internal queue that the fetch operation manages. Your handlers must be capable of executing on a background thread, so any tasks that require access to the main thread must redirect accordingly.

In addition to data records, a fetch records operation can fetch the current user record. The [`fetchCurrentUserRecordOperation()`](ckfetchrecordsoperation/fetchcurrentuserrecordoperation().md) method returns a specially configured operation object that retrieves the current user record. That record is a standard [`CKRecord`](ckrecord.md) object that has no content initially. You can add data to the user record and save it as necessary. Don’t store sensitive personal information, such as passwords, in the user record because other users of your app can access the discoverable user record in a public database. If you must store sensitive information about a user, do so in a separate record that is accessible only to that user.

If you assign a closure to the [`completionBlock`](https://developer.apple.com/documentation/Foundation/Operation/completionBlock) property of the operation object, CloudKit calls it after the operation executes and returns its results. Use a closure to perform any housekeeping tasks for the operation, but don’t use it to process the results of the operation. The closure you specify should handle the failure of the operation to complete its task, whether due to an error or an explicit cancellation.

## Topics

### Creating a Record Fetch Operation
- [convenience init(recordIDs: [CKRecord.ID])](ckfetchrecordsoperation/init(recordids:).md)
  Creates a fetch operation for retrieving the records with the specified IDs.
- [init()](ckfetchrecordsoperation/init.md)
  Creates an empty fetch operation.
### Getting the Current User Record
- [class func fetchCurrentUserRecordOperation() -> Self](ckfetchrecordsoperation/fetchcurrentuserrecordoperation.md)
  Returns a fetch operation for retrieving the current user record.
### Configuring a Record Fetch Operation
- [var recordIDs: [CKRecord.ID]?](ckfetchrecordsoperation/recordids.md)
  The record IDs of the records to fetch.
- [var desiredKeys: [CKRecord.FieldKey]?](ckfetchrecordsoperation/desiredkeys-31bbq.md)
  The fields of the records to fetch.
### Processing Record Fetch Results
- [var perRecordProgressBlock: ((CKRecord.ID, Double) -> Void)?](ckfetchrecordsoperation/perrecordprogressblock.md)
  The closure to execute with progress information for individual records.
- [var perRecordCompletionBlock: ((CKRecord?, CKRecord.ID?, (any Error)?) -> Void)?](ckfetchrecordsoperation/perrecordcompletionblock.md)
  The closure to execute when a record becomes available.
- [var fetchRecordsCompletionBlock: (([CKRecord.ID : CKRecord]?, (any Error)?) -> Void)?](ckfetchrecordsoperation/fetchrecordscompletionblock.md)
  The closure to execute after CloudKit retrieves all of the records.
### Instance Properties
- [var fetchRecordsResultBlock: ((Result<Void, any Error>) -> Void)?](ckfetchrecordsoperation/fetchrecordsresultblock.md)
- [var perRecordResultBlock: ((CKRecord.ID, Result<CKRecord, any Error>) -> Void)?](ckfetchrecordsoperation/perrecordresultblock.md)

## Relationships

### Inherits From
- [CKDatabaseOperation](ckdatabaseoperation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CKFetchRecordZonesOperation](ckfetchrecordzonesoperation.md)
  An operation for retrieving record zones from a database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation)*