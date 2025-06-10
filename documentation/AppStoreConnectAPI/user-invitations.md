# User Invitations

**Framework**: App Store Connect API

Email invitations to join your App Store Connect team.

#### Overview

The `userInvitations` resource represents users who have been invited to join a team in App Store Connect. When you create a user invitation the user receives an email with a link to activate an account and connect it to their Apple Account.

If the user accepts the invitation, the user is added to the team and the invitation is deleted. User invitations expire after three days.

You can also get a list of all invited users, read the invite information of a single user, and find out which apps an invited user can test.

## Topics

### Getting Invited Users
- [List Invited Users](get-v1-userinvitations.md)
  Get a list of pending invitations to join your team.
- [Read User Invitation Information](get-v1-userinvitations-_id_.md)
  Get information about a pending invitation to join your team.
### Sending and Canceling Invitations
- [Invite a User](post-v1-userinvitations.md)
  Invite a user with assigned user roles to join your team.
- [Cancel a User Invitation](delete-v1-userinvitations-_id_.md)
  Cancel a pending invitation for a user to join your team.
### Getting Visible Apps
- [List All Apps Visible to an Invited User](get-v1-userinvitations-_id_-visibleapps.md)
  Get a list of apps that will be visible to a user with a pending invitation.
- [GET /v1/userInvitations/{id}/relationships/visibleApps](get-v1-userinvitations-_id_-relationships-visibleapps.md)
### Objects
- [object UserInvitation](userinvitation.md)
  The data structure that represents a User Invitations resource.
- [object UserInvitationCreateRequest](userinvitationcreaterequest.md)
  The request body you use to create a User Invitation.
- [object UserInvitationResponse](userinvitationresponse.md)
  A response that contains a single User Invitations resource.
- [object UserInvitationsResponse](userinvitationsresponse.md)
  A response that contains a list of User Invitations resources.
- [object UserInvitationVisibleAppsLinkagesResponse](userinvitationvisibleappslinkagesresponse.md)

## See Also

- [Users](users.md)
  Manage users on your App Store Connect team.
- [Sandbox Testers](sandbox-testers.md)
  Manage sandbox testers on your App Store Connect team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/user-invitations)*