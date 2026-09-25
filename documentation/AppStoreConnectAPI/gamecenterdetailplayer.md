# GameCenterDetailPlayer

**Framework**: App Store Connect API  
**Kind**: dictionary

A Game Center player tied to a single game, whom you can block from playing that game.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object GameCenterDetailPlayer
```

## Topics

### Objects
- [object GameCenterDetailPlayer.Attributes](gamecenterdetailplayer/attributes-data.dictionary.md)
  The attributes that describe a Game Center detail player.

## Properties

- `attributes` (GameCenterDetailPlayer.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The player’s game-scoped ID — the same identifier GameKit vends as [`gamePlayerID`](https://developer.apple.com/documentation/gamekit/gkplayer/gameplayerid).
- `links` (ResourceLinks): Navigational links that include the self-link.
- `type` (string) *(required)*: The resource type.

## See Also

- [object GameCenterDetailPlayerResponse](gamecenterdetailplayerresponse.md)
  The response body for endpoints that modify a Game Center player in an app’s Game Center configuration.
- [object GameCenterDetailPlayerUpdateRequest](gamecenterdetailplayerupdaterequest.md)
  The request body you use to update a Game Center detail player.
- [object GameCenterDetailPlayersResponse](gamecenterdetailplayersresponse.md)
  The response body for endpoints that list the blocked players for a game.
- [object GameCenterDetailBlockedPlayersLinkagesResponse](gamecenterdetailblockedplayerslinkagesresponse.md)
  The response body for endpoints that list the blocked player IDs related to a Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterdetailplayer)*