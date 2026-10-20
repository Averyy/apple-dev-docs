# failedRecordDeletes

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The unique identifiers of the records CloudKit is unable to delete, and the reasons why.

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
let failedRecordDeletes: [CKRecord.ID : CKError]
```

## See Also

### Accessing failed changes
- [let failedRecordSaves: [CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave]](./failedrecordsaves.md)
  The records that CloudKit is unable to modify.
- [CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave](./failedrecordsave.md)
  A type that describes an unsuccessful attempt to modify a single record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/sentrecordzonechanges/failedrecorddeletes)*