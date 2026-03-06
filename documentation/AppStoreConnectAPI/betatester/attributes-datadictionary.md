# BetaTester.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a beta tester resource.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaTester.Attributes
```

## Mentions

- [App Store Connect API 3.5 release notes](app-store-connect-api-3-5-release-notes.md)
- [App Store Connect API 4.2 release notes](app-store-connect-api-4-2-release-notes.md)

## Topics

### Generated dictionaries
- [object BetaTester.Attributes.AppDevices](betatester/attributes-data.dictionary/appdevices-data.dictionary.md)
  Information about devices used by the beta tester.

## Properties

- `appDevices` ([BetaTester.Attributes.AppDevices])
- `email` (email): The beta tester’s email address, used for sending beta testing invitations.
- `firstName` (string): The beta tester’s first name.
- `inviteType` (BetaInviteType): An invite type that indicates if a beta tester was invited by an email invite or used a TestFlight public link to join a beta test.
- `lastName` (string): The beta tester’s last name.
- `state` (BetaTesterState): The status of a beta tester.

## See Also

- [Beta Testers](beta-testers.md)
  People who can install and test prerelease builds.
- [type BetaInviteType](betainvitetype.md)
  String that indicates how you offer a beta invitation.
- [type BetaTesterState](betatesterstate.md)
  String that describes the state of a beta tester.
- [object BetaTester.Relationships](betatester/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.
- [type BetaInviteType](betainvitetype.md)
  String that indicates how you offer a beta invitation.
- [type BetaTesterState](betatesterstate.md)
  String that describes the state of a beta tester.
- [object BetaTester.Relationships](betatester/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betatester/attributes-data.dictionary)*