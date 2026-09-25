# GameCenterScoreModerationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list Game Center score moderations.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object GameCenterScoreModerationsResponse
```

## Properties

- `data` ([GameCenterScoreModeration]) *(required)*: The resource data. Contains an array of [`GameCenterScoreModeration`](gamecenterscoremoderation.md) resources.
- `included` ([GameCenterDetailPlayer]): The requested relationship data. Contains an array of [`GameCenterDetailPlayer`](gamecenterdetailplayer.md) resources.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.

## See Also

- [object GameCenterScoreModeration](gamecenterscoremoderation.md)
  A score submitted to a Game Center leaderboard that you review and choose to block or unblock.
- [object GameCenterScoreModerationResponse](gamecenterscoremoderationresponse.md)
  The response body for endpoints that modify a single Game Center score moderation.
- [object GameCenterScoreModerationUpdateRequest](gamecenterscoremoderationupdaterequest.md)
  The request body you use to update a Game Center score moderation.
- [object GameCenterLeaderboardV2GameCenterScoreModerationsLinkagesResponse](gamecenterleaderboardv2gamecenterscoremoderationslinkagesresponse.md)
  The response body for endpoints that list the score moderation linkages for a Game Center leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterscoremoderationsresponse)*