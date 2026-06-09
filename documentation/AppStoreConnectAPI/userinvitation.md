# UserInvitation

**Framework**: App Store Connect API  
**Kind**: dictionary

A pending invitation for a person to join your App Store Connect team with a specified role and app access.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object UserInvitation
```

## Topics

### Objects
- [object UserInvitation.Attributes](userinvitation/attributes-data.dictionary.md)
  Attributes that describe a User Invitations resource.
- [object UserInvitation.Relationships](userinvitation/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (UserInvitation.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (UserInvitation.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [object UserInvitationCreateRequest](userinvitationcreaterequest.md)
  The request body you use to create a User Invitation.
- [object UserInvitationResponse](userinvitationresponse.md)
  The response body for endpoints that read or modify a pending App Store Connect team invitation.
- [object UserInvitationsResponse](userinvitationsresponse.md)
  The response body for endpoints that list pending App Store Connect team invitations.
- [object UserInvitationVisibleAppsLinkagesResponse](userinvitationvisibleappslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/userinvitation)*