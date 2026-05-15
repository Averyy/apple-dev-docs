# Read Game Center Leaderboard Set Image Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific Game Center leaderboard set image.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- fields[gameCenterLeaderboardSetImages]:
- include:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardSetImages/{id}`

## Parameters

- `fields[gameCenterLeaderboardSetImages]` ([string])
- `fields[gameCenterLeaderboardSetLocalizations]` ([string])
- `include` ([string])

## See Also

- [Create a Game Center Leaderboard Set Image](post-v2-gamecenterleaderboardsetimages.md)
  Create a Game Center leaderboard set image.
- [Modify a Game Center Leaderboard Set Image](patch-v2-gamecenterleaderboardsetimages-_id_.md)
  Update a specific Game Center leaderboard set image.
- [Delete a Game Center Leaderboard Set Image](delete-v2-gamecenterleaderboardsetimages-_id_.md)
  Delete a specific Game Center leaderboard set image.
- [Read Leaderboard Set Image Information](get-v1-gamecenterleaderboardsetimages-_id_.md)
  Get information about a leaderboard set image and its upload and processing status.
- [Create a Leaderboard Set Image](post-v1-gamecenterleaderboardsetimages.md)
  Add a new leaderboard set image.
- [Modify a Leaderboard Set Image](patch-v1-gamecenterleaderboardsetimages-_id_.md)
  Commit a leaderboard set image after uploading it.
- [Delete a Leaderboard Set Image](delete-v1-gamecenterleaderboardsetimages-_id_.md)
  Delete an image that’s associated with a leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboardsetimages-_id_)*