# List Score Moderations for a Leaderboard

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List the score moderations for a leaderboard.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5 release notes](./app-store-connect-api-4-5-release-notes.md)

## Overview

The response contains a list of [`GameCenterScoreModeration`](./gamecenterscoremoderation.md) resources in a [`GameCenterScoreModerationsResponse`](./gamecenterscoremoderationsresponse.md).

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboards/{id}/gameCenterScoreModerations`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the leaderboard resource ID from the [`Get leaderboards information`](./get-v1-gamecenterdetails-_id_-gamecenterleaderboards.md) response.

### Query Parameters

- `exists[blocked]` (boolean): Filter the returned score moderations to include only those that are blocked (true) or not blocked (false).
- `fields[gameCenterScoreModerations]` ([string]): Additional fields to include for each gameCenterScoreModerations resource returned by the response.

  **Allowed Values**: `rank`, `score`, `submittedDate`, `blocked`, `preReleased`, `context`, `challengeIds`, `player`
- `fields[gameCenterDetailPlayers]` ([string]): Additional fields to include for each gameCenterDetailPlayers resource returned by the response.

  **Allowed Values**: `nickname`, `blocked`, `bundleId`
- `limit` (integer): The maximum number of score moderation resources to return.

  **Maximum**: `200`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `player`

## Responses

- `200` OK (`GameCenterScoreModerationsResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): The request isn’t authorized.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`): The rate limit is exceeded.

## See Also

### Reading score moderations
- [List Score Moderation IDs for a Game Center Leaderboard](./get-v2-gamecenterleaderboards-_id_-relationships-gamecenterscoremoderations.md)
  List the score moderation IDs for a Game Center leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboards-_id_-gamecenterscoremoderations)*