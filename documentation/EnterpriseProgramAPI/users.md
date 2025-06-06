# Users

**Framework**: Enterprise Program API

Manage users on your Enterprise Program team.

#### Overview

The `users` resource represents an Enteprise Program user. You can change or delete users, but you cannot add them directly. To add users, create a `userInvitation`. The [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com) adds the user to your team when they accept the invitation.

## Topics

### Getting User Information
- [List Users](list-users.md)
  Get a list of the users on your team.
- [Read User Information](read-user-information.md)
  Get information about a user on your team, such as name, roles, and app visibility.
### Modifying and Removing User Accounts
- [Modify a User Account](modify-a-user-account.md)
  Change a user’s role, app visibility information, or other account details.
- [Delete a User Account](delete-a-user-account.md)
  Remove a user from your team.
### Objects and Data Types
- [object User](user.md)
  The data structure that represents a Users resource.
- [object UserUpdateRequest](userupdaterequest.md)
  The request body you use to update a User.
- [object UserResponse](userresponse.md)
  A response that contains a single Users resource.
- [object UsersResponse](usersresponse.md)
  A response that contains a list of Users resources.
- [type UserRole](userrole.md)
  Strings that represent user roles and permissions in the Apple Developer website.

## See Also

- [User Invitations](user-invitations.md)
  Email invitations to join your Enterprise Program team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/users)*