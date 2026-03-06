# forceReplace

**Framework**: CloudKit JS  
**Kind**: method

Replaces one or more records with the specified records regardless of conflicts.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
CloudKit.RecordsBatchBuilder forceReplace(
	CloudKit.Record|CloudKit.Record[] records,
	optional Object options
);
```

#### Return Value

The object that received this method call.

#### Discussion

Creates records if they don’t exist.

## Parameters

- `records`: A [`CloudKit.Record`](cloudkit.record.md) dictionary representing the replacement record, if you are replacing a single record. If you are replacing multiple records, this value is an array of replacement [`CloudKit.Record`](cloudkit.record.md) dictionaries. The `recordChangeTag` key is not required in the [`CloudKit.Record`](cloudkit.record.md) dictionaries. Only the values of the fields in these dictionaries are replaced. The other field values are set to `null`.
- `options`: A dictionary containing options for this operation. This parameter contains a single `desiredKeys` key that is an array of field names (`String` values). Only the fields specified in the array are set.

## See Also

- [replace](cloudkit.recordsbatchbuilder/replace.md)
  Replaces one or more records with the specified records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordsbatchbuilder/forcereplace)*