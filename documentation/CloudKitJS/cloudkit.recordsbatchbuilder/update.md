# update

**Framework**: CloudKit JS  
**Kind**: method

Updates one or more existing records.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
CloudKit.RecordsBatchBuilder update(
	CloudKit.Record|CloudKit.Record[] records,
	optional Object options
);
```

#### Return Value

The object that received this method call.

## Parameters

- `records`: A   dictionary representing the fields of the record you want to update, if you are updating a single record. If you are updating multiple records, this parameter is an array of   dictionaries. The   dictionaries need to contain the   key. Only the values of the fields in these dictionaries are updated.
- `options`: A dictionary containing options for this operation. This parameter contains a single   key that is an array of field names (  values). Only the fields specified in the array are set.

## See Also

- [create](cloudkit.recordsbatchbuilder/create.md)
  Creates one or more records.
- [createOrUpdate](cloudkit.recordsbatchbuilder/createorupdate.md)
  Creates or updates one or more records depending on the information provided.
- [forceUpdate](cloudkit.recordsbatchbuilder/forceupdate.md)
  Updates one or more existing records regardless of conflicts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordsbatchbuilder/update)*