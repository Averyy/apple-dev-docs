# replace

**Framework**: CloudKit JS  
**Kind**: method

Replaces one or more records with the specified records.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
CloudKit.RecordsBatchBuilder replace(
	CloudKit.Record|CloudKit.Record[] records,
	optional Object options
);
```

#### Return Value

The object that received this method call.

#### Discussion

The fields whose values you do not specify are set to `null`.

## Parameters

- `records`: A   dictionary representing the replacement record, if you are replacing a single record. If you are replacing multiple records, this parameter is an array of replacement   dictionaries. The   dictionaries must contain the   key. Only the values of the fields in these dictionaries are replaced. The other field values are set to  .
- `options`: A dictionary containing options for this operation. This parameter contains a single   key that is an array of field names (  values). Only the fields specified in the array are set.

## See Also

- [forceReplace](cloudkit.recordsbatchbuilder/forcereplace.md)
  Replaces one or more records with the specified records regardless of conflicts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordsbatchbuilder/replace)*