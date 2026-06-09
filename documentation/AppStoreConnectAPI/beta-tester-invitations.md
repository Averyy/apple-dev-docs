# Beta Tester Invitations

**Framework**: App Store Connect API

Requests to send or resend an email inviting a beta tester to test an app.

#### Overview

A `betaTesterInvitations` resource has a single purpose: to resend an email inviting an existing beta tester to test an app. When the app is ready to test, TestFlight sends invitations to users when you add them to builds or beta groups. You can use the `betaTesterInvitations` resource to resend an invitation, or, if you disable automatic notifications, to send the invitation for the first time.

## Topics

### Resending Invitations
- [Send an invitation to a beta tester](post-v1-betatesterinvitations.md)
  Send or resend an invitation to a beta tester to test a specified app.
### Objects
- [object BetaTesterInvitation](betatesterinvitation.md)
  A pending email invitation sent to recruit someone as a TestFlight beta tester for an app.
- [object BetaTesterInvitationCreateRequest](betatesterinvitationcreaterequest.md)
  The request body you use to create a Beta Tester Invitation.
- [object BetaTesterInvitationResponse](betatesterinvitationresponse.md)
  The response body for the endpoint that sends a TestFlight invitation to a beta tester.

## See Also

- [Beta Testers](beta-testers.md)
  People who can install and test prerelease builds.
- [Beta recruitment criteria](beta-recruitment-criteria.md)
  Create public links that accept testers with specific device and OS combinations.
- [Beta Groups](beta-groups.md)
  Groups of beta testers that have access to one or more builds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-tester-invitations)*