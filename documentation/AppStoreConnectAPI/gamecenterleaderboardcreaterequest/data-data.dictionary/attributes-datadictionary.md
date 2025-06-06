# GameCenterLeaderboardCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object GameCenterLeaderboardCreateRequest.Data.Attributes
```

## Mentions

- [App Store Connect API 3.7 release notes](app-store-connect-api-3-7-release-notes.md)

##### Discussion

Use leaderboard formatters to specify the unit of measurement for a Game Center leaderboard. There is a new required attribute `defaultFormatter` when using [`Create a leaderboard`](post-v1-gamecenterleaderboards.md), which gives all your localizations the same formatter. You can also optionally use `formatterOverride` to override a specific leaderboard localization when calling [`Create a leaderboard localization`](post-v1-gamecenterleaderboardlocalizations.md) or [`Modify a leaderboard localization`](patch-v1-gamecenterleaderboardlocalizations-_id_.md).

Before App Store Connect API version 3.0, formatters were based on localizations and were required for each localization. Legacy leaderboards created before the new addition of the Game Center APIs don’t have a `defaultFormatter` value; the value is `null`. Any localizations created before the new addition of the Game Center APIs have a `formatterOverride`.

## See Also

- [object GameCenterLeaderboardCreateRequest.Data.Relationships](gamecenterleaderboardcreaterequest/data-data.dictionary/relationships-data.dictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardcreaterequest/data-data.dictionary/attributes-data.dictionary)*