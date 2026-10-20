# List Score Moderation IDs for a Game Center Leaderboard

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List the score moderation IDs for a Game Center leaderboard.

**Availability**:
- App Store Connect API 4.5+

#### Overview

The response contains the score moderations’ resource identifiers in a [`GameCenterLeaderboardV2GameCenterScoreModerationsLinkagesResponse`](./gamecenterleaderboardv2gamecenterscoremoderationslinkagesresponse.md).

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboards/{id}/relationships/gameCenterScoreModerations`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the leaderboard resource ID from the [`Get leaderboards information`](./get-v1-gamecenterdetails-_id_-gamecenterleaderboards.md) response.

### Query Parameters

- `limit` (integer): The maximum number of related gameCenterScoreModerations resource identifiers to return.

  **Maximum**: `200`

## Responses

- `200` OK (`GameCenterLeaderboardV2GameCenterScoreModerationsLinkagesResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading score moderations
- [List Score Moderations for a Leaderboard](./get-v2-gamecenterleaderboards-_id_-gamecenterscoremoderations.md)
  List the score moderations for a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboards-_id_-relationships-gamecenterscoremoderations)*