# GameCenterDetailPlayerUpdateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The resource data for the Game Center detail player you update.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```
object GameCenterDetailPlayerUpdateRequest.Data
```

## Topics

### Objects
- [object GameCenterDetailPlayerUpdateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  The attributes that describe a Game Center detail player you update.

## Properties

- `attributes` (GameCenterDetailPlayerUpdateRequest.Data.Attributes): The attributes that describe the Game Center detail player.
- `id` (string) *(required)*: The player’s game-scoped ID — the same identifier GameKit vends as [`gamePlayerID`](../../GameKit/gkplayer/gameplayerid.md).
- `type` (string) *(required)*: The resource type.

  - gameCenterDetailPlayers:

  **Allowed Values**: `gameCenterDetailPlayers`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterdetailplayerupdaterequest/data-data.dictionary)*