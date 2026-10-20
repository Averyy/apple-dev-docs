# CKRecord.ReferenceAction

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the behavior when deleting a referenced record.

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
enum ReferenceAction
```

```c
enum CKReferenceAction : NSUInteger;
```

## Topics

### Deletion Reference Actions
- [CKRecord.ReferenceAction.none](./referenceaction/none.md)
  A reference action that has no cascading behavior.
- [CKRecord.ReferenceAction.deleteSelf](./referenceaction/deleteself.md)
  A reference action that cascades deletions.
### Initializers
- [init?(rawValue: UInt)](./referenceaction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Reference Attributes
- [var action: CKRecord.ReferenceAction](./reference/action-swift.property.md)
  The ownership behavior for the records.
- [var recordID: CKRecord.ID](./reference/recordid.md)
  The ID of the referenced record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/referenceaction)*