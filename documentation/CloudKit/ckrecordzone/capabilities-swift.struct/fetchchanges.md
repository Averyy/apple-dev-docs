# fetchChanges

**Framework**: CloudKit  
**Kind**: property  
**Role**: Type Property

A capability for fetching only the changed records from a zone.

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
static var fetchChanges: CKRecordZone.Capabilities { get }
```

```c
CKRecordZoneCapabilityFetchChanges
```

## Discussion

This capability makes the creation of offline caches more efficient. Instead of fetching the entire record every time, use [`CKFetchRecordZoneChangesOperation`](../../ckfetchrecordzonechangesoperation.md) to fetch only the changed values, and use the data it returns to update your cache. This minimizes the amount of data you receive from the server.

## See Also

### Zone Capabilities
- [static var atomic: CKRecordZone.Capabilities](./atomic.md)
  A capability that allows atomic changes of multiple records.
- [static var sharing: CKRecordZone.Capabilities](./sharing.md)
  A capability for sharing a specific hierarchy of records.
- [static var zoneWideSharing: CKRecordZone.Capabilities](./zonewidesharing.md)
  A capability for sharing the entire contents of a record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/capabilities-swift.struct/fetchchanges)*