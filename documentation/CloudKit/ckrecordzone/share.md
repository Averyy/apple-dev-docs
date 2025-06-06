# share

**Framework**: CloudKit  
**Kind**: property

A reference to the record zone’s share record.

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
var share: CKRecord.Reference? { get }
```

#### Discussion

CloudKit sets this property only for fetched record zones that contain a share record; otherwise, it’s `nil`.

To share a record zone, create a share record using the [`init(recordZoneID:)`](ckshare/init(recordzoneid:).md) method and then save it to the server. Shared record zones must have the [`zoneWideSharing`](ckrecordzone/capabilities-swift.struct/zonewidesharing.md) capability, which CloudKit enables by default for new custom record zones in the user’s private database.

A record zone, and the records it contains, can take part in only a single share. CloudKit returns an error if you attempt to share an already-shared record zone, or if that record zone contains previously shared records.

Record zone sharing errors include the following:

- [`CKError.Code.serverRecordChanged`](ckerror/code/serverrecordchanged.md), which CloudKit returns if you try to share an already-shared record zone.
- [`CKError.Code.serverRejectedRequest`](ckerror/code/serverrejectedrequest.md), which CloudKit returns if you try to share a record hierarchy from an already-shared record zone.
- [`CKError.Code.invalidArguments`](ckerror/code/invalidarguments.md), which CloudKit returns if you try to share a record zone that contains one or more shared hierarchies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/share)*