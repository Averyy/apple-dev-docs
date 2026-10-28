# setParent(_:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setParentReferenceFromRecordID:(CKRecordID *) parentRecordID;
```

## Discussion

This method creates and sets a [`CKRecord.Reference`](./reference.md) object that points to the record you provide. The resulting `CKReference` has an action of [`CKRecord.ReferenceAction.none`](./referenceaction/none.md).

## Parameters

- `parentRecordID`: The [`CKRecord.ID`](./id.md) object for the record that you want to set as this record’s parent.

## See Also

### Sharing Records
- [var parent: CKRecord.Reference?](./parent.md)
  A reference to the record’s parent record.
- [var share: CKRecord.Reference?](./share.md)
  A reference to the share object that determines the share status of the record.
- [CKRecord.Reference](./reference.md)
  A relationship between two records in a record zone.
- [func setParent(CKRecord?)](./setparent%28_%29-23du1.md)
  Creates and sets a reference object for a parent from its record.
- [CKRecord.SystemFieldKey](./systemfieldkey.md)
  Possible values for types of system field keys on records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/setparent(_:)-7egcx)*