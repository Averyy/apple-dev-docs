# List Score Moderation IDs for a Game Center Leaderboard

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the score moderation IDs for a Game Center leaderboard.

**Availability**:
- App Store Connect API 4.5+

#### Overview

The response contains the score moderations’ resource identifiers in a [`GameCenterLeaderboardV2GameCenterScoreModerationsLinkagesResponse`](gamecenterleaderboardv2gamecenterscoremoderationslinkagesresponse.md).

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboards/{id}/relationships/gameCenterScoreModerations`

## Parameters

- `limit` (integer): The maximum number of related gameCenterScoreModerations resource identifiers to return.

## See Also

- [List Score Moderations for a Leaderboard](get-v2-gamecenterleaderboards-_id_-gamecenterscoremoderations.md)
  List the score moderations for a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboards-_id_-relationships-gamecenterscoremoderations)*