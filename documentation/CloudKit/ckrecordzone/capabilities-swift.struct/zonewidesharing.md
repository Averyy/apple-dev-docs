# zoneWideSharing

**Framework**: CloudKit  
**Kind**: property

A capability for sharing the entire contents of a record zone.

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
static var zoneWideSharing: CKRecordZone.Capabilities { get }
```

#### Discussion

CloudKit allows you to share custom record zones that you create in the user’s private database. For more information, see [`Shared Records`](shared-records.md).

## See Also

- [static var atomic: CKRecordZone.Capabilities](ckrecordzone/capabilities-swift.struct/atomic.md)
  A capability that allows atomic changes of multiple records.
- [static var fetchChanges: CKRecordZone.Capabilities](ckrecordzone/capabilities-swift.struct/fetchchanges.md)
  A capability for fetching only the changed records from a zone.
- [static var sharing: CKRecordZone.Capabilities](ckrecordzone/capabilities-swift.struct/sharing.md)
  A capability for sharing a specific hierarchy of records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/capabilities-swift.struct/zonewidesharing)*