# Read the Image for a Leaderboard Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about the image associated with a leaderboard localization.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/5a75be8c-225a-4fd4-b51f-d33876c2c79b/gameCenterLeaderboardImage
```

**Response**:

```json
{
  “data” : {
    “type” : “gameCenterLeaderboardImages”,
    “id” : “482f6124-4570-43a0-aa5e-ec289ba6faf8”,
    “attributes” : {
      “fileSize” : 357407,
      “fileName” : “coffee2.png”,
      “imageAsset” : {
        “templateUrl” : “https://isq11.mzstatic.com/image/thumb/PurpleSource113/v4/ad/e2/7b/ade27bd0-013d-86ef-2748-9d63b53e781e/482f6124-4570-43a0-aa5e-ec289ba6faf8_coffee2.png/{w}x{h}bb.{f}”,
        “width” : 512,
        “height” : 512
      },
      “uploadOperations” : [ ],
      “assetDeliveryState” : {
        “errors” : null,
        “warnings” : null,
        “state” : “COMPLETE”
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardImages/482f6124-4570-43a0-aa5e-ec289ba6faf8”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/5a75be8c-225a-4fd4-b51f-d33876c2c79b/gameCenterLeaderboardImage”
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/{id}/gameCenterLeaderboardImage`

## Parameters

- `fields[gameCenterLeaderboardImages]` ([string])
- `fields[gameCenterLeaderboardLocalizations]` ([string])
- `include` ([string])

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
- [GET /v1/gameCenterLeaderboardLocalizations/{id}/relationships/gameCenterLeaderboardImage](get-v1-gamecenterleaderboardlocalizations-_id_-relationships-gamecenterleaderboardimage.md)
- [Create a Leaderboard Localization](post-v1-gamecenterleaderboardlocalizations.md)
  Add a new leaderboard localization.
- [Modify a Leaderboard Localization](patch-v1-gamecenterleaderboardlocalizations-_id_.md)
  Edit a leaderboard localization.
- [Delete a Leaderboard Localization](delete-v1-gamecenterleaderboardlocalizations-_id_.md)
  Delete a localization that’s associated with a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboardlocalizations-_id_-gamecenterleaderboardimage)*