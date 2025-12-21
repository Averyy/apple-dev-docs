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

## See Also

- [object GameCenterLeaderboardV2](gamecenterleaderboardv2.md)
  The data structure that represents a Game Center leaderboard v2 resource.
- [object GameCenterLeaderboardV2CreateRequest](gamecenterleaderboardv2createrequest.md)
  The request body you use to create a Game Center leaderboard v2.
- [object GameCenterLeaderboardV2Response](gamecenterleaderboardv2response.md)
  A response that contains a single Game Center leaderboard v2 resource.
- [object GameCenterLeaderboardV2UpdateRequest](gamecenterleaderboardv2updaterequest.md)
  The request body you use to update a Game Center leaderboard v2.
- [object GameCenterLeaderboardsV2Response](gamecenterleaderboardsv2response.md)
  A response that contains a list of Game Center leaderboard resources.
- [object GameCenterLeaderboardV2ActivityLinkageRequest](gamecenterleaderboardv2activitylinkagerequest.md)
  The data structure that represents a Game Center leaderboard v2 activity linkage request resource.
- [object GameCenterLeaderboardV2ChallengeLinkageRequest](gamecenterleaderboardv2challengelinkagerequest.md)
  The data structure that represents a Game Center leaderboard v2 challenge linkage request resource.
- [object GameCenterLeaderboardV2VersionsLinkagesResponse](gamecenterleaderboardv2versionslinkagesresponse.md)
  A response that contains a list of Game Center leaderboard v2 version linkage resources.
- [object GameCenterLeaderboardUpdateRequest](gamecenterleaderboardupdaterequest.md)
  The request body you use to update a leaderboard.
- [object GameCenterLeaderboardsResponse](gamecenterleaderboardsresponse.md)
  A response that contains multiple leaderboard resources.
- [object GameCenterLeaderboard](gamecenterleaderboard.md)
  The data structure that represent a leaderboard resource.
- [object GameCenterLeaderboardCreateRequest](gamecenterleaderboardcreaterequest.md)
  The request body you use to create a leaderboard.
- [object GameCenterLeaderboardResponse](gamecenterleaderboardresponse.md)
  A response that contains a single leaderboard image resource.
- [object GameCenterLeaderboardGroupLeaderboardLinkageRequest](gamecenterleaderboardgroupleaderboardlinkagerequest.md)
  The request body you use to attach an individual leaderbaord to a group leaderboard.
- [object GameCenterLeaderboardGroupLeaderboardLinkageResponse](gamecenterleaderboardgroupleaderboardlinkageresponse.md)
  A response confriming a relationship between a leaderboard and group leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardformatter)*