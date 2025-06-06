# Users

**Framework**: App Store Connect API

Manage users on your App Store Connect team.

#### Overview

The `users` resource represents an App Store Connect user. You can change or delete users, but you cannot add them directly. To add users, create a `userInvitation`. App Store Connect adds the user to your team when they accept the invitation.

## Topics

### Getting User Information
- [List Users](get-v1-users.md)
  Get a list of the users on your team.
- [Read User Information](get-v1-users-_id_.md)
  Get information about a user on your team, such as name, roles, and app visibility.
### Modifying and Removing User Accounts
- [Modify a User Account](patch-v1-users-_id_.md)
  Change a user’s role, app visibility information, or other account details.
- [Remove a User Account](delete-v1-users-_id_.md)
  Remove a user from your team.
### Listing, Adding, and Removing App Access
- [List All Apps Visible to a User](get-v1-users-_id_-visibleapps.md)
  Get a list of apps that a user on your team can view.
- [Get All Visible App Resource IDs for a User](get-v1-users-_id_-relationships-visibleapps.md)
  Get a list of app resource IDs to which a user on your team has access.
- [Add Visible Apps to a User](post-v1-users-_id_-relationships-visibleapps.md)
  Give a user on your team access to one or more apps.
- [Replace the List of Visible Apps for a User](patch-v1-users-_id_-relationships-visibleapps.md)
  Replace the list of apps a user on your team can see.
- [Remove Visible Apps from a User](delete-v1-users-_id_-relationships-visibleapps.md)
  Remove a user on your team’s access to one or more apps.
### Objects and Data Types
- [object User](user.md)
  The data structure that represents a Users resource.
- [object UserUpdateRequest](userupdaterequest.md)
  The request body you use to update a User.
- [object UserResponse](userresponse.md)
  A response that contains a single Users resource.
- [object UsersResponse](usersresponse.md)
  A response that contains a list of Users resources.
- [object UserVisibleAppsLinkagesRequest](uservisibleappslinkagesrequest.md)
  A request body you use to add or remove visible apps from a user.
- [object UserVisibleAppsLinkagesResponse](uservisibleappslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [type UserRole](userrole.md)
  Strings that represent user roles and permissions in App Store Connect.

## See Also

- [User Invitations](user-invitations.md)
  Email invitations to join your App Store Connect team.
- [Sandbox Testers](sandbox-testers.md)
  Manage sandbox testers on your App Store Connect team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/users)*