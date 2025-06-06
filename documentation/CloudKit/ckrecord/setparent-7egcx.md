# setParent(_:)

**Framework**: CloudKit  
**Kind**: method

Creates and sets a reference object for a parent from the parent’s record ID.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func setParent(_ parentRecordID: CKRecord.ID?)
```

#### Discussion

This method creates and sets a [`CKRecord.Reference`](ckrecord/reference.md) object that points to the record you provide. The resulting `CKReference` has an action of [`CKRecord.ReferenceAction.none`](ckrecord/referenceaction/none.md).

## Parameters

- `parentRecordID`: The   object for the record that you want to set as this record’s parent.

## See Also

- [var parent: CKRecord.Reference?](ckrecord/parent.md)
  A reference to the record’s parent record.
- [var share: CKRecord.Reference?](ckrecord/share.md)
  A reference to the share object that determines the share status of the record.
- [CKRecord.Reference](ckrecord/reference.md)
  A relationship between two records in a record zone.
- [func setParent(CKRecord?)](ckrecord/setparent(_:)-23du1.md)
  Creates and sets a reference object for a parent from its record.
- [CKRecord.SystemFieldKey](ckrecord/systemfieldkey.md)
  Possible values for types of system field keys on records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/setparent(_:)-7egcx)*