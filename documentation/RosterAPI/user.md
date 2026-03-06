# User

**Framework**: Roster API  
**Kind**: dictionary

A user in an Apple School Manager organization.

**Availability**:
- Roster API 1.0.0+

## Declaration

```swift
object User
```

## Properties

- `dateCreated` (string): The date the record was created in ASM, formatted in ISO 8601.
- `dateLastModified` (string): The date the user record was last modified in ASM, formatted in ISO 8601.
- `email` (email): The email address of the user. Not all student accounts have an email address.
- `familyName` (string): The user’s last name.
- `givenName` (string): The user’s first name.
- `grade` (string): If the user is a student, the user’s grade.
- `id` (string): A unique identifier for the user. Use it to request information for one user in the [`Read a user`](returns-a-specific-user-in-an-apple-school-manager-organization.md) endpoint.
- `middleName` (string): The user’s middle name.
- `roleLocationMapping` ([RoleLocation]): A list that maps between the user’s `roles` and the [`Location`](location.md) for each role.
- `roles` ([string]): A list of roles this user fills in the Apple School Manager organization. Possible values are `Student`, `Instructor`, and `Staff`.

## See Also

- [Read a user](returns-a-specific-user-in-an-apple-school-manager-organization.md)
  Read a user in an Apple School Manager organization.
- [object RoleLocation](rolelocation.md)
  A mapping between a role assumed by a user in an Apple School Manager organization, and the corresponding location.
- [List users](returns-a-list-of-users-in-an-apple-school-manager-organization.md)
  List users in an Apple School Manager organization.
- [List users in a class](returns-a-users-for-an-apple-school-manager-class.md)
  List users in a class of an Apple School Manager organization.
- [object Users](users.md)
  A list of users, with a token for pagination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/user)*