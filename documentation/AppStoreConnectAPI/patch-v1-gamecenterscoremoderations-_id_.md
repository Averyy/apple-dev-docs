# Modify a Game Center Score Moderation

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Block or unblock a score submitted to a leaderboard.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5 release notes](./app-store-connect-api-4-5-release-notes.md)

#### Overview

Blocking a score removes it from the leaderboard, and unblocking reinstates it. The response contains the updated [`GameCenterScoreModeration`](./gamecenterscoremoderation.md) in a [`GameCenterScoreModerationResponse`](./gamecenterscoremoderationresponse.md).

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterScoreModerations/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the score moderation resource ID from the [`List Score Moderations for a Leaderboard`](./get-v2-gamecenterleaderboards-_id_-gamecenterscoremoderations.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterScoreModerationUpdateRequest`

The request body you use to modify a Game Center score moderation. See [`GameCenterScoreModerationUpdateRequest`](./gamecenterscoremoderationupdaterequest.md).

## Responses

- `200` OK (`GameCenterScoreModerationResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterscoremoderations-_id_)*