# fetchAllChanges

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) BOOL fetchAllChanges;
```

#### Discussion

If [`true`](../../Swift/true.md), the operation sends repeat requests to the server until it fetches all changes. CloudKit executes the handler you set on the [`recordZoneFetchResultBlock`](./recordzonefetchresultblock.md) property with a change token after each request.

The default value is [`true`](../../Swift/true.md).

## See Also

### Configuring the Zone Change Operation
- [var configurationsByRecordZoneID: [CKRecordZone.ID : CKFetchRecordZoneChangesOperation.ZoneConfiguration]?](./configurationsbyrecordzoneid.md)
  A dictionary of configurations for fetching change operations by zone identifier.
- [CKFetchRecordZoneChangesOperation.ZoneConfiguration](./zoneconfiguration.md)
  A configuration object that describes the information to fetch from a record zone.
- [var recordZoneIDs: [CKRecordZone.ID]?](./recordzoneids.md)
  The IDs of the record zones that contain the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/fetchallchanges)*