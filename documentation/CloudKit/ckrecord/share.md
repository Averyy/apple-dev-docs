# share

**Framework**: Cloudkit  
**Kind**: property

A reference to the share object that determines the share status of the record.

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
@NSCopying
var share: CKRecord.Reference? { get }
```

#### Discussion

CloudKit clears this property’s value when it deletes the corresponding [`CKShare`](ckshare.md) object on the server. Send this record in the same batch operation as the share object you’re deleting, and this property updates accordingly.

CloudKit only supports sharing in zones with the `CKRecordZoneCapabilitySharing` capability. The default zone doesn’t support sharing.

If any records have a parent reference to this record, CloudKit implicitly shares them along with this record.

> **Note**:  Records in a hierarchy must only exist within one share. If a child record in a hierarchy already has a share reference, you get a `CKErrorAlreadyShared` error if you try to share any of that record’s parents.

## See Also

- [var parent: CKRecord.Reference?](ckrecord/parent.md)
  A reference to the record’s parent record.
- [CKRecord.Reference](ckrecord/reference.md)
  A relationship between two records in a record zone.
- [func setParent(CKRecord?)](ckrecord/setparent(_:)-23du1.md)
  Creates and sets a reference object for a parent from its record.
- [func setParent(CKRecord.ID?)](ckrecord/setparent(_:)-7egcx.md)
  Creates and sets a reference object for a parent from the parent’s record ID.
- [CKRecord.SystemFieldKey](ckrecord/systemfieldkey.md)
  Possible values for types of system field keys on records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/share)*