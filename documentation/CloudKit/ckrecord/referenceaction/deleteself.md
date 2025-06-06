# CKRecord.ReferenceAction.deleteSelf

**Framework**: CloudKit  
**Kind**: case

A reference action that cascades deletions.

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
case deleteSelf
```

#### Discussion

CloudKit deletes any records that contain `CKReference` objects pointing to the current record. The deletion of the additional records can trigger further deletions as the action cascades. The deletions are asynchronous in the default zone and immediate in a custom zone.

## See Also

- [CKRecord.ReferenceAction.none](ckrecord/referenceaction/none.md)
  A reference action that has no cascading behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/referenceaction/deleteself)*