# User.Attributes

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a user resource.

**Availability**:
- Apple Business API 2.6+

## Declaration

```
object User.Attributes
```

#### Overview

> **Note**: When additional attributes are added by Apple, they appear automatically, without requiring a newer version of the API.

## Properties

- `firstName` (string): The first name of the user.
- `middleName` (string): The middle name of the user.
- `lastName` (string): The last name of the user.
- `status` (UserStatus): The status of the user. See [`UserStatus`](../userstatus.md) for possible values.
- `managedAppleAccount` (string): The Apple Account of the user registered in the system.
- `isExternalUser` (boolean): Indicates if the user is an external user invited to the organization.
- `roleOuList` ([UserRoleOuMapping]): A list of role-organizational unit mappings for the user, where each item contains a `roleName` and `ouId` representing the role of a user at a particular organizational unit.
- `email` (string): The email address of the user.
- `employeeNumber` (string): The employee number of the user.
- `costCenter` (string): The cost center the user belongs to in the organization.
- `division` (string): The division the user belongs to in the organization.
- `department` (string): The department the user belongs to in the organization.
- `jobTitle` (string): The job title the user holds in the organization.
- `phoneNumbers` ([UserPhoneNumber]): The phone numbers of the user.
- `startDateTime` (date-time): The date and time when the user started as part of the organization.
- `createdDateTime` (date-time): The date and time that the user was created.
- `updatedDateTime` (date-time): The date and time that the user was last updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/user/attributes-data.dictionary)*