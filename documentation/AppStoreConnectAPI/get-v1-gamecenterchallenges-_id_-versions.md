# Read the Versions for a Challenge

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of versions for a specific Game Center challenge.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterChallenges/{id}/versions`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[gameCenterChallengeImages]` ([string]): **Allowed Values**: `fileSize`, `fileName`, `imageAsset`, `uploadOperations`, `assetDeliveryState`
- `fields[gameCenterChallengeLocalizations]` ([string]): **Allowed Values**: `locale`, `name`, `description`, `version`, `image`
- `fields[gameCenterChallengeVersionReleases]` ([string]): **Allowed Values**: `version`
- `fields[gameCenterChallengeVersions]` ([string]): **Allowed Values**: `version`, `state`, `challenge`, `localizations`, `releases`, `defaultImage`
- `fields[gameCenterChallenges]` ([string]): **Allowed Values**: `referenceName`, `vendorIdentifier`, `archived`, `challengeType`, `repeatable`, `gameCenterDetail`, `gameCenterGroup`, `versions`, `leaderboard`, `leaderboardV2`
- `include` ([string]): **Allowed Values**: `challenge`, `localizations`, `releases`, `defaultImage`
- `limit` (integer): **Maximum**: `200`
- `limit[localizations]` (integer): **Maximum**: `50`
- `limit[releases]` (integer) *(deprecated)*: **Maximum**: `50`

## Responses

- `200` OK (`GameCenterChallengeVersionsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing challenges
- [Read Challenge Information](./get-v1-gamecenterchallenges-_id_.md)
  Get information for a specific Game Center challenge.
- [Create a Challenge](./post-v1-gamecenterchallenges.md)
  Add a challenge to a Game Center detail or group by referencing an existing leaderboard.
- [Modify a Challenge](./patch-v1-gamecenterchallenges-_id_.md)
  Update details for a specific Game Center challenge.
- [Modify the Leaderboard for a Game Center Challenge](./patch-v1-gamecenterchallenges-_id_-relationships-leaderboardv2.md)
  Update the leaderboard relationship for a specific Game Center challenge.
- [Modify the Leaderboard for a Challenge](./patch-v1-gamecenterchallenges-_id_-relationships-leaderboard.md)
  Update the relationship between a leaderbaord and a specific Game Center challenge.
- [Modify the challenges minimum platform version for a game center detail](./patch-v1-gamecenterdetails-_id_-relationships-challengesminimumplatformversions.md)
  Update the relationship between a challenges minimum platform version and a specific Game Center detail.
- [Delete a Challenge](./delete-v1-gamecenterchallenges-_id_.md)
  Remove a specific Game Center challenge.
- [Read the challenges for a game center detail](./get-v1-gamecenterdetails-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center detail.
- [Read the challenges for a game center group](./get-v1-gamecentergroups-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center group.
- [List Game Center challenge IDs for a Game Center group](./get-v1-gamecentergroups-_id_-relationships-gamecenterchallenges.md)
- [Read the challenges for a game center group](./get-v1-gamecentergroups-_id_-gamecenterchallenges.md)
  Get challenge information for a specific Game Center group.
- [List Game Center challenge IDs for a Game Center group](./get-v1-gamecentergroups-_id_-relationships-gamecenterchallenges.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterchallenges-_id_-versions)*