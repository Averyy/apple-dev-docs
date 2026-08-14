# rootRecord

**Framework**: CloudKit  
**Kind**: property

The share’s root record.

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
var rootRecord: CKRecord? { get }
```

#### Discussion

This property contains the root record of the shared record hierarchy if you set the [`shouldFetchRootRecord`](ckfetchsharemetadataoperation/shouldfetchrootrecord.md) property of the operation that fetches the metadata to [`true`](https://developer.apple.com/documentation/swift/true). You can specify which fields CloudKit returns by setting the same operation’s [`rootRecordDesiredKeys`](ckfetchsharemetadataoperation/rootrecorddesiredkeys-3xrex.md) property.

The operation ignores the [`shouldFetchRootRecord`](ckfetchsharemetadataoperation/shouldfetchrootrecord.md) and [`rootRecordDesiredKeys`](ckfetchsharemetadataoperation/rootrecorddesiredkeys-3xrex.md) properties when fetching a shared record zone’s metadata because, unlike a shared record hierarchy, a record zone doesn’t have a nominated root record.

## See Also

- [var hierarchicalRootRecordID: CKRecord.ID?](ckshare/metadata/hierarchicalrootrecordid.md)
  The record ID of the shared hierarchy’s root record.
- [var rootRecordID: CKRecord.ID](ckshare/metadata/rootrecordid.md)
  The record ID of the share’s root record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/rootrecord)*