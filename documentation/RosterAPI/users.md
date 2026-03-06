# Users

**Framework**: Roster API  
**Kind**: dictionary

A list of users, with a token for pagination.

**Availability**:
- Roster API 1.0.0+

## Declaration

```swift
object Users
```

## Properties

- `moreToFollow` (boolean): A flag that indicates whether there are more users. If `true`, use the `nextPageToken` to request another list from the remaining users.
- `nextPageToken` (string): A token to request additional users, if any. Use this as the `nextPageToken` parameter for the [`List users`](returns-a-list-of-users-in-an-apple-school-manager-organization.md) request.
- `users` ([User]): A list of [`User`](user.md) objects.

## See Also

- [Read a user](returns-a-specific-user-in-an-apple-school-manager-organization.md)
  Read a user in an Apple School Manager organization.
- [object User](user.md)
  A user in an Apple School Manager organization.
- [object RoleLocation](rolelocation.md)
  A mapping between a role assumed by a user in an Apple School Manager organization, and the corresponding location.
- [List users](returns-a-list-of-users-in-an-apple-school-manager-organization.md)
  List users in an Apple School Manager organization.
- [List users in a class](returns-a-users-for-an-apple-school-manager-class.md)
  List users in a class of an Apple School Manager organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/users)*