# CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

A type that describes an unsuccessful attempt to modify a single record.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
struct FailedRecordSave
```

## Topics

### Accessing the record
- [let record: CKRecord](./failedrecordsave/record.md)
  The record that CloudKit is unable to modify.
### Accessing the error
- [let error: CKError](./failedrecordsave/error.md)
  An error that describes the reason for the unsuccessful attempt to modify the associated record.
### Debugging the type
- [var description: String](./failedrecordsave/description.md)
  A textual description of the type that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](./failedrecordsave/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../../../Swift/copyable.md)
- [CustomStringConvertible](../../../../Swift/customstringconvertible.md)
- [Escapable](../../../../Swift/escapable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Accessing failed changes
- [let failedRecordDeletes: [CKRecord.ID : CKError]](./failedrecorddeletes.md)
  The unique identifiers of the records CloudKit is unable to delete, and the reasons why.
- [let failedRecordSaves: [CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave]](./failedrecordsaves.md)
  The records that CloudKit is unable to modify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/sentrecordzonechanges/failedrecordsave)*