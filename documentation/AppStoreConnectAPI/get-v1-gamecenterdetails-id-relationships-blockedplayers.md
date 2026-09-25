# List Blocked Player IDs

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the blocked player IDs for a Game Center detail.

**Availability**:
- App Store Connect API 4.5+

#### Overview

The response contains the blocked players’ resource identifiers in a [`GameCenterDetailBlockedPlayersLinkagesResponse`](gamecenterdetailblockedplayerslinkagesresponse.md).

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/relationships/blockedPlayers`

## Parameters

- `limit` (integer): The maximum number of related blockedPlayers resource identifiers to return.

## See Also

- [List Blocked Players](get-v1-gamecenterdetails-_id_-blockedplayers.md)
  List the blocked players for a game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-relationships-blockedplayers)*