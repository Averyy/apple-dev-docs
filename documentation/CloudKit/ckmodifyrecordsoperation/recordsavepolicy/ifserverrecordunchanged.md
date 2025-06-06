# CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged

**Framework**: CloudKit  
**Kind**: case

A policy that instructs CloudKit to only proceed if the record’s change tag matches that of the server’s copy.

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
case ifServerRecordUnchanged
```

#### Discussion

The server maintains a change tag for each record automatically. When you fetch a record, that change tag accompanies the rest of the record’s data. If the change tag in your local record matches the change tag of the record on the server, the save operation proceeds normally. If the server record contains a newer change tag, CloudKit doesn’t save the record and reports a [`CKError.Code.serverRecordChanged`](ckerror/code/serverrecordchanged.md) error.

## See Also

- [CKModifyRecordsOperation.RecordSavePolicy.changedKeys](ckmodifyrecordsoperation/recordsavepolicy/changedkeys.md)
  A policy that instructs CloudKit to save only the fields of a record that contain changes.
- [CKModifyRecordsOperation.RecordSavePolicy.allKeys](ckmodifyrecordsoperation/recordsavepolicy/allkeys.md)
  A policy that instructs CloudKit to save all keys of a record, even those without changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordsavepolicy/ifserverrecordunchanged)*