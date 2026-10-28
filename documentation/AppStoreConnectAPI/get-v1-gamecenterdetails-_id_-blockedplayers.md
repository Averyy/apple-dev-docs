# List Blocked Players

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List the blocked players for a game.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5 release notes](./app-store-connect-api-4-5-release-notes.md)

## Overview

The response contains a list of [`GameCenterDetailPlayer`](./gamecenterdetailplayer.md) resources in a [`GameCenterDetailPlayersResponse`](./gamecenterdetailplayersresponse.md).

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/blockedPlayers`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the Game Center detail resource ID from the [`Read the state of game center for an app`](./get-v1-apps-_id_-gamecenterdetail.md) response.

### Query Parameters

- `fields[gameCenterDetailPlayers]` ([string]): Additional fields to include for each gameCenterDetailPlayers resource returned by the response.

  **Allowed Values**: `nickname`, `blocked`, `bundleId`
- `limit` (integer): The maximum number of blocked player resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`GameCenterDetailPlayersResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading blocked players
- [List Blocked Player IDs](./get-v1-gamecenterdetails-_id_-relationships-blockedplayers.md)
  List the blocked player IDs for a Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-blockedplayers)*