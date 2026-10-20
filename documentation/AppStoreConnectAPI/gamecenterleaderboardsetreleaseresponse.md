# GameCenterLeaderboardSetReleaseResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that create, read, or modify a single Game Center leaderboard set release.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This object is deprecated.

## Declaration

```
object GameCenterLeaderboardSetReleaseResponse
```

## Properties

- `data` (GameCenterLeaderboardSetRelease) *(required)* *(deprecated)*
- `included` ([*]): **Allowed Types**: `GameCenterDetail`, `GameCenterLeaderboardSet`
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object GameCenterLeaderboardSetRelease](./gamecenterleaderboardsetrelease.md)
  The data structure that represent a leaderboard set release.
- [object GameCenterLeaderboardSetReleaseCreateRequest](./gamecenterleaderboardsetreleasecreaterequest.md)
  The request body you use to create a leaderboard set release.
- [object GameCenterLeaderboardSetReleasesResponse](./gamecenterleaderboardsetreleasesresponse.md)
  A response that contains multiple leaderboard set release resource.
- [object GameCenterLeaderboardSetReleasesLinkagesResponse](./gamecenterleaderboardsetreleaseslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardsetreleaseresponse)*