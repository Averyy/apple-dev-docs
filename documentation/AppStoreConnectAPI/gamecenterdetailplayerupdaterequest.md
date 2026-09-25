# GameCenterDetailPlayerUpdateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to update a Game Center detail player.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object GameCenterDetailPlayerUpdateRequest
```

## Topics

### Objects
- [object GameCenterDetailPlayerUpdateRequest.Data](gamecenterdetailplayerupdaterequest/data-data.dictionary.md)
  The resource data for the Game Center detail player you update.

## Properties

- `data` (GameCenterDetailPlayerUpdateRequest.Data) *(required)*: The resource data.

## See Also

- [object GameCenterDetailPlayer](gamecenterdetailplayer.md)
  A Game Center player tied to a single game, whom you can block from playing that game.
- [object GameCenterDetailPlayerResponse](gamecenterdetailplayerresponse.md)
  The response body for endpoints that modify a Game Center player in an app’s Game Center configuration.
- [object GameCenterDetailPlayersResponse](gamecenterdetailplayersresponse.md)
  The response body for endpoints that list the blocked players for a game.
- [object GameCenterDetailBlockedPlayersLinkagesResponse](gamecenterdetailblockedplayerslinkagesresponse.md)
  The response body for endpoints that list the blocked player IDs related to a Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterdetailplayerupdaterequest)*