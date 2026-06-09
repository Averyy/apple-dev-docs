# Delete a Leaderboard Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a localization that’s associated with a leaderboard.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
DELETE https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/5a75be8c-225a-4fd4-b51f-d33876c2c79b
```

**Response**:

```json
HTTP/1.1 204 No Content
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Read Game Center Leaderboard Localization Information](get-v2-gamecenterleaderboardlocalizations-_id_.md)
  Get information about a specific Game Center leaderboard localization.
- [List All Images for a Game Center Leaderboard Localization](get-v2-gamecenterleaderboardlocalizations-_id_-image.md)
  Get a list of images for a specific Game Center leaderboard localization.
- [Get All Image IDs for a Game Center Leaderboard Localization](get-v2-gamecenterleaderboardlocalizations-_id_-relationships-image.md)
  Get a list of image resource IDs for a specific Game Center leaderboard localization.
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
- [Get the leaderboard image ID for a Game Center leaderboard localization](get-v1-gamecenterleaderboardlocalizations-_id_-relationships-gamecenterleaderboardimage.md)
- [Create a Leaderboard Localization](post-v1-gamecenterleaderboardlocalizations.md)
  Add a new leaderboard localization.
- [Modify a Leaderboard Localization](patch-v1-gamecenterleaderboardlocalizations-_id_.md)
  Edit a leaderboard localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecenterleaderboardlocalizations-_id_)*