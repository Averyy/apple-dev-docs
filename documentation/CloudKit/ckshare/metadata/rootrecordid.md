# rootRecordID

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The record ID of the share’s root record.

**Availability**:
- iOS 10.0+ - Deprecated in 16.0
- iPadOS 10.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.12+ - Deprecated in 13.0
- tvOS 10.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 9.0

> **Deprecated**: Use [`hierarchicalRootRecordID`](./hierarchicalrootrecordid.md) instead.

## Declaration

```swift
@NSCopying
var rootRecordID: CKRecord.ID { get }
```

```objc
@property (copy, readonly) CKRecordID * rootRecordID;
```

## Discussion

CloudKit populates this property only for metadata that belongs to a shared record hierarchy. If the metadata is part of a shared record zone, the property returns `nil`. This is because, unlike a shared record hierarchy, a shared record zone doesn’t have a nominated root record.

## See Also

### Accessing the Root Record
- [var hierarchicalRootRecordID: CKRecord.ID?](./hierarchicalrootrecordid.md)
  The record ID of the shared hierarchy’s root record.
- [var rootRecord: CKRecord?](./rootrecord.md)
  The share’s root record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/rootrecordid)*