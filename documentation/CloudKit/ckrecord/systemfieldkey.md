# CKRecord.SystemFieldKey

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Possible values for types of system field keys on records.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
enum SystemFieldKey
```

#### Overview

Use the values [`share`](./systemfieldkey/share.md) and [`parent`](./systemfieldkey/parent.md) when creating an [`NSPredicate`](../../Foundation/nspredicate.md) for a [`CKQuery`](../ckquery.md) to reference a record’s [`share`](./share.md) or [`parent`](./parent.md) property, respectively.

## Topics

### Types of Shared Records
- [static let parent: CKRecord.FieldKey](./systemfieldkey/parent.md)
  The key constant that a record uses for its CKRecord.parent.
- [static let share: CKRecord.FieldKey](./systemfieldkey/share.md)
  The key constant that a record uses for its CKRecord.share.
### Type Properties
- [static var creationDate: CKRecord.FieldKey](./systemfieldkey/creationdate.md)
  A key constant that a record uses for its CKRecord.creationDate.
- [static var creatorUserRecordID: CKRecord.FieldKey](./systemfieldkey/creatoruserrecordid.md)
  A key constant that a record uses for its CKRecord.creatorUserRecordID.
- [static var lastModifiedUserRecordID: CKRecord.FieldKey](./systemfieldkey/lastmodifieduserrecordid.md)
  A key constant that a record uses for its CKRecord.lastModifiedUserRecordID.
- [static var modificationDate: CKRecord.FieldKey](./systemfieldkey/modificationdate.md)
  A key constant that a record uses for its CKRecord.modificationDate.
- [static var recordID: CKRecord.FieldKey](./systemfieldkey/recordid.md)
  A key constant that a record uses for its CKRecord.recordID.

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
- [func setParent(CKRecord.ID?)](./setparent%28_%29-7egcx.md)
  Creates and sets a reference object for a parent from the parent’s record ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/systemfieldkey)*