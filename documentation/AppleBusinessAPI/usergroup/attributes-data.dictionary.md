# UserGroup.Attributes

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a user group resource.

**Availability**:
- Apple Business API 2.6+

## Declaration

```
object UserGroup.Attributes
```

## Overview

> **Note**: When additional attributes are added by Apple, they appear automatically, without requiring a newer version of the API.

## Properties

- `ouId` (string): The identifier of the organizational unit the group belongs to.
- `name` (string): The name of the user group.
- `type` (UserGroupType): The type of group. See [`UserGroupType`](../usergrouptype.md) for possible values.
- `totalMemberCount` (integer): The total number of members in the group.
- `status` (UserGroupStatus): The status of the group. See [`UserGroupStatus`](../usergroupstatus.md) for possible values.
- `createdDateTime` (date-time): The date and time the user group was created.
- `updatedDateTime` (date-time): The date and time the user group was last modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/usergroup/attributes-data.dictionary)*