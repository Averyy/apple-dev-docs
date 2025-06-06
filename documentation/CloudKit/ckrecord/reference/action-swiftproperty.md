# action

**Framework**: CloudKit  
**Kind**: property

The ownership behavior for the records.

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
var action: CKRecord.ReferenceAction { get }
```

#### Discussion

The value in this property determines which action, if any, to take when deleting the target of the reference object — that is, the object that the [`recordID`](ckrecord/reference/recordid.md) property points to. When this property is [`CKRecord.ReferenceAction.deleteSelf`](ckrecord/referenceaction/deleteself.md), deleting the target object deletes any records that contain that reference in one of their fields. When this property is [`CKRecord.ReferenceAction.none`](ckrecord/referenceaction/none.md), deleting the target object doesn’t delete any additional objects.

## See Also

- [var recordID: CKRecord.ID](ckrecord/reference/recordid.md)
  The ID of the referenced record.
- [CKRecord.ReferenceAction](ckrecord/referenceaction.md)
  Constants that indicate the behavior when deleting a referenced record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/reference/action-swift.property)*