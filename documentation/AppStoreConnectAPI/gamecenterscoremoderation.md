# GameCenterScoreModeration

**Framework**: App Store Connect API  
**Kind**: dictionary

A score submitted to a Game Center leaderboard that you review and choose to block or unblock.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object GameCenterScoreModeration
```

## Topics

### Objects
- [object GameCenterScoreModeration.Attributes](gamecenterscoremoderation/attributes-data.dictionary.md)
  The attributes that describe a Game Center score moderation.
- [object GameCenterScoreModeration.Relationships](gamecenterscoremoderation/relationships-data.dictionary.md)
  The relationships between a Game Center score moderation and other resources.

## Properties

- `attributes` (GameCenterScoreModeration.Attributes): The resource’s attributes.
- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (GameCenterScoreModeration.Relationships): The relationships between this resource and other resources.
- `type` (string) *(required)*: The resource type.

## See Also

- [object GameCenterScoreModerationResponse](gamecenterscoremoderationresponse.md)
  The response body for endpoints that modify a single Game Center score moderation.
- [object GameCenterScoreModerationUpdateRequest](gamecenterscoremoderationupdaterequest.md)
  The request body you use to update a Game Center score moderation.
- [object GameCenterScoreModerationsResponse](gamecenterscoremoderationsresponse.md)
  The response body for endpoints that list Game Center score moderations.
- [object GameCenterLeaderboardV2GameCenterScoreModerationsLinkagesResponse](gamecenterleaderboardv2gamecenterscoremoderationslinkagesresponse.md)
  The response body for endpoints that list the score moderation linkages for a Game Center leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterscoremoderation)*