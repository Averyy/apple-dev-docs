# GameCenterScoreModerationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that modify a single Game Center score moderation.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object GameCenterScoreModerationResponse
```

#### Overview

The [`Modify a Game Center Score Moderation`](patch-v1-gamecenterscoremoderations-_id_.md) endpoint returns this response.

## Properties

- `data` (GameCenterScoreModeration) *(required)*: The resource data. Contains a single [`GameCenterScoreModeration`](gamecenterscoremoderation.md) resource.
- `included` ([GameCenterDetailPlayer]): The requested relationship data. Contains an array of [`GameCenterDetailPlayer`](gamecenterdetailplayer.md) resources.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [object GameCenterScoreModeration](gamecenterscoremoderation.md)
  A score submitted to a Game Center leaderboard that you review and choose to block or unblock.
- [object GameCenterScoreModerationUpdateRequest](gamecenterscoremoderationupdaterequest.md)
  The request body you use to update a Game Center score moderation.
- [object GameCenterScoreModerationsResponse](gamecenterscoremoderationsresponse.md)
  The response body for endpoints that list Game Center score moderations.
- [object GameCenterLeaderboardV2GameCenterScoreModerationsLinkagesResponse](gamecenterleaderboardv2gamecenterscoremoderationslinkagesresponse.md)
  The response body for endpoints that list the score moderation linkages for a Game Center leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterscoremoderationresponse)*