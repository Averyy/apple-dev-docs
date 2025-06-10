# GameCenterLeaderboardFormatter

**Framework**: App Store Connect API  
**Kind**: typealias

The values you can select to describe the format of a leaderboard.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
string GameCenterLeaderboardFormatter
```

## Mentions

- [App Store Connect API 3.5 release notes](app-store-connect-api-3-5-release-notes.md)
- [App Store Connect API 3.8 release notes](app-store-connect-api-3-8-release-notes.md)

#### Discussion

- PossibleValues - INTEGER
- DECIMAL_POINT_1_PLACE
- DECIMAL_POINT_2_PLACE
- DECIMAL_POINT_3_PLACE
- ELAPSED_TIME_CENTISECOND
- ELAPSED_TIME_MINUTE
- ELAPSED_TIME_SECOND
- MONEY_POUND_DECIMAL
- MONEY_POUND
- MONEY_DOLLAR_DECIMAL
- MONEY_DOLLAR
- MONEY_EURO_DECIMAL
- MONEY_EURO
- MONEY_FRANC_DECIMAL
- MONEY_FRANC
- MONEY_KRONER_DECIMAL
- MONEY_KRONER
- MONEY_YEN

##### Discussion

Leaderboard formatters allow you to specify the unit of measurement for a Game Center leaderboard. There is a new required attribute `defaultFormatter` when using [`Create a leaderboard`](post-v1-gamecenterleaderboards.md) which will give all your localizations the same formatter. You can also optionally use `formatterOverride` to override a specific leaderboard localization when calling [`Create a leaderboard localization`](post-v1-gamecenterleaderboardlocalizations.md) or [`Modify a leaderboard localization`](patch-v1-gamecenterleaderboardlocalizations-_id_.md).

Before App Store Connect API version 3.0, formatters were based on localizations and were required for each localization. Legacy leaderboards created before the new addition of the Game Center APIs will not have a `defaultFormatter` value, the value would be `null` in this case. Any localizations created before the new addition of the Game Center APIs will always have a `formatterOverride`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardformatter)*