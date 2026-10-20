# GameCenterLeaderboardCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a leaderboard resource.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```
object GameCenterLeaderboardCreateRequest.Data.Attributes
```

## Mentions

- [App Store Connect API 3.7 release notes](../../app-store-connect-api-3-7-release-notes.md)

##### Discussion

Use leaderboard formatters to specify the unit of measurement for a Game Center leaderboard. There is a new required attribute `defaultFormatter` when using [`Create a Leaderboard`](../../post-v1-gamecenterleaderboards.md), which gives all your localizations the same formatter. You can also optionally use `formatterOverride` to override a specific leaderboard localization when calling [`Create a Leaderboard Localization`](../../post-v1-gamecenterleaderboardlocalizations.md) or [`Modify a Leaderboard Localization`](../../patch-v1-gamecenterleaderboardlocalizations-_id_.md).

Before App Store Connect API version 3.0, formatters were based on localizations and were required for each localization. Legacy leaderboards created before the new addition of the Game Center APIs don’t have a `defaultFormatter` value; the value is `null`. Any localizations created before the new addition of the Game Center APIs have a `formatterOverride`.

## Properties

- `activityProperties` (StringToStringMap)
- `defaultFormatter` (GameCenterLeaderboardFormatter) *(required)*
- `recurrenceDuration` (duration)
- `recurrenceRule` (string)
- `recurrenceStartDate` (date-time)
- `referenceName` (string) *(required)*
- `scoreRangeEnd` (number)
- `scoreRangeStart` (number)
- `scoreSortType` (string) *(required)*: **Allowed Values**: `ASC`, `DESC`
- `submissionType` (string) *(required)*: **Allowed Values**: `BEST_SCORE`, `MOST_RECENT_SCORE`
- `vendorIdentifier` (string) *(required)*
- `visibility` (string): **Allowed Values**: `SHOW_FOR_ALL`, `HIDE_FOR_ALL`

## See Also

### Objects
- [object GameCenterLeaderboardCreateRequest.Data.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardcreaterequest/data-data.dictionary/attributes-data.dictionary)*