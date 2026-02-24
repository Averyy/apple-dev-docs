# RosterPerson

**Framework**: Device Management  
**Kind**: dictionary

A person’s properties and their values.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RosterPerson
```

## Properties

- `email_address` (string): The email address of the person that Apple School Manager (ASM) displays. Available in X-Protocol version 5 and later.
- `first_name` (string): The person’s first (given) name. Maximum length iw 1024 UTF-8 characters. Available in protocol version 3 and later.
- `grade` (string): The grade information for the student. Maximum length is 256 UTF-8 characters. Value can be null. Not used for instructors.
- `is_federated_auth` (boolean): If `true`, the system enables federated authentication for the person from an external identity provider. Available in X-Protocol version 6 and later.
- `last_name` (string): The person’s last name. Maximum length is 1024 UTF-8 characters. Available in protocol version 3 and later.
- `managed_apple_id` (string): The Managed Apple Account for the person. Maximum length is 1024 UTF-8 characters.
- `middle_name` (string): The person’s middle name. Maximum length is 1024 UTF-8 characters. Available in protocol version 3 and later.
- `name` (string): The person’s name. Maximum length is 1024 UTF-8 characters.
- `op_date` (string): The time stamp, in iSO 8601 format, when the system added, updated, or deleted the person.
- `passcode_type` (string): The password policy of the person. Possible values are `complex`, `four`, or `six`. Available in protocol version 3 and later.
- `person_id` (string): The `personid` of the person that ASM displays. Available in X-Protocol version 4 and later.
- `sis_username` (string): The SIS `username` of the person that ASM displays. Available in X-Protocol version 5 and later.
- `source` (string): The creation data source of the class.
- `source_system_identifier` (string): The identifier that the organization configures for the person. Maximum length is 256 UTF-8 characters.
- `status` (string): The status of the person. Possible values are `Active,` `InActive,` `FailedPasswordLocked`, and `AtoLocked`. `AtoLocked` indicates that the system detects account take over and temporarily locks the person until an authentic user claims it. Available in X-Protocol version 3 and later.
- `unique_identifier` (string): The unique identifier for the person. Maximum length 256 UTF-8 characters.

## See Also

- [Get the List of People](fetch-person-roster.md)
  Obtain a list of people the server manages, across the organization.
- [Sync the List of People](fetch-person-roster-sync.md)
  Get updates about the list of people the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rosterperson)*