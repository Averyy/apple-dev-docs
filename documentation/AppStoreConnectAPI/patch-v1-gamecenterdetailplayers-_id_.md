# Modify a Game Center Detail Player

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Block or unblock a player for a game.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5 release notes](./app-store-connect-api-4-5-release-notes.md)

#### Overview

> 💡 **Tip**:  These endpoints require information from GameKit, specifically [`gamePlayerID`](../GameKit/gkplayer/gameplayerid.md).

Blocking a player prevents that player from playing the game. The response contains the updated [`GameCenterDetailPlayer`](./gamecenterdetailplayer.md) in a [`GameCenterDetailPlayerResponse`](./gamecenterdetailplayerresponse.md).

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterDetailPlayers/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The player’s game-scoped ID. Obtain it from the [`List Blocked Players`](./get-v1-gamecenterdetails-_id_-blockedplayers.md) response or the [`List Score Moderations for a Leaderboard`](./get-v2-gamecenterleaderboards-_id_-gamecenterscoremoderations.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `GameCenterDetailPlayerUpdateRequest`

The request body you use to modify a Game Center detail player. See [`GameCenterDetailPlayerUpdateRequest`](./gamecenterdetailplayerupdaterequest.md).

## Responses

- `200` OK (`GameCenterDetailPlayerResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterdetailplayers-_id_)*