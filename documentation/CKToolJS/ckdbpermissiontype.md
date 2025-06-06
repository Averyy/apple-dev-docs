# CKDBPermissionType

**Framework**: CKTool JS  
**Kind**: enum

The participant’s read and write permissions.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface CKDBPermissionType {
	const string NONE;
	const string READ_ONLY;
	const string READ_WRITE;
	const string UNKNOWN;
};
```

#### Overview

Possible values are `NONE`, `READ_ONLY`, `READ_WRITE`, and `UNKNOWN`.

```javascript
import { CKDBPermissionType } from "@apple/cktool.database";
```

## Topics

### Enumeration Cases
- [NONE](ckdbpermissiontype/none.md)
- [READ_ONLY](ckdbpermissiontype/read_only.md)
- [READ_WRITE](ckdbpermissiontype/read_write.md)
- [UNKNOWN](ckdbpermissiontype/unknown.md)

## See Also

- [CKDBQueryFilterType](ckdbqueryfiltertype.md)
  An object that represents the type of a filter that indicates the comparison operator when applying the filter.
- [CKDBQuerySortOrder](ckdbquerysortorder.md)
  An enumeration that represents the order to use when sorting records.
- [CKDBRecordReferenceAction](ckdbrecordreferenceaction.md)
  An object that represents the action to be performed for the referenced record.
- [CKDBShareAcceptanceStatus](ckdbshareacceptancestatus.md)
  An enumeration that indicates the status of accepting the shared record.
- [CKDBShareParticipantType](ckdbshareparticipanttype.md)
  An enumeration that represents the type of a share participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbpermissiontype)*