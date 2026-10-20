# UserInvitationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that read or modify a pending App Store Connect team invitation.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```
object UserInvitationResponse
```

## Properties

- `data` (UserInvitation) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.
- `included` ([App])

## See Also

### Related Documentation
- [Invite a user](./post-v1-userinvitations.md)
  Invite a user with assigned user roles to join your team.
### Objects
- [object UserInvitation](./userinvitation.md)
  A pending invitation for a person to join your App Store Connect team with a specified role and app access.
- [object UserInvitationCreateRequest](./userinvitationcreaterequest.md)
  The request body you use to create a User Invitation.
- [object UserInvitationsResponse](./userinvitationsresponse.md)
  The response body for endpoints that list pending App Store Connect team invitations.
- [object UserInvitationVisibleAppsLinkagesResponse](./userinvitationvisibleappslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/userinvitationresponse)*