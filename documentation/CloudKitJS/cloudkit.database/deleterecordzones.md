# deleteRecordZones

**Framework**: CloudKit JS  
**Kind**: method

Deletes the specified zones.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.RecordZonesResponse, CloudKit.CKError> deleteRecordZones(
	CloudKit.ZoneID|CloudKit.ZoneID[]|String|String[] zones
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.RecordZonesResponse`](cloudkit.recordzonesresponse.md) object if the operation succeeds; otherwise, a [`CKError`](cloudkit/ckerror.md) object.

## Parameters

- `zones`: Possible values are:

## See Also

- [saveRecordZones](cloudkit.database/saverecordzones.md)
  Creates one or more zones in the database.
- [fetchRecordZones](cloudkit.database/fetchrecordzones.md)
  Fetches one or more zones.
- [fetchAllRecordZones](cloudkit.database/fetchallrecordzones.md)
  Fetches all zones in the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/deleterecordzones)*