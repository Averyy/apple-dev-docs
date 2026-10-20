# GameCenterDetailBlockedPlayersLinkagesResponse.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The resource identifier for a blocked player related to a Game Center detail.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```
object GameCenterDetailBlockedPlayersLinkagesResponse.Data
```

## Properties

- `id` (string) *(required)*: The player’s game-scoped ID — the same identifier GameKit vends as [`gamePlayerID`](../../GameKit/gkplayer/gameplayerid.md).
- `type` (string) *(required)*: The resource type.

  - gameCenterDetailPlayers:

  **Allowed Values**: `gameCenterDetailPlayers`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterdetailblockedplayerslinkagesresponse/data-data.dictionary)*