# CKRecord.ReferenceAction

**Framework**: CloudKit  
**Kind**: enum

Constants that indicate the behavior when deleting a referenced record.

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
enum ReferenceAction
```

## Topics

### Deletion Reference Actions
- [CKRecord.ReferenceAction.none](ckrecord/referenceaction/none.md)
  A reference action that has no cascading behavior.
- [CKRecord.ReferenceAction.deleteSelf](ckrecord/referenceaction/deleteself.md)
  A reference action that cascades deletions.
### Initializers
- [init?(rawValue: UInt)](ckrecord/referenceaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var action: CKRecord.ReferenceAction](ckrecord/reference/action-swift.property.md)
  The ownership behavior for the records.
- [var recordID: CKRecord.ID](ckrecord/reference/recordid.md)
  The ID of the referenced record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/referenceaction)*