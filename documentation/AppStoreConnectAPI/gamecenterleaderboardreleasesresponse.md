# GameCenterLeaderboardReleasesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response that contains multiple leaderboard release resource.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This object is deprecated.

## Declaration

```
object GameCenterLeaderboardReleasesResponse
```

## Properties

- `data` ([GameCenterLeaderboardRelease]) *(required)*
- `included` ([*]): **Allowed Types**: `GameCenterDetail`, `GameCenterLeaderboard`
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

### Objects
- [object GameCenterLeaderboardRelease](./gamecenterleaderboardrelease.md)
  A record indicating that a Game Center leaderboard has been released to players, making it visible in the game.
- [object GameCenterLeaderboardReleaseCreateRequest](./gamecenterleaderboardreleasecreaterequest.md)
  The request body you use to create a leaderboard release.
- [object GameCenterLeaderboardReleaseResponse](./gamecenterleaderboardreleaseresponse.md)
  The response body for endpoints that create, read, or modify a single Game Center leaderboard release.
- [object GameCenterLeaderboardReleasesLinkagesResponse](./gamecenterleaderboardreleaseslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardreleasesresponse)*