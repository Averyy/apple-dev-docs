# recordID

**Framework**: CloudKit  
**Kind**: property

The ID of the referenced record.

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
@NSCopying
var recordID: CKRecord.ID { get }
```

#### Discussion

Use the ID in this property to fetch the record on the other end of the link.

## See Also

- [var action: CKRecord.ReferenceAction](ckrecord/reference/action-swift.property.md)
  The ownership behavior for the records.
- [CKRecord.ReferenceAction](ckrecord/referenceaction.md)
  Constants that indicate the behavior when deleting a referenced record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/reference/recordid)*