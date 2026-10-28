# GameCenterLeaderboardV2CreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create a Game Center leaderboard create request.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```
object GameCenterLeaderboardV2CreateRequest.Data.Attributes
```

## Overview

- activityProperties:
- defaultFormatter:
- recurrenceDuration:
- recurrenceRule:
- recurrenceStartDate:
- referenceName:
- scoreRangeEnd:
- scoreRangeStart:
- scoreSortType:
- submissionType:
- vendorIdentifier:
- visibility:

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

### Dictionaries
- [object GameCenterLeaderboardV2CreateRequest.Data.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those you can operate on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardv2createrequest/data-data.dictionary/attributes-data.dictionary)*