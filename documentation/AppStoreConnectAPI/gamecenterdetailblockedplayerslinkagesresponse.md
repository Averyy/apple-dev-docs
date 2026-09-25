# GameCenterDetailBlockedPlayersLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list the blocked player IDs related to a Game Center detail.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object GameCenterDetailBlockedPlayersLinkagesResponse
```

## Topics

### Objects
- [object GameCenterDetailBlockedPlayersLinkagesResponse.Data](gamecenterdetailblockedplayerslinkagesresponse/data-data.dictionary.md)
  The resource identifier for a blocked player related to a Game Center detail.

## Properties

- `data` ([GameCenterDetailBlockedPlayersLinkagesResponse.Data]) *(required)*: The resource identifiers for the blocked players related to the Game Center detail.
- `links` (PagedDocumentLinks) *(required)*: Navigational links including the self-link and links to the related data.
- `meta` (PagingInformation): Paging information.

## See Also

- [object GameCenterDetailPlayer](gamecenterdetailplayer.md)
  A Game Center player tied to a single game, whom you can block from playing that game.
- [object GameCenterDetailPlayerResponse](gamecenterdetailplayerresponse.md)
  The response body for endpoints that modify a Game Center player in an app’s Game Center configuration.
- [object GameCenterDetailPlayerUpdateRequest](gamecenterdetailplayerupdaterequest.md)
  The request body you use to update a Game Center detail player.
- [object GameCenterDetailPlayersResponse](gamecenterdetailplayersresponse.md)
  The response body for endpoints that list the blocked players for a game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterdetailblockedplayerslinkagesresponse)*