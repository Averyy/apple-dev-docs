# CKModifyRecordsOperation.RecordSavePolicy.changedKeys

**Framework**: CloudKit  
**Kind**: case  
**Role**: Case

A policy that instructs CloudKit to save only the fields of a record that contain changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case changedKeys
```

```c
CKRecordSaveChangedKeys
```

## Discussion

> ❗ **Important**: This policy doesn’t compare record change tags. To only save changes to the most recent version of a record, use [`CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged`](./ifserverrecordunchanged.md) instead.

## See Also

### Save Policies
- [CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged](./ifserverrecordunchanged.md)
  A policy that instructs CloudKit to only proceed if the record’s change tag matches that of the server’s copy.
- [CKModifyRecordsOperation.RecordSavePolicy.allKeys](./allkeys.md)
  A policy that instructs CloudKit to save all keys of a record, even those without changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordsavepolicy/changedkeys)*