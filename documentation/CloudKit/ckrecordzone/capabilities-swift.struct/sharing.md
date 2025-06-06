# sharing

**Framework**: CloudKit  
**Kind**: property

A capability for sharing a specific hierarchy of records.

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
static var sharing: CKRecordZone.Capabilities { get }
```

#### Discussion

CloudKit allows you to share record hierarchies from custom record zones that you create in the user’s private database. For more information, see [`Shared Records`](shared-records.md).

## See Also

- [static var atomic: CKRecordZone.Capabilities](ckrecordzone/capabilities-swift.struct/atomic.md)
  A capability that allows atomic changes of multiple records.
- [static var fetchChanges: CKRecordZone.Capabilities](ckrecordzone/capabilities-swift.struct/fetchchanges.md)
  A capability for fetching only the changed records from a zone.
- [static var zoneWideSharing: CKRecordZone.Capabilities](ckrecordzone/capabilities-swift.struct/zonewidesharing.md)
  A capability for sharing the entire contents of a record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/capabilities-swift.struct/sharing)*