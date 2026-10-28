# fetchRecordZoneChanges

**Framework**: CloudKit JS  
**Kind**: method  
**Role**: Instance Method

Fetch changes to the specified record zones in the database.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
Promise<CloudKit.RecordZoneChangesResponse, CloudKit.CKError> fetchRecordZoneChanges(
	CloudKit.RecordZoneChangesOptions|CloudKit.RecordZoneChangesOptions[] options
);
```

## Return Value

A `Promise` object that resolves to a [`CloudKit.RecordZoneChangesResponse`](../cloudkit.recordzonechangesresponse.md) object, or rejects to a [`CKError`](../cloudkit/ckerror.md) object.

## Discussion

Use the [`fetchDatabaseChanges`](./fetchdatabasechanges.md) method to get the zones that contain changed records.

## Parameters

- `options`: Specifies the zones and what data to fetch from each. If you want to fetch from multiple zones, pass an array containing a [`CloudKit.RecordZoneChangesOptions`](../cloudkit.recordzonechangesoptions.md) dictionary for each zone.

## See Also

### Fetching Changes
- [databaseScope](./databasescope.md)
  The type of database (public, private, or shared).
- [fetchDatabaseChanges](./fetchdatabasechanges.md)
  Fetch changed record zones in the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/fetchrecordzonechanges)*