# Get All Image IDs for a Game Center Leaderboard Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of image resource IDs for a specific Game Center leaderboard localization.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterLeaderboardLocalizations/{id}/relationships/image`

## Parameters

- `id` (string) *(required)*

## See Also

- [Read Game Center Leaderboard Localization Information](get-v2-gamecenterleaderboardlocalizations-_id_.md)
  Get information about a specific Game Center leaderboard localization.
- [List All Images for a Game Center Leaderboard Localization](get-v2-gamecenterleaderboardlocalizations-_id_-image.md)
  Get a list of images for a specific Game Center leaderboard localization.
- [Create a Game Center Leaderboard Localization](post-v2-gamecenterleaderboardlocalizations.md)
  Create a Game Center leaderboard localization.
- [Modify a Game Center Leaderboard Localization](patch-v2-gamecenterleaderboardlocalizations-_id_.md)
  Update a specific Game Center leaderboard localization.
- [Delete a Game Center Leaderboard Localization](delete-v2-gamecenterleaderboardlocalizations-_id_.md)
  Delete a specific Game Center leaderboard localization.
- [Read Leaderboard Localization Information](get-v1-gamecenterleaderboardlocalizations-_id_.md)
  Get information about a leaderboard localization.
- [Read the Image for a Leaderboard Localization](get-v1-gamecenterleaderboardlocalizations-_id_-gamecenterleaderboardimage.md)
  Get information about the image associated with a leaderboard localization.
- [GET /v1/gameCenterLeaderboardLocalizations/{id}/relationships/gameCenterLeaderboardImage](get-v1-gamecenterleaderboardlocalizations-_id_-relationships-gamecenterleaderboardimage.md)
- [Create a Leaderboard Localization](post-v1-gamecenterleaderboardlocalizations.md)
  Add a new leaderboard localization.
- [Modify a Leaderboard Localization](patch-v1-gamecenterleaderboardlocalizations-_id_.md)
  Edit a leaderboard localization.
- [Delete a Leaderboard Localization](delete-v1-gamecenterleaderboardlocalizations-_id_.md)
  Delete a localization that’s associated with a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterleaderboardlocalizations-_id_-relationships-image)*