# Read Game Center Leaderboard Image Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific Game Center leaderboard image.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- fields[gameCenterLeaderboardImages]:
- include:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardImages/{id}`

## Parameters

- `fields[gameCenterLeaderboardImages]` ([string])
- `fields[gameCenterLeaderboardLocalizations]` ([string])
- `include` ([string])

## See Also

- [Create a Game Center Leaderboard Image](post-v2-gamecenterleaderboardimages.md)
  Create a Game Center leaderboard image.
- [Modify a Game Center Leaderboard Image](patch-v2-gamecenterleaderboardimages-_id_.md)
  Update a specific Game Center leaderboard image.
- [Delete a Game Center Leaderboard Image](delete-v2-gamecenterleaderboardimages-_id_.md)
  Delete a specific Game Center leaderboard image.
- [Read Leaderboard Image Information](get-v1-gamecenterleaderboardimages-_id_.md)
  Get information about a leaderboard image and its upload and processing status.
- [Create a Leaderboard Image](post-v1-gamecenterleaderboardimages.md)
  Add a new leaderboard image.
- [Modify a Leaderboard Image](patch-v1-gamecenterleaderboardimages-_id_.md)
  Commit a leaderboard image after uploading it.
- [Delete a Leaderboard Image](delete-v1-gamecenterleaderboardimages-_id_.md)
  Delete an image that’s associated with a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboardimages-_id_)*