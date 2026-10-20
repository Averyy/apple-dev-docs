# GameCenterActivityVersionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing a single version of a Game Center activity.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```
object GameCenterActivityVersionResponse
```

## Properties

- `data` (GameCenterActivityVersion) *(required)*
- `included` ([*]): **Allowed Types**: `GameCenterActivity`, `GameCenterActivityImage`, `GameCenterActivityLocalization`, `GameCenterActivityVersionRelease`
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object GameCenterActivityVersionRelease](./gamecenteractivityversionrelease.md)
  A record indicating that a version of a Game Center activity has been released to players.
- [object GameCenterActivityVersionReleaseCreateRequest](./gamecenteractivityversionreleasecreaterequest.md)
  The request body for releasing a Game Center activity version to players.
- [object GameCenterActivityVersionReleaseResponse](./gamecenteractivityversionreleaseresponse.md)
  A response containing a single release record for a Game Center activity version.
- [object GameCenterActivityVersionReleasesResponse](./gamecenteractivityversionreleasesresponse.md)
  A response containing a list of release records for a Game Center activity version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenteractivityversionresponse)*