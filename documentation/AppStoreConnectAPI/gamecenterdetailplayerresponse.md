# GameCenterDetailPlayerResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that modify a Game Center player in an app’s Game Center configuration.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object GameCenterDetailPlayerResponse
```

#### Overview

The [`Modify a Game Center Detail Player`](patch-v1-gamecenterdetailplayers-_id_.md) endpoint returns this response.

## Properties

- `data` (GameCenterDetailPlayer) *(required)*: The resource data. Contains a single [`GameCenterDetailPlayer`](gamecenterdetailplayer.md) resource.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [object GameCenterDetailPlayer](gamecenterdetailplayer.md)
  A Game Center player tied to a single game, whom you can block from playing that game.
- [object GameCenterDetailPlayerUpdateRequest](gamecenterdetailplayerupdaterequest.md)
  The request body you use to update a Game Center detail player.
- [object GameCenterDetailPlayersResponse](gamecenterdetailplayersresponse.md)
  The response body for endpoints that list the blocked players for a game.
- [object GameCenterDetailBlockedPlayersLinkagesResponse](gamecenterdetailblockedplayerslinkagesresponse.md)
  The response body for endpoints that list the blocked player IDs related to a Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterdetailplayerresponse)*