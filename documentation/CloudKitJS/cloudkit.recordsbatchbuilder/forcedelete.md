# forceDelete

**Framework**: CloudKit JS  
**Kind**: method

Deletes one or more records regardless of conflicts.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
RecordsBatchBuilder forceDelete(
	CloudKit.Record|CloudKit.Record[] records
);
```

#### Return Value

The object that received this method call.

## Parameters

- `records`: A   dictionary representing the record to delete, if you are deleting a single record. If you are deleting multiple records, this parameter is an array of   dictionaries. The   key is not required in the   dictionaries.

## See Also

- [delete](cloudkit.recordsbatchbuilder/delete.md)
  Deletes one or more records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordsbatchbuilder/forcedelete)*