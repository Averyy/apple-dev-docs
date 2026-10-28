# action

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The ownership behavior for the records.

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
var action: CKRecord.ReferenceAction { get }
```

```objc
@property (nonatomic, assign, readonly) CKReferenceAction referenceAction;
```

## Discussion

The value in this property determines which action, if any, to take when deleting the target of the reference object — that is, the object that the [`recordID`](./recordid.md) property points to. When this property is [`CKRecord.ReferenceAction.deleteSelf`](../referenceaction/deleteself.md), deleting the target object deletes any records that contain that reference in one of their fields. When this property is [`CKRecord.ReferenceAction.none`](../referenceaction/none.md), deleting the target object doesn’t delete any additional objects.

## See Also

### Getting the Reference Attributes
- [var recordID: CKRecord.ID](./recordid.md)
  The ID of the referenced record.
- [CKRecord.ReferenceAction](../referenceaction.md)
  Constants that indicate the behavior when deleting a referenced record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/reference/action-swift.property)*