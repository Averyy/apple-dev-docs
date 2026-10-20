# GameCenterChallengeVersionReleasesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing a list of release records for a Game Center challenge version.

**Availability**:
- App Store Connect API 4.0+ - Deprecated in 4.3

> **Deprecated**: This object is deprecated.

## Declaration

```
object GameCenterChallengeVersionReleasesResponse
```

## Properties

- `data` ([GameCenterChallengeVersionRelease]) *(required)*
- `included` ([GameCenterChallengeVersion])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

### Objects
- [object GameCenterChallengeVersionRelease](./gamecenterchallengeversionrelease.md)
  The data structure that represent a challenge version release.
- [object GameCenterChallengeVersionReleaseCreateRequest](./gamecenterchallengeversionreleasecreaterequest.md)
  The request body for releasing a Game Center challenge version to players.
- [object GameCenterChallengeVersionReleaseResponse](./gamecenterchallengeversionreleaseresponse.md)
  A response containing a single release record for a Game Center challenge version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterchallengeversionreleasesresponse)*