# GameCenterLeaderboardReleasesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains multiple leaderboard release resource.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object GameCenterLeaderboardReleasesResponse
```

## Properties

- `data` ([GameCenterLeaderboardRelease]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object GameCenterLeaderboardRelease](gamecenterleaderboardrelease.md)
  A record indicating that a Game Center leaderboard has been released to players, making it visible in the game.
- [object GameCenterLeaderboardReleaseCreateRequest](gamecenterleaderboardreleasecreaterequest.md)
  The request body you use to create a leaderboard release.
- [object GameCenterLeaderboardReleaseResponse](gamecenterleaderboardreleaseresponse.md)
  The response body for endpoints that create, read, or modify a single Game Center leaderboard release.
- [object GameCenterLeaderboardReleasesLinkagesResponse](gamecenterleaderboardreleaseslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardreleasesresponse)*