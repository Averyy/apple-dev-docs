# BetaTesterInvitation

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A pending email invitation sent to recruit someone as a TestFlight beta tester for an app.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```
object BetaTesterInvitation
```

## Properties

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `betaTesterInvitations`
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

### Objects
- [object BetaTesterInvitationCreateRequest](./betatesterinvitationcreaterequest.md)
  The request body you use to create a Beta Tester Invitation.
- [object BetaTesterInvitationResponse](./betatesterinvitationresponse.md)
  The response body for the endpoint that sends a TestFlight invitation to a beta tester.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betatesterinvitation)*