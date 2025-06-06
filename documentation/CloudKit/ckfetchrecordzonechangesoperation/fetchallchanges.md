# fetchAllChanges

**Framework**: CloudKit  
**Kind**: property

A Boolean value that indicates whether to send repeated requests to the server.

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
var fetchAllChanges: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the operation sends repeat requests to the server until it fetches all changes. CloudKit executes the handler you set on the [`recordZoneFetchCompletionBlock`](ckfetchrecordzonechangesoperation/recordzonefetchcompletionblock.md) property with a change token after each request.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var configurationsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneConfiguration]?](ckfetchrecordzonechangesoperation/configurationsbyrecordzoneid.md)
  A dictionary of configurations for fetching change operations by zone identifier.
- [CKFetchRecordZoneChangesOperation.ZoneConfiguration](ckfetchrecordzonechangesoperation/zoneconfiguration.md)
  A configuration object that describes the information to fetch from a record zone.
- [var recordZoneIDs: [CKRecordZone.ID]?](ckfetchrecordzonechangesoperation/recordzoneids.md)
  The IDs of the record zones that contain the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/fetchallchanges)*