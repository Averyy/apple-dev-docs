# create

**Framework**: CloudKit JS  
**Kind**: method

Creates one or more records.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
CloudKit.RecordsBatchBuilder create(
	CloudKit.Record|CloudKit.Record[] records,
	optional Object options
);
```

#### Return Value

The object that received this method call.

## Parameters

- `records`: A   dictionary representing the record to create, if you are creating a single record. If you are creating multiple records, this parameter is an array of   dictionaries representing the records to create. Only the values of the fields in the dictionaries are set.
- `options`: A dictionary containing options for this operation. This parameter contains a single   key that is an array of field names (  values). Only the fields specified in the array are set.

## See Also

- [createOrUpdate](cloudkit.recordsbatchbuilder/createorupdate.md)
  Creates or updates one or more records depending on the information provided.
- [update](cloudkit.recordsbatchbuilder/update.md)
  Updates one or more existing records.
- [forceUpdate](cloudkit.recordsbatchbuilder/forceupdate.md)
  Updates one or more existing records regardless of conflicts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordsbatchbuilder/create)*