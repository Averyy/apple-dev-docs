# CKRecord.SystemFieldKey

**Framework**: CloudKit  
**Kind**: enum

Possible values for types of system field keys on records.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
enum SystemFieldKey
```

#### Overview

Use the values [`share`](ckrecord/systemfieldkey/share.md) and [`parent`](ckrecord/systemfieldkey/parent.md) when creating an [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate) for a [`CKQuery`](ckquery.md) to reference a record’s [`share`](ckrecord/share.md) or [`parent`](ckrecord/parent.md) property, respectively.

## Topics

### Types of Shared Records
- [static let parent: CKRecord.FieldKey](ckrecord/systemfieldkey/parent.md)
  A value that represents the parent property of a record.
- [static let share: CKRecord.FieldKey](ckrecord/systemfieldkey/share.md)
  A value that represents the share property of a record.
### Type Properties
- [static var creationDate: CKRecord.FieldKey](ckrecord/systemfieldkey/creationdate.md)
- [static var creatorUserRecordID: CKRecord.FieldKey](ckrecord/systemfieldkey/creatoruserrecordid.md)
- [static var lastModifiedUserRecordID: CKRecord.FieldKey](ckrecord/systemfieldkey/lastmodifieduserrecordid.md)
- [static var modificationDate: CKRecord.FieldKey](ckrecord/systemfieldkey/modificationdate.md)
- [static var recordID: CKRecord.FieldKey](ckrecord/systemfieldkey/recordid.md)

## See Also

- [var parent: CKRecord.Reference?](ckrecord/parent.md)
  A reference to the record’s parent record.
- [var share: CKRecord.Reference?](ckrecord/share.md)
  A reference to the share object that determines the share status of the record.
- [CKRecord.Reference](ckrecord/reference.md)
  A relationship between two records in a record zone.
- [func setParent(CKRecord?)](ckrecord/setparent(_:)-23du1.md)
  Creates and sets a reference object for a parent from its record.
- [func setParent(CKRecord.ID?)](ckrecord/setparent(_:)-7egcx.md)
  Creates and sets a reference object for a parent from the parent’s record ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/systemfieldkey)*