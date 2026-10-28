# GameCenterLeaderboardV2UpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to modify a Game Center leaderboard update request.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```
object GameCenterLeaderboardV2UpdateRequest.Data.Attributes
```

## Overview

- activityProperties:
- archived:
- defaultFormatter:
- recurrenceDuration:
- recurrenceRule:
- recurrenceStartDate:
- referenceName:
- scoreRangeEnd:
- scoreRangeStart:
- scoreSortType:
- submissionType:
- visibility:

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
- `scoreSortType` (string): **Allowed Values**: `ASC`, `DESC`
- `submissionType` (string): **Allowed Values**: `BEST_SCORE`, `MOST_RECENT_SCORE`
- `visibility` (string): **Allowed Values**: `SHOW_FOR_ALL`, `HIDE_FOR_ALL`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardv2updaterequest/data-data.dictionary/attributes-data.dictionary)*