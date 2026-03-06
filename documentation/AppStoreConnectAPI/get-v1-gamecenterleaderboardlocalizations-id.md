# Read leaderboard localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a leaderboard localization.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/843189c3-61a6-480a-a9d2-760a41299829/localizations
```

**Response**:

```json
{
  “data” : {
    “type” : “gameCenterLeaderboardLocalizations”,
    “id” : “5a75be8c-225a-4fd4-b51f-d33876c2c79b”,
    “attributes” : {
      “locale” : “en-US”,
      “name” : “Best Latte Art”,
      “formatterOverride” : “INTEGER”,
      “formatterSuffix” : “points”,
      “formatterSuffixSingular” : “points”
    },
    “relationships” : {
      “gameCenterLeaderboardImage” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/5a75be8c-225a-4fd4-b51f-d33876c2c79b/relationships/gameCenterLeaderboardImage”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/5a75be8c-225a-4fd4-b51f-d33876c2c79b/gameCenterLeaderboardImage”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/5a75be8c-225a-4fd4-b51f-d33876c2c79b”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/5a75be8c-225a-4fd4-b51f-d33876c2c79b”
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/{id}`

## Parameters

- `fields[gameCenterLeaderboardImages]` ([string])
- `fields[gameCenterLeaderboardLocalizations]` ([string])
- `include` ([string])

## See Also

- [Read Game Center leaderboard localization information](get-v2-gamecenterleaderboardlocalizations-_id_.md)
  Get information about a specific Game Center leaderboard localization.
- [List all images for a Game Center leaderboard localization](get-v2-gamecenterleaderboardlocalizations-_id_-image.md)
  Get a list of images for a specific Game Center leaderboard localization.
- [Get all image IDs for a Game Center leaderboard localization](get-v2-gamecenterleaderboardlocalizations-_id_-relationships-image.md)
  Get a list of image resource IDs for a specific Game Center leaderboard localization.
- [Create a Game Center leaderboard localization](post-v2-gamecenterleaderboardlocalizations.md)
  Create a Game Center leaderboard localization.
- [Modify a Game Center leaderboard localization](patch-v2-gamecenterleaderboardlocalizations-_id_.md)
  Update a specific Game Center leaderboard localization.
- [Delete a Game Center leaderboard localization](delete-v2-gamecenterleaderboardlocalizations-_id_.md)
  Delete a specific Game Center leaderboard localization.
- [Read the image for a leaderboard localization](get-v1-gamecenterleaderboardlocalizations-_id_-gamecenterleaderboardimage.md)
  Get information about the image associated with a leaderboard localization.
- [GET /v1/gameCenterLeaderboardLocalizations/{id}/relationships/gameCenterLeaderboardImage](get-v1-gamecenterleaderboardlocalizations-_id_-relationships-gamecenterleaderboardimage.md)
- [Create a leaderboard localization](post-v1-gamecenterleaderboardlocalizations.md)
  Add a new leaderboard localization.
- [Modify a leaderboard localization](patch-v1-gamecenterleaderboardlocalizations-_id_.md)
  Edit a leaderboard localization.
- [Delete a leaderboard localization](delete-v1-gamecenterleaderboardlocalizations-_id_.md)
  Delete a localization that’s associated with a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboardlocalizations-_id_)*