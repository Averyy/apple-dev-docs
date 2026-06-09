# Get challenge releases for a game center detail

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all challenge release information for a specific Game Center detail.

**Availability**:
- App Store Connect API 4.0+

## Mentions

- [Configuring Game Center challenges](configuring-game-center-challenges.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterDetails/{id}/challengeReleases`

## Parameters

- `fields[gameCenterChallengeVersionReleases]` ([string])
- `fields[gameCenterChallengeVersions]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [Read challenge release ids for a game center detail](get-v1-gamecenterdetails-_id_-relationships-challengereleases.md)
  List all the challenge release IDs for a specific Game Center detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterdetails-_id_-challengereleases)*