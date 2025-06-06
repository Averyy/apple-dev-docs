# configurationsByRecordZoneID

**Framework**: CloudKit  
**Kind**: property

A dictionary of configurations for fetching change operations by zone identifier.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var configurationsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneConfiguration]? { get set }
```

## See Also

- [CKFetchRecordZoneChangesOperation.ZoneConfiguration](ckfetchrecordzonechangesoperation/zoneconfiguration.md)
  A configuration object that describes the information to fetch from a record zone.
- [var fetchAllChanges: Bool](ckfetchrecordzonechangesoperation/fetchallchanges.md)
  A Boolean value that indicates whether to send repeated requests to the server.
- [var recordZoneIDs: [CKRecordZone.ID]?](ckfetchrecordzonechangesoperation/recordzoneids.md)
  The IDs of the record zones that contain the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/configurationsbyrecordzoneid)*