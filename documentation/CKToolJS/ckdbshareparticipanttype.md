# CKDBShareParticipantType

**Framework**: CKTool JS  
**Kind**: enum

An enumeration that represents the type of a share participant.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface CKDBShareParticipantType {
	const string OWNER;
	const string ADMINISTRATOR;
	const string USER;
	const string PUBLIC_USER;
	const string UNKNOWN;
};
```

#### Overview

Possible values are `OWNER`, `ADMINISTRATOR`, `USER`, `PUBLIC_USER`, and `UNKNOWN`.

```javascript
import { CKDBShareParticipantType } from "@apple/cktool.database";
```

## Topics

### Enumeration Cases
- [ADMINISTRATOR](ckdbshareparticipanttype/administrator.md)
- [OWNER](ckdbshareparticipanttype/owner.md)
- [PUBLIC_USER](ckdbshareparticipanttype/public_user.md)
- [UNKNOWN](ckdbshareparticipanttype/unknown.md)
- [USER](ckdbshareparticipanttype/user.md)

## See Also

- [CKDBPermissionType](ckdbpermissiontype.md)
  The participant’s read and write permissions.
- [CKDBQueryFilterType](ckdbqueryfiltertype.md)
  An object that represents the type of a filter that indicates the comparison operator when applying the filter.
- [CKDBQuerySortOrder](ckdbquerysortorder.md)
  An enumeration that represents the order to use when sorting records.
- [CKDBRecordReferenceAction](ckdbrecordreferenceaction.md)
  An object that represents the action to be performed for the referenced record.
- [CKDBShareAcceptanceStatus](ckdbshareacceptancestatus.md)
  An enumeration that indicates the status of accepting the shared record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbshareparticipanttype)*