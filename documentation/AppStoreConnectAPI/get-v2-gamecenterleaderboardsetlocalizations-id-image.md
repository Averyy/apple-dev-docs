# List All Images for a Game Center Leaderboard Set Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of images for a specific Game Center leaderboard set localization.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- fields[gameCenterLeaderboardSetImages]:
- fields[gameCenterLeaderboardSetLocalizations]:
- include:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardSetLocalizations/{id}/image`

## Parameters

- `fields[gameCenterLeaderboardSetImages]` ([string])
- `fields[gameCenterLeaderboardSetLocalizations]` ([string])
- `include` ([string])

## See Also

- [Read Game Center Leaderboard Set Localization Information](get-v2-gamecenterleaderboardsetlocalizations-_id_.md)
  Get information about a specific Game Center leaderboard set localization.
- [Get All Image IDs for a Game Center Leaderboard Set Localization](get-v2-gamecenterleaderboardsetlocalizations-_id_-relationships-image.md)
  Get a list of image resource IDs for a specific Game Center leaderboard set localization.
- [Create a Game Center Leaderboard Set Localization](post-v2-gamecenterleaderboardsetlocalizations.md)
  Create a Game Center leaderboard set localization.
- [Modify a Game Center Leaderboard Set Localization](patch-v2-gamecenterleaderboardsetlocalizations-_id_.md)
  Update a specific Game Center leaderboard set localization.
- [Delete a Game Center Leaderboard Set Localization](delete-v2-gamecenterleaderboardsetlocalizations-_id_.md)
  Delete a specific Game Center leaderboard set localization.
- [Read Leaderboard Set Localization Information](get-v1-gamecenterleaderboardsetlocalizations-_id_.md)
  Get information about a leaderboard set localization.
- [Read the Image Associated With a Leaderboard Set Localization](get-v1-gamecenterleaderboardsetlocalizations-_id_-gamecenterleaderboardsetimage.md)
  Get information about a leaderboard set image associated with a leaderboard set localization.
- [Get the leaderboard set image ID for a Game Center leaderboard set localization](get-v1-gamecenterleaderboardsetlocalizations-_id_-relationships-gamecenterleaderboardsetimage.md)
- [Create a Leaderboard Set Localization](post-v1-gamecenterleaderboardsetlocalizations.md)
  Add a new leaderboard set localization.
- [Modify a Leaderboard Set Localization](patch-v1-gamecenterleaderboardsetlocalizations-_id_.md)
  Edit a leaderboard set localization.
- [Delete a Leaderboard Set Localization](delete-v1-gamecenterleaderboardsetlocalizations-_id_.md)
  Delete a localization that’s associated with a leaderboard set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboardsetlocalizations-_id_-image)*