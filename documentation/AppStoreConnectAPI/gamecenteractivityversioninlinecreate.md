# GameCenterActivityVersionInlineCreate

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure you use to configure an activity version while creating an activity.

**Availability**:
- App Store Connect API 4.3+

## Declaration

```swift
object GameCenterActivityVersionInlineCreate
```

## Mentions

- [App Store Connect API 4.3 release notes](app-store-connect-api-4-3-release-notes.md)

## Topics

### Dictionaries
- [object GameCenterActivityVersionInlineCreate.Attributes](gamecenteractivityversioninlinecreate/attributes-data.dictionary.md)
  Attributes that describe an activity version resource that you create while creating an activity.
- [object GameCenterActivityVersionInlineCreate.Relationships](gamecenteractivityversioninlinecreate/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (GameCenterActivityVersionInlineCreate.Attributes)
- `id` (string)
- `relationships` (GameCenterActivityVersionInlineCreate.Relationships)
- `type` (string) *(required)*

## See Also

- [object GameCenterActivitiesResponse](gamecenteractivitiesresponse.md)
  A response containing a list of Game Center activities configured for an app.
- [object GameCenterActivity](gamecenteractivity.md)
  A social or competitive event in Game Center that players can participate in, such as a leaderboard challenge.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenteractivityversioninlinecreate)*