# delete

**Framework**: CloudKit JS  
**Kind**: method

Deletes one or more records.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
CloudKit.RecordsBatchBuilder delete(
	CloudKit.Record|CloudKit.Record[] records
);
```

#### Return Value

The object that received this method call.

## Parameters

- `records`: A   dictionary representing the record to delete, if you are deleting a single record. If you are deleting multiple records, this parameter is an array of   dictionaries. The   dictionaries need to contain the   key.

## See Also

- [forceDelete](cloudkit.recordsbatchbuilder/forcedelete.md)
  Deletes one or more records regardless of conflicts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordsbatchbuilder/delete)*