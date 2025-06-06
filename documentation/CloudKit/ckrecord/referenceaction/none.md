# CKRecord.ReferenceAction.none

**Framework**: CloudKit  
**Kind**: case

A reference action that has no cascading behavior.

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
case none
```

#### Discussion

No action occurs when you delete a record that the current record references. Deleting a parent record doesn’t delete that record’s children. The `CKReference` object still contains the ID of the deleted record and doesn’t update.

## See Also

- [CKRecord.ReferenceAction.deleteSelf](ckrecord/referenceaction/deleteself.md)
  A reference action that cascades deletions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/referenceaction/none)*