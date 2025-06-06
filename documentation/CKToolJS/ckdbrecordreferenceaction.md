# CKDBRecordReferenceAction

**Framework**: CKTool JS  
**Kind**: enum

An object that represents the action to be performed for the referenced record.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface CKDBRecordReferenceAction {
	const string NONE;
	const string DELETE_SELF;
	const string VALIDATE;
};
```

#### Overview

```javascript
import { CKDBRecordReferenceAction } from "@apple/cktool.database";
```

## Topics

### Enumeration Cases
- [DELETE_SELF](ckdbrecordreferenceaction/delete_self.md)
- [NONE](ckdbrecordreferenceaction/none.md)
- [VALIDATE](ckdbrecordreferenceaction/validate.md)

## See Also

- [CKDBPermissionType](ckdbpermissiontype.md)
  The participant’s read and write permissions.
- [CKDBQueryFilterType](ckdbqueryfiltertype.md)
  An object that represents the type of a filter that indicates the comparison operator when applying the filter.
- [CKDBQuerySortOrder](ckdbquerysortorder.md)
  An enumeration that represents the order to use when sorting records.
- [CKDBShareAcceptanceStatus](ckdbshareacceptancestatus.md)
  An enumeration that indicates the status of accepting the shared record.
- [CKDBShareParticipantType](ckdbshareparticipanttype.md)
  An enumeration that represents the type of a share participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecordreferenceaction)*