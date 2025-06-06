# CKDBQueryFilterType

**Framework**: CKTool JS  
**Kind**: enum

An object that represents the type of a filter that indicates the comparison operator when applying the filter.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface CKDBQueryFilterType {
	const string EQUALS;
	const string NOT_EQUALS;
	const string LESS_THAN;
	const string LESS_THAN_OR_EQUALS;
	const string GREATER_THAN;
	const string GREATER_THAN_OR_EQUALS;
	const string NEAR;
	const string CONTAINS_ALL_TOKENS;
	const string IN;
	const string NOT_IN;
	const string CONTAINS_ANY_TOKENS;
	const string LIST_CONTAINS;
	const string LIST_NOT_CONTAINS;
	const string LIST_CONTAINS_ANY;
	const string LIST_NOT_CONTAINS_ANY;
	const string BEGINS_WITH;
	const string NOT_BEGINS_WITH;
	const string LIST_MEMBER_BEGINS_WITH;
	const string NOT_LIST_MEMBER_BEGINS_WITH;
	const string LIST_CONTAINS_ALL;
	const string NOT_LIST_CONTAINS_ALL;
};
```

#### Overview

```javascript
import { CKDBQueryFilterType } from "@apple/cktool.database";
```

## Topics

### Enumeration Cases
- [BEGINS_WITH](ckdbqueryfiltertype/begins_with.md)
- [CONTAINS_ALL_TOKENS](ckdbqueryfiltertype/contains_all_tokens.md)
- [CONTAINS_ANY_TOKENS](ckdbqueryfiltertype/contains_any_tokens.md)
- [EQUALS](ckdbqueryfiltertype/equals.md)
- [GREATER_THAN](ckdbqueryfiltertype/greater_than.md)
- [GREATER_THAN_OR_EQUALS](ckdbqueryfiltertype/greater_than_or_equals.md)
- [IN](ckdbqueryfiltertype/in.md)
- [LESS_THAN](ckdbqueryfiltertype/less_than.md)
- [LESS_THAN_OR_EQUALS](ckdbqueryfiltertype/less_than_or_equals.md)
- [LIST_CONTAINS](ckdbqueryfiltertype/list_contains.md)
- [LIST_CONTAINS_ALL](ckdbqueryfiltertype/list_contains_all.md)
- [LIST_CONTAINS_ANY](ckdbqueryfiltertype/list_contains_any.md)
- [LIST_MEMBER_BEGINS_WITH](ckdbqueryfiltertype/list_member_begins_with.md)
- [LIST_NOT_CONTAINS](ckdbqueryfiltertype/list_not_contains.md)
- [LIST_NOT_CONTAINS_ANY](ckdbqueryfiltertype/list_not_contains_any.md)
- [NEAR](ckdbqueryfiltertype/near.md)
- [NOT_BEGINS_WITH](ckdbqueryfiltertype/not_begins_with.md)
- [NOT_EQUALS](ckdbqueryfiltertype/not_equals.md)
- [NOT_IN](ckdbqueryfiltertype/not_in.md)
- [NOT_LIST_CONTAINS_ALL](ckdbqueryfiltertype/not_list_contains_all.md)
- [NOT_LIST_MEMBER_BEGINS_WITH](ckdbqueryfiltertype/not_list_member_begins_with.md)

## See Also

- [CKDBPermissionType](ckdbpermissiontype.md)
  The participant’s read and write permissions.
- [CKDBQuerySortOrder](ckdbquerysortorder.md)
  An enumeration that represents the order to use when sorting records.
- [CKDBRecordReferenceAction](ckdbrecordreferenceaction.md)
  An object that represents the action to be performed for the referenced record.
- [CKDBShareAcceptanceStatus](ckdbshareacceptancestatus.md)
  An enumeration that indicates the status of accepting the shared record.
- [CKDBShareParticipantType](ckdbshareparticipanttype.md)
  An enumeration that represents the type of a share participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbqueryfiltertype)*