# saveRecordZones

**Framework**: CloudKit JS  
**Kind**: method  
**Role**: Instance Method

Creates one or more zones in the database.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
Promise<CloudKit.RecordZonesResponse, CloudKit.CKError> saveRecordZones(
	CloudKit.ZoneID|CloudKit.ZoneID[]|String|String[] zones
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.RecordZonesResponse`](../cloudkit.recordzonesresponse.md) object if the operation succeeds; otherwise, a [`CKError`](../cloudkit/ckerror.md) object.

#### Discussion

See [Modifying Zones (zones/modify)](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/ModifyZones.html#//apple_ref/doc/uid/TP40015240-CH10) in [CloudKit Web Services Reference](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## Parameters

- `zones`: Possible values are:

  | Type | Description |
  | --- | --- |
  | [`CloudKit.ZoneID`](../cloudkit.zoneid.md) | A zone in the database to save. |
  | `CloudKit.ZoneID[]` | An array of zones to save. |
  | `String` | The name of a zone to save. |
  | `String[]` | An array of names of zones to save. |

## See Also

### Accessing Record Zones
- [fetchRecordZones](./fetchrecordzones.md)
  Fetches one or more zones.
- [fetchAllRecordZones](./fetchallrecordzones.md)
  Fetches all zones in the database.
- [deleteRecordZones](./deleterecordzones.md)
  Deletes the specified zones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/saverecordzones)*