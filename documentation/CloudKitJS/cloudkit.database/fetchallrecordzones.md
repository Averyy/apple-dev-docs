# fetchAllRecordZones

**Framework**: CloudKit JS  
**Kind**: method  
**Role**: Instance Method

Fetches all zones in the database.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
Promise<CloudKit.RecordZonesResponse, CloudKit.CKError> fetchAllRecordZones();
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.RecordZonesResponse`](../cloudkit.recordzonesresponse.md) object or if it fails, a [`CKError`](../cloudkit/ckerror.md) object.

#### Discussion

See [Fetching Zones (zones/list)](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/GettingAllZones.html#//apple_ref/doc/uid/TP40015240-CH21) in [CloudKit Web Services Reference](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## See Also

### Accessing Record Zones
- [saveRecordZones](./saverecordzones.md)
  Creates one or more zones in the database.
- [fetchRecordZones](./fetchrecordzones.md)
  Fetches one or more zones.
- [deleteRecordZones](./deleterecordzones.md)
  Deletes the specified zones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/fetchallrecordzones)*