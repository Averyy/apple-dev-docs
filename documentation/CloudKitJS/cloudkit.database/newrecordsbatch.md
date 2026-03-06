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

- `options`: A dictionary containing options to use when modifying records. Possible dictionary keys are: | Key | Description |
| --- | --- |
| `zoneID` | A [`CloudKit.ZoneID`](cloudkit.zoneid.md) or zone name (`String`) that identifies the record zone in the database where you want to perform the operation. The default is the database default zone. |
| `desiredKeys` | An array of strings containing record field names that limits the amount of data returned in this operation. Only the fields specified in the array are returned. The default is `null`, which fetches all record fields. |
| `atomic` | A Boolean value indicating whether the entire operation fails when one or more operations fail. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) If `true`, the entire request fails if one operation fails. If `false`, some operations may succeed and others may fail. The default value is `false`. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) This property only applies to custom zones. |

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