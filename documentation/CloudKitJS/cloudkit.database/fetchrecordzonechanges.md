# fetchRecordZoneChanges

**Framework**: CloudKit JS  
**Kind**: method

Fetch changes to the specified record zones in the database.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.RecordZoneChangesResponse, CloudKit.CKError> fetchRecordZoneChanges(
	CloudKit.RecordZoneChangesOptions|CloudKit.RecordZoneChangesOptions[] options
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.RecordZoneChangesResponse`](cloudkit.recordzonechangesresponse.md) object, or rejects to a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

Use the [`fetchDatabaseChanges`](cloudkit.database/fetchdatabasechanges.md) method to get the zones that contain changed records.

## Parameters

- `options`: Specifies the zones and what data to fetch from each. If you want to fetch from multiple zones, pass an array containing a   dictionary for each zone.

## See Also

- [databaseScope](cloudkit.database/databasescope.md)
  The type of database (public, private, or shared).
- [fetchDatabaseChanges](cloudkit.database/fetchdatabasechanges.md)
  Fetch changed record zones in the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/fetchrecordzonechanges)*