# GameCenterScoreModeration.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes that describe a Game Center score moderation.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object GameCenterScoreModeration.Attributes
```

## Properties

- `blocked` (boolean): A Boolean value that indicates whether the score is blocked from the leaderboard.
- `challengeIds` ([string]): The identifiers of the challenges the score completes.
- `context` (number): A developer-defined 64-bit value the game stores with the score, as a string. This value doesn’t affect ranking.
- `preReleased` (boolean): A Boolean value that indicates whether the player submitted the score to a prerelease version of the game.
- `rank` (number): The rank of the score on the leaderboard, as a string representation of a 64-bit integer.
- `score` (number): The score value the player submitted to the leaderboard, as a string representation of a 64-bit integer.
- `submittedDate` (date-time): The date and time when the player submitted the score.

## See Also

- [object GameCenterScoreModeration.Relationships](gamecenterscoremoderation/relationships-data.dictionary.md)
  The relationships between a Game Center score moderation and other resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterscoremoderation/attributes-data.dictionary)*