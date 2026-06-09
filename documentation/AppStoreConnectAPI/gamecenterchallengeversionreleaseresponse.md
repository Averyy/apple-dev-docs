# GameCenterChallengeVersionReleaseResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a single release record for a Game Center challenge version.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object GameCenterChallengeVersionReleaseResponse
```

## Properties

- `data` (GameCenterChallengeVersionRelease) *(required)*
- `included` ([GameCenterChallengeVersion])
- `links` (DocumentLinks) *(required)*

## See Also

- [object GameCenterChallengeVersionRelease](gamecenterchallengeversionrelease.md)
  The data structure that represent a challenge version release.
- [object GameCenterChallengeVersionReleaseCreateRequest](gamecenterchallengeversionreleasecreaterequest.md)
  The request body for releasing a Game Center challenge version to players.
- [object GameCenterChallengeVersionReleasesResponse](gamecenterchallengeversionreleasesresponse.md)
  A response containing a list of release records for a Game Center challenge version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterchallengeversionreleaseresponse)*