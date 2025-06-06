# fetchRecords

**Framework**: CloudKit JS  
**Kind**: method

Fetches one or more records.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.RecordsResponse, CloudKit.CKError> fetchRecords(
	CloudKit.Record|CloudKit.Record[]|String|String[] records,
	optional Object options
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.RecordsResponse`](cloudkit.recordsresponse.md) object if the operation succeeds; otherwise, a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

To get the fetched record, use the [`records`](cloudkit.recordsresponse/records.md) property in the [`CloudKit.RecordsResponse`](cloudkit.recordsresponse.md) class.

```javascript
database.fetchRecords('115').then(function(response) {
    if (response.hasErrors) {
        // Insert error handling
        throw response.errors[0];
    } else {
        // Insert successfully fetched record
        var fetchedRecord = response.records[0];
    }
});
```

Similar to the [`saveRecords`](cloudkit.database/saverecords.md) method, if you don’t specify a zone ID in the `options` parameter, the records are fetched from the default zone. To fetch records from a specific zone, pass a dictionary with the `zoneID` key set to the name of your zone.

```javascript
database.fetchRecords('115', { zoneID: 'myZone' }).then(function(response) {
    // …
}
```

## Parameters

- `records`: Possible values are:
- `options`: A dictionary containing options to use when fetching records. Possible dictionary keys are:

## See Also

- [saveRecords](cloudkit.database/saverecords.md)
  Saves records to the database.
- [deleteRecords](cloudkit.database/deleterecords.md)
  Deletes one or more records.
- [performQuery](cloudkit.database/performquery.md)
  Fetches records by using a query.
- [newRecordsBatch](cloudkit.database/newrecordsbatch.md)
  Creates records batch builder object for modifying multiple records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/fetchrecords)*