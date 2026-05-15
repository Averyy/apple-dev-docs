# GameCenterLeaderboard.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object GameCenterLeaderboard.Attributes
```

##### Discussion

Use leaderboard formatters to specify the unit of measurement for a Game Center leaderboard. There is a new required attribute `defaultFormatter` when you use [`Create a Leaderboard`](post-v1-gamecenterleaderboards.md), which gives all your localizations the same formatter. You can also optionally use `formatterOverride` to override a specific leaderboard localization when calling [`Create a Leaderboard Localization`](post-v1-gamecenterleaderboardlocalizations.md) or [`Modify a Leaderboard Localization`](patch-v1-gamecenterleaderboardlocalizations-_id_.md).

Before App Store Connect API version 3.0, formatters were based on localizations and were required for each localization. Legacy leaderboards created before the new addition of the Game Center APIs don’t have a `defaultFormatter` value; the value is `null`. Any localizations created before the new addition of the Game Center APIs have a `formatterOverride`.

## Properties

- `activityProperties` (StringToStringMap)
- `archived` (boolean)
- `defaultFormatter` (GameCenterLeaderboardFormatter)
- `recurrenceDuration` (duration)
- `recurrenceRule` (string)
- `recurrenceStartDate` (date-time)
- `referenceName` (string)
- `scoreRangeEnd` (number)
- `scoreRangeStart` (number)
- `scoreSortType` (string)
- `submissionType` (string)
- `vendorIdentifier` (string)
- `visibility` (string)

## See Also

- [object GameCenterLeaderboard.Relationships](gamecenterleaderboard/relationships-data.dictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboard/attributes-data.dictionary)*