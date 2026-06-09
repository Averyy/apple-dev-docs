# Users

**Framework**: App Store Connect API

Manage users on your App Store Connect team.

#### Overview

The `users` resource represents an App Store Connect user. You can change or delete users, but you cannot add them directly. To add users, create a `userInvitation`. App Store Connect adds the user to your team when they accept the invitation.

## Topics

### Getting User Information
- [List users](get-v1-users.md)
  Get a list of the users on your team.
- [Read user information](get-v1-users-_id_.md)
  Get information about a user on your team, such as name, roles, and app visibility.
### Modifying and Removing User Accounts
- [Modify a user account](patch-v1-users-_id_.md)
  Change a user’s role, app visibility information, or other account details.
- [Remove a user account](delete-v1-users-_id_.md)
  Remove a user from your team.
### Listing, Adding, and Removing App Access
- [List all apps visible to a user](get-v1-users-_id_-visibleapps.md)
  Get a list of apps that a user on your team can view.
- [Get all visible app resource ids for a user](get-v1-users-_id_-relationships-visibleapps.md)
  Get a list of app resource IDs to which a user on your team has access.
- [Add visible apps to a user](post-v1-users-_id_-relationships-visibleapps.md)
  Give a user on your team access to one or more apps.
- [Replace the list of visible apps for a user](patch-v1-users-_id_-relationships-visibleapps.md)
  Replace the list of apps a user on your team can see.
- [Remove visible apps from a user](delete-v1-users-_id_-relationships-visibleapps.md)
  Remove a user on your team’s access to one or more apps.
### Objects and Data Types
- [object User](user.md)
  A member of your App Store Connect team, with assigned roles and access to specific apps.
- [object UserUpdateRequest](userupdaterequest.md)
  The request body you use to update a User.
- [object UserResponse](userresponse.md)
  The response body for endpoints that read or modify a single App Store Connect team member.
- [object UsersResponse](usersresponse.md)
  A response containing a list of team members who have access to your App Store Connect account.
- [object UserVisibleAppsLinkagesRequest](uservisibleappslinkagesrequest.md)
  A request body you use to add or remove visible apps from a user.
- [object UserVisibleAppsLinkagesResponse](uservisibleappslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [type UserRole](userrole.md)
  A string that represents user roles and permissions in App Store Connect.

## See Also

- [User Invitations](user-invitations.md)
  Email invitations to join your App Store Connect team.
- [Sandbox Testers](sandbox-testers.md)
  Manage sandbox testers on your App Store Connect team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/users)*