# CKModifyRecordsOperation.RecordSavePolicy.changedKeys

**Framework**: CloudKit  
**Kind**: case

A policy that instructs CloudKit to save only the fields of a record that contain changes.

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
case changedKeys
```

#### Discussion

> ❗ **Important**:  This policy doesn’t compare record change tags. To ensure that you only save changes to the most recent version of a record, use [`CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged`](ckmodifyrecordsoperation/recordsavepolicy/ifserverrecordunchanged.md) instead.

 This policy doesn’t compare record change tags. To ensure that you only save changes to the most recent version of a record, use [`CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged`](ckmodifyrecordsoperation/recordsavepolicy/ifserverrecordunchanged.md) instead.

## See Also

- [CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged](ckmodifyrecordsoperation/recordsavepolicy/ifserverrecordunchanged.md)
  A policy that instructs CloudKit to only proceed if the record’s change tag matches that of the server’s copy.
- [CKModifyRecordsOperation.RecordSavePolicy.allKeys](ckmodifyrecordsoperation/recordsavepolicy/allkeys.md)
  A policy that instructs CloudKit to save all keys of a record, even those without changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordsavepolicy/changedkeys)*