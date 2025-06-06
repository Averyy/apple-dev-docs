# saveRecordZones

**Framework**: CloudKit JS  
**Kind**: method

Creates one or more zones in the database.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.RecordZonesResponse, CloudKit.CKError> saveRecordZones(
	CloudKit.ZoneID|CloudKit.ZoneID[]|String|String[] zones
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.RecordZonesResponse`](cloudkit.recordzonesresponse.md) object if the operation succeeds; otherwise, a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

See [`Modifying Zones (zones/modify)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/ModifyZones.html#//apple_ref/doc/uid/TP40015240-CH10) in [`CloudKit Web Services Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## Parameters

- `zones`: Possible values are:

## See Also

- [fetchRecordZones](cloudkit.database/fetchrecordzones.md)
  Fetches one or more zones.
- [fetchAllRecordZones](cloudkit.database/fetchallrecordzones.md)
  Fetches all zones in the database.
- [deleteRecordZones](cloudkit.database/deleterecordzones.md)
  Deletes the specified zones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/saverecordzones)*