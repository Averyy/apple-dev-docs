# GameCenterLeaderboardRelease

**Framework**: App Store Connect API  
**Kind**: dictionary

A record indicating that a Game Center leaderboard has been released to players, making it visible in the game.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object GameCenterLeaderboardRelease
```

## Topics

### Objects
- [object GameCenterLeaderboardRelease.Attributes](gamecenterleaderboardrelease/attributes-data.dictionary.md)
  Attributes that describe a leaderboard resource.
- [object GameCenterLeaderboardRelease.Relationships](gamecenterleaderboardrelease/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (GameCenterLeaderboardRelease.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (GameCenterLeaderboardRelease.Relationships)
- `type` (string) *(required)*

## See Also

- [object GameCenterLeaderboardReleaseCreateRequest](gamecenterleaderboardreleasecreaterequest.md)
  The request body you use to create a leaderboard release.
- [object GameCenterLeaderboardReleaseResponse](gamecenterleaderboardreleaseresponse.md)
  The response body for endpoints that create, read, or modify a single Game Center leaderboard release.
- [object GameCenterLeaderboardReleasesResponse](gamecenterleaderboardreleasesresponse.md)
  A response that contains multiple leaderboard release resource.
- [object GameCenterLeaderboardReleasesLinkagesResponse](gamecenterleaderboardreleaseslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardrelease)*