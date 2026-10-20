# GameCenterLeaderboardReleaseResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that create, read, or modify a single Game Center leaderboard release.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This object is deprecated.

## Declaration

```
object GameCenterLeaderboardReleaseResponse
```

## Properties

- `data` (GameCenterLeaderboardRelease) *(required)* *(deprecated)*
- `included` ([*]): **Allowed Types**: `GameCenterDetail`, `GameCenterLeaderboard`
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object GameCenterLeaderboardRelease](./gamecenterleaderboardrelease.md)
  A record indicating that a Game Center leaderboard has been released to players, making it visible in the game.
- [object GameCenterLeaderboardReleaseCreateRequest](./gamecenterleaderboardreleasecreaterequest.md)
  The request body you use to create a leaderboard release.
- [object GameCenterLeaderboardReleasesResponse](./gamecenterleaderboardreleasesresponse.md)
  A response that contains multiple leaderboard release resource.
- [object GameCenterLeaderboardReleasesLinkagesResponse](./gamecenterleaderboardreleaseslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardreleaseresponse)*