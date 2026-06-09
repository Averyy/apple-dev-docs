# BetaTesterInvitationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for the endpoint that sends a TestFlight invitation to a beta tester.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaTesterInvitationResponse
```

## Properties

- `data` (BetaTesterInvitation) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [Send an invitation to a beta tester](post-v1-betatesterinvitations.md)
  Send or resend an invitation to a beta tester to test a specified app.
- [object BetaTesterInvitation](betatesterinvitation.md)
  A pending email invitation sent to recruit someone as a TestFlight beta tester for an app.
- [object BetaTesterInvitationCreateRequest](betatesterinvitationcreaterequest.md)
  The request body you use to create a Beta Tester Invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betatesterinvitationresponse)*