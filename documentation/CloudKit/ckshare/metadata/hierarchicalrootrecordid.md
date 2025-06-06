# hierarchicalRootRecordID

**Framework**: CloudKit  
**Kind**: property

The record ID of the shared hierarchy’s root record.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@NSCopying
var hierarchicalRootRecordID: CKRecord.ID? { get }
```

#### Discussion

CloudKit populates this property only for metadata that belongs to a shared record hierarchy. If the metadata is part of a shared record zone, the property is `nil`. This is because, unlike a shared record hierarchy, a shared record zone doesn’t have a nominated root record.

## See Also

- [var rootRecord: CKRecord?](ckshare/metadata/rootrecord.md)
  The share’s root record.
- [var rootRecordID: CKRecord.ID](ckshare/metadata/rootrecordid.md)
  The record ID of the share’s root record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/hierarchicalrootrecordid)*