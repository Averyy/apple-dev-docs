# GameCenterLeaderboardV2CreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to create a Game Center leaderboard create request.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object GameCenterLeaderboardV2CreateRequest.Data.Attributes
```

#### Overview

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
- `scoreSortType` (string) *(required)*
- `submissionType` (string) *(required)*
- `vendorIdentifier` (string) *(required)*
- `visibility` (string)

## See Also

- [object GameCenterLeaderboardV2CreateRequest.Data.Relationships](gamecenterleaderboardv2createrequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those you can operate on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardv2createrequest/data-data.dictionary/attributes-data.dictionary)*