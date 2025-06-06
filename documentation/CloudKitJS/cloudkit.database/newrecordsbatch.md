# newRecordsBatch

**Framework**: CloudKit JS  
**Kind**: method

Creates records batch builder object for modifying multiple records.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
CloudKit.RecordsBatchBuilder newRecordsBatch(
	optional Object options
);
```

#### Return Value

A [`CloudKit.RecordsBatchBuilder`](cloudkit.recordsbatchbuilder.md) object for this database.

## Parameters

- `options`: A dictionary containing options to use when modifying records. Possible dictionary keys are:

## See Also

- [saveRecords](cloudkit.database/saverecords.md)
  Saves records to the database.
- [fetchRecords](cloudkit.database/fetchrecords.md)
  Fetches one or more records.
- [deleteRecords](cloudkit.database/deleterecords.md)
  Deletes one or more records.
- [performQuery](cloudkit.database/performquery.md)
  Fetches records by using a query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/newrecordsbatch)*