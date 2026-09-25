# List Blocked Players

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the blocked players for a game.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5 release notes](app-store-connect-api-4-5-release-notes.md)

#### Overview

The response contains a list of [`GameCenterDetailPlayer`](gamecenterdetailplayer.md) resources in a [`GameCenterDetailPlayersResponse`](gamecenterdetailplayersresponse.md).

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/blockedPlayers`

## Parameters

- `fields[gameCenterDetailPlayers]` ([string]): Additional fields to include for each gameCenterDetailPlayers resource returned by the response.
- `limit` (integer): The maximum number of blocked player resources to return.

## See Also

- [List Blocked Player IDs](get-v1-gamecenterdetails-_id_-relationships-blockedplayers.md)
  List the blocked player IDs for a Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-blockedplayers)*