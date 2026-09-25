# List Score Moderations for a Leaderboard

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the score moderations for a leaderboard.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5 release notes](app-store-connect-api-4-5-release-notes.md)

#### Overview

The response contains a list of [`GameCenterScoreModeration`](gamecenterscoremoderation.md) resources in a [`GameCenterScoreModerationsResponse`](gamecenterscoremoderationsresponse.md).

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboards/{id}/gameCenterScoreModerations`

## Parameters

- `exists[blocked]` (boolean): Filter the returned score moderations to include only those that are blocked (true) or not blocked (false).
- `fields[gameCenterScoreModerations]` ([string]): Additional fields to include for each gameCenterScoreModerations resource returned by the response.
- `fields[gameCenterDetailPlayers]` ([string]): Additional fields to include for each gameCenterDetailPlayers resource returned by the response.
- `limit` (integer): The maximum number of score moderation resources to return.
- `include` ([string]): The relationship data to include in the response.

## See Also

- [List Score Moderation IDs for a Game Center Leaderboard](get-v2-gamecenterleaderboards-_id_-relationships-gamecenterscoremoderations.md)
  List the score moderation IDs for a Game Center leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboards-_id_-gamecenterscoremoderations)*