# fetchRecordZones

**Framework**: CloudKit JS  
**Kind**: method

Fetches one or more zones.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.RecordZonesResponse, CloudKit.CKError> fetchRecordZones(
	CloudKit.ZoneID|CloudKit.ZoneID[]|String|String[] zones
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.RecordZonesResponse`](cloudkit.recordzonesresponse.md) object if the operation succeeds; otherwise, a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

See [`Fetching Zones by Identifier (zones/lookup)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/GettingZonesbyIdentifier.html#//apple_ref/doc/uid/TP40015240-CH22) in [`CloudKit Web Services Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## Parameters

- `zones`: Possible values are:

## See Also

- [saveRecordZones](cloudkit.database/saverecordzones.md)
  Creates one or more zones in the database.
- [fetchAllRecordZones](cloudkit.database/fetchallrecordzones.md)
  Fetches all zones in the database.
- [deleteRecordZones](cloudkit.database/deleterecordzones.md)
  Deletes the specified zones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/fetchrecordzones)*