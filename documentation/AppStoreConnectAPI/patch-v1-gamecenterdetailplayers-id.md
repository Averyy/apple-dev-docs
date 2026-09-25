# Modify a Game Center Detail Player

**Framework**: App Store Connect API  
**Kind**: httpRequest

Block or unblock a player for a game.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5 release notes](app-store-connect-api-4-5-release-notes.md)

#### Overview

> 💡 **Tip**:  These endpoints require information from GameKit, specifically [`gamePlayerID`](https://developer.apple.com/documentation/gamekit/gkplayer/gameplayerid).

Blocking a player prevents that player from playing the game. The response contains the updated [`GameCenterDetailPlayer`](gamecenterdetailplayer.md) in a [`GameCenterDetailPlayerResponse`](gamecenterdetailplayerresponse.md).

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterDetailPlayers/{id}`

## Parameters

- `id` (string) *(required)*: The player’s game-scoped ID. Obtain it from the [`List Blocked Players`](get-v1-gamecenterdetails-_id_-blockedplayers.md) response or the [`List Score Moderations for a Leaderboard`](get-v2-gamecenterleaderboards-_id_-gamecenterscoremoderations.md) response.

## Request Body

The request body you use to modify a Game Center detail player. See [`GameCenterDetailPlayerUpdateRequest`](gamecenterdetailplayerupdaterequest.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterdetailplayers-_id_)*