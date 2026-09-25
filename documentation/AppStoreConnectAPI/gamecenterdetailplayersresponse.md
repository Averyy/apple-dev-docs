# GameCenterDetailPlayersResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list the blocked players for a game.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object GameCenterDetailPlayersResponse
```

#### Overview

The [`List Blocked Players`](get-v1-gamecenterdetails-_id_-blockedplayers.md) endpoint returns this response.

## Properties

- `data` ([GameCenterDetailPlayer]) *(required)*: The resource data. Contains an array of [`GameCenterDetailPlayer`](gamecenterdetailplayer.md) resources.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.

## See Also

- [object GameCenterDetailPlayer](gamecenterdetailplayer.md)
  A Game Center player tied to a single game, whom you can block from playing that game.
- [object GameCenterDetailPlayerResponse](gamecenterdetailplayerresponse.md)
  The response body for endpoints that modify a Game Center player in an app’s Game Center configuration.
- [object GameCenterDetailPlayerUpdateRequest](gamecenterdetailplayerupdaterequest.md)
  The request body you use to update a Game Center detail player.
- [object GameCenterDetailBlockedPlayersLinkagesResponse](gamecenterdetailblockedplayerslinkagesresponse.md)
  The response body for endpoints that list the blocked player IDs related to a Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterdetailplayersresponse)*