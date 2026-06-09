# GameCenterActivity

**Framework**: App Store Connect API  
**Kind**: dictionary

A social or competitive event in Game Center that players can participate in, such as a leaderboard challenge.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object GameCenterActivity
```

## Topics

### Dictionaries
- [object GameCenterActivity.Attributes](gamecenteractivity/attributes-data.dictionary.md)
  Attributes that describe an activity resource.
- [object GameCenterActivity.Relationships](gamecenteractivity/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (GameCenterActivity.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (GameCenterActivity.Relationships)
- `type` (string) *(required)*

## See Also

- [object GameCenterActivitiesResponse](gamecenteractivitiesresponse.md)
  A response containing a list of Game Center activities configured for an app.
- [object GameCenterActivityAchievementsV2LinkagesRequest](gamecenteractivityachievementsv2linkagesrequest.md)
  The data structure that represents a Game Center activity achievement linkage request resource.
- [object GameCenterActivityLeaderboardsV2LinkagesRequest](gamecenteractivityleaderboardsv2linkagesrequest.md)
  The data structure that represents a Game Center activity leaderboard linkage request resource.
- [object GameCenterActivityAchievementsLinkagesRequest](gamecenteractivityachievementslinkagesrequest.md)
  The request body for updating the list of achievements linked to a Game Center activity.
- [object GameCenterActivityLeaderboardsLinkagesRequest](gamecenteractivityleaderboardslinkagesrequest.md)
  The request body for updating the list of leaderboards linked to a Game Center activity.
- [object GameCenterActivityCreateRequest](gamecenteractivitycreaterequest.md)
  The request body for creating a new Game Center activity.
- [object GameCenterActivityVersionInlineCreate](gamecenteractivityversioninlinecreate.md)
  The data structure you use to configure an activity version while creating an activity.
- [object GameCenterActivityResponse](gamecenteractivityresponse.md)
  A response containing a single Game Center activity with its configuration.
- [object GameCenterActivityUpdateRequest](gamecenteractivityupdaterequest.md)
  The request body you use to update an activity.
- [object GameCenterActivityVersion](gamecenteractivityversion.md)
  A versioned configuration of a Game Center activity, containing its localizations and release status.
- [object GameCenterActivityVersionCreateRequest](gamecenteractivityversioncreaterequest.md)
  The request body for creating a version of a Game Center activity.
- [object GameCenterActivityLocalizationImageLinkageResponse](gamecenteractivitylocalizationimagelinkageresponse.md)
- [object StringToStringMap](stringtostringmap.md)
  A dictionary object mapping arbitrary string keys to string values, used for flexible key-value metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenteractivity)*