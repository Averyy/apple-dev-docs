# GameCenterLeaderboardV2.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a Game Center leaderboard v2 resource.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```
object GameCenterLeaderboardV2.Attributes
```

#### Overview

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
- vendorIdentifier:
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
- `vendorIdentifier` (string)
- `visibility` (string): **Allowed Values**: `SHOW_FOR_ALL`, `HIDE_FOR_ALL`

## See Also

### Dictionaries
- [object GameCenterLeaderboardV2.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those you can operate on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardv2/attributes-data.dictionary)*