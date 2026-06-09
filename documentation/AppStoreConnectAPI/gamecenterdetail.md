# GameCenterDetail

**Framework**: App Store Connect API  
**Kind**: dictionary

The Game Center configuration for an app, linking it to leaderboards, achievement sets, and groups.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object GameCenterDetail
```

## Topics

### Objects
- [object GameCenterDetail.Attributes](gamecenterdetail/attributes-data.dictionary.md)
  Attributes that describe a detail resource.
- [object GameCenterDetail.Relationships](gamecenterdetail/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (GameCenterDetail.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (GameCenterDetail.Relationships)
- `type` (string) *(required)*

## See Also

- [object GameCenterDetailCreateRequest](gamecenterdetailcreaterequest.md)
  The request body you use to create a Game Center detail.
- [object GameCenterDetailGameCenterAchievementsV2LinkagesRequest](gamecenterdetailgamecenterachievementsv2linkagesrequest.md)
  The data structure that represents a Game Center detail Game Center achievement linkage request resource.
- [object GameCenterDetailGameCenterAchievementsV2LinkagesResponse](gamecenterdetailgamecenterachievementsv2linkagesresponse.md)
  A response that contains a list of Game Center detail Game Center achievement linkage resources.
- [object GameCenterDetailGameCenterLeaderboardSetsV2LinkagesRequest](gamecenterdetailgamecenterleaderboardsetsv2linkagesrequest.md)
  The data structure that represents a Game Center detail Game Center leaderboard set linkage request resource.
- [object GameCenterDetailGameCenterLeaderboardSetsV2LinkagesResponse](gamecenterdetailgamecenterleaderboardsetsv2linkagesresponse.md)
  A response that contains a list of Game Center detail Game Center leaderboard set linkage resources.
- [object GameCenterDetailGameCenterLeaderboardsV2LinkagesRequest](gamecenterdetailgamecenterleaderboardsv2linkagesrequest.md)
  The data structure that represents a Game Center detail Game Center leaderboard linkage request resource.
- [object GameCenterDetailGameCenterLeaderboardsV2LinkagesResponse](gamecenterdetailgamecenterleaderboardsv2linkagesresponse.md)
  A response that contains a list of Game Center detail Game Center leaderboard linkage resources.
- [object GameCenterDetailGameCenterAchievementsLinkagesRequest](gamecenterdetailgamecenterachievementslinkagesrequest.md)
  The request body you use to create a relationship between a Game Center detail and an achievement.
- [object GameCenterDetailGameCenterAchievementsLinkagesResponse](gamecenterdetailgamecenterachievementslinkagesresponse.md)
  A response that confirms a relationship between a Game Center detail and an achievement.
- [object GameCenterDetailGameCenterLeaderboardSetsLinkagesRequest](gamecenterdetailgamecenterleaderboardsetslinkagesrequest.md)
  The request body you use to create a relationship between a Game Center detail and a leaderboard set.
- [object GameCenterDetailGameCenterLeaderboardSetsLinkagesResponse](gamecenterdetailgamecenterleaderboardsetslinkagesresponse.md)
  A response that confirms a relationship between a Game Center detail and leaderboard set.
- [object GameCenterDetailGameCenterLeaderboardsLinkagesRequest](gamecenterdetailgamecenterleaderboardslinkagesrequest.md)
  The request body you use to create a relationship between a Game Center detail and a leaderboard.
- [object GameCenterDetailGameCenterLeaderboardsLinkagesResponse](gamecenterdetailgamecenterleaderboardslinkagesresponse.md)
  A response that confirms a relationship between a Game Center detail and a leaderboard.
- [object GameCenterDetailChallengesMinimumPlatformVersionsLinkagesRequest](gamecenterdetailchallengesminimumplatformversionslinkagesrequest.md)
  The request body for updating the minimum platform versions required for challenges in a Game Center detail.
- [object GameCenterDetailResponse](gamecenterdetailresponse.md)
  The response body for endpoints that read or modify the Game Center details for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterdetail)*