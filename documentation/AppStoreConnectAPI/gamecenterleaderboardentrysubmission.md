# GameCenterLeaderboardEntrySubmission

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A player’s score submission to a Game Center leaderboard, including the score value and context.

**Availability**:
- App Store Connect API 3.2+

## Declaration

```
object GameCenterLeaderboardEntrySubmission
```

## Topics

### Objects
- [object GameCenterLeaderboardEntrySubmission.Attributes](./gamecenterleaderboardentrysubmission/attributes-data.dictionary.md)
  Attributes that describe a leaderboard resource.

## Properties

- `attributes` (GameCenterLeaderboardEntrySubmission.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `type` (string) *(required)*: **Allowed Values**: `gameCenterLeaderboardEntrySubmissions`

## See Also

### Objects
- [object GameCenterLeaderboardEntrySubmissionCreateRequest](./gamecenterleaderboardentrysubmissioncreaterequest.md)
  The request body you use to create a Game Center leaderboard entry submission.
- [object GameCenterLeaderboardEntrySubmissionResponse](./gamecenterleaderboardentrysubmissionresponse.md)
  A response confirming a player’s score submission to a Game Center leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardentrysubmission)*