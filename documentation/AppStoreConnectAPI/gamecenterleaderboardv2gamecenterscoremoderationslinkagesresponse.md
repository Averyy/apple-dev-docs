# GameCenterLeaderboardV2GameCenterScoreModerationsLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list the score moderation linkages for a Game Center leaderboard.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object GameCenterLeaderboardV2GameCenterScoreModerationsLinkagesResponse
```

## Topics

### Dictionaries
- [object GameCenterLeaderboardV2GameCenterScoreModerationsLinkagesResponse.Data](gamecenterleaderboardv2gamecenterscoremoderationslinkagesresponse/data-data.dictionary.md)
  The resource identifier for a related score moderation.

## Properties

- `data` ([GameCenterLeaderboardV2GameCenterScoreModerationsLinkagesResponse.Data]) *(required)*: The resource identifiers for the related score moderations.
- `links` (PagedDocumentLinks) *(required)*: Navigational links including the self-link and links to the related data.
- `meta` (PagingInformation): Paging information.

## See Also

- [object GameCenterScoreModeration](gamecenterscoremoderation.md)
  A score submitted to a Game Center leaderboard that you review and choose to block or unblock.
- [object GameCenterScoreModerationResponse](gamecenterscoremoderationresponse.md)
  The response body for endpoints that modify a single Game Center score moderation.
- [object GameCenterScoreModerationUpdateRequest](gamecenterscoremoderationupdaterequest.md)
  The request body you use to update a Game Center score moderation.
- [object GameCenterScoreModerationsResponse](gamecenterscoremoderationsresponse.md)
  The response body for endpoints that list Game Center score moderations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterleaderboardv2gamecenterscoremoderationslinkagesresponse)*