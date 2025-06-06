# rootRecordID

**Framework**: CloudKit  
**Kind**: property

The record ID of the share’s root record.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var rootRecordID: CKRecord.ID { get }
```

#### Discussion

CloudKit populates this property only for metadata that belongs to a shared record hierarchy. If the metadata is part of a shared record zone, the property returns `nil`. This is because, unlike a shared record hierarchy, a shared record zone doesn’t have a nominated root record.

## See Also

- [var hierarchicalRootRecordID: CKRecord.ID?](ckshare/metadata/hierarchicalrootrecordid.md)
  The record ID of the shared hierarchy’s root record.
- [var rootRecord: CKRecord?](ckshare/metadata/rootrecord.md)
  The share’s root record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/rootrecordid)*