# deleteRecords

**Framework**: CloudKit JS  
**Kind**: method

Deletes one or more records.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.RecordsResponse, CloudKit.CKError> deleteRecords(
	CloudKit.Record|CloudKit.Record[]|String|String[] records,
	optional Object options
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.RecordsResponse`](cloudkit.recordsresponse.md) object if the operation succeeds; otherwise, a [`CKError`](cloudkit/ckerror.md) object.

## Parameters

- `records`: Possible values are:
- `options`: A dictionary containing a single   key that identifies the zone ( ) in the database where the record resides. If the   parameter is omitted, the default zone is used.

## See Also

- [saveRecords](cloudkit.database/saverecords.md)
  Saves records to the database.
- [fetchRecords](cloudkit.database/fetchrecords.md)
  Fetches one or more records.
- [performQuery](cloudkit.database/performquery.md)
  Fetches records by using a query.
- [newRecordsBatch](cloudkit.database/newrecordsbatch.md)
  Creates records batch builder object for modifying multiple records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/deleterecords)*