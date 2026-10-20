# deleteRecordZones

**Framework**: CloudKit JS  
**Kind**: method  
**Role**: Instance Method

Deletes the specified zones.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
Promise<CloudKit.RecordZonesResponse, CloudKit.CKError> deleteRecordZones(
	CloudKit.ZoneID|CloudKit.ZoneID[]|String|String[] zones
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.RecordZonesResponse`](../cloudkit.recordzonesresponse.md) object if the operation succeeds; otherwise, a [`CKError`](../cloudkit/ckerror.md) object.

## Parameters

- `zones`: Possible values are:

  | Type | Description |
  | --- | --- |
  | [`CloudKit.ZoneID`](../cloudkit.zoneid.md) | A zone in the database to delete. |
  | `CloudKit.ZoneID[]` | An array of zones to delete. |
  | `String` | The name of a zone to delete. |
  | `String[]` | An array of names of zones to delete. |

## See Also

### Accessing Record Zones
- [saveRecordZones](./saverecordzones.md)
  Creates one or more zones in the database.
- [fetchRecordZones](./fetchrecordzones.md)
  Fetches one or more zones.
- [fetchAllRecordZones](./fetchallrecordzones.md)
  Fetches all zones in the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/deleterecordzones)*