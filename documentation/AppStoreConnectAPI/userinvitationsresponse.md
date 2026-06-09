# UserInvitationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list pending App Store Connect team invitations.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object UserInvitationsResponse
```

## Properties

- `data` ([UserInvitation]) *(required)*: The resource data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.
- `included` ([App])

## See Also

- [List invited users](get-v1-userinvitations.md)
  Get a list of pending invitations to join your team.
- [object UserInvitation](userinvitation.md)
  A pending invitation for a person to join your App Store Connect team with a specified role and app access.
- [object UserInvitationCreateRequest](userinvitationcreaterequest.md)
  The request body you use to create a User Invitation.
- [object UserInvitationResponse](userinvitationresponse.md)
  The response body for endpoints that read or modify a pending App Store Connect team invitation.
- [object UserInvitationVisibleAppsLinkagesResponse](userinvitationvisibleappslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/userinvitationsresponse)*