# CKModifyRecordsOperation.RecordSavePolicy.allKeys

**Framework**: CloudKit  
**Kind**: case

A policy that instructs CloudKit to save all keys of a record, even those without changes.

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
case allKeys
```

#### Discussion

> ❗ **Important**:  This policy doesn’t compare record change tags. To ensure that you only save changes to the most recent version of a record, use [`CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged`](ckmodifyrecordsoperation/recordsavepolicy/ifserverrecordunchanged.md) instead.

 This policy doesn’t compare record change tags. To ensure that you only save changes to the most recent version of a record, use [`CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged`](ckmodifyrecordsoperation/recordsavepolicy/ifserverrecordunchanged.md) instead.

This policy causes CloudKit to overwrite any existing values on the server. It’s possible for a server record to contain keys that aren’t present locally. Another client might add keys to the record after you fetch it. Also, if you use the [`desiredKeys`](ckfetchrecordsoperation/desiredkeys-34l1l.md) property to request a subset of keys during a fetch operation, saving that same record modifies only those keys that you include in the fetch and any keys you add to the record after that.

## See Also

- [CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged](ckmodifyrecordsoperation/recordsavepolicy/ifserverrecordunchanged.md)
  A policy that instructs CloudKit to only proceed if the record’s change tag matches that of the server’s copy.
- [CKModifyRecordsOperation.RecordSavePolicy.changedKeys](ckmodifyrecordsoperation/recordsavepolicy/changedkeys.md)
  A policy that instructs CloudKit to save only the fields of a record that contain changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordsavepolicy/allkeys)*