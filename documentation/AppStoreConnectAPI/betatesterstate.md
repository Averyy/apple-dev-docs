# BetaTesterState

**Framework**: App Store Connect API  
**Kind**: typealias

String that describes the state of a beta tester.

**Availability**:
- App Store Connect API 3.5+

## Declaration

```swift
string BetaTesterState
```

#### Possible Values

- **NOT_INVITED**: The beta tester is not currently invited.
- **INVITED**: The build of your app is eligible for submission and release on the App Store.
- **ACCEPTED**: The beta tester has accepted an invite to test a build.
- **INSTALLED**: The beta tester has installed a build.
- **REVOKED**: The beta tester chose to stop testing or the beta tester was removed from the app. In both cases the build they installed is not expired. Once the build expires, the system deletes the resource.

## See Also

- [object BetaTester.Attributes](betatester/attributes-data.dictionary.md)
  Attributes that describe a beta tester resource.
- [type BetaInviteType](betainvitetype.md)
  String that indicates how you offer a beta invitation.
- [object BetaTester.Relationships](betatester/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betatesterstate)*