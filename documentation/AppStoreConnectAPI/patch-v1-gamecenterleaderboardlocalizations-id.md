# Modify a Leaderboard Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Edit a leaderboard localization.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

Use leaderboard formatters to specify the unit of measurement for a Game Center leaderboard. There is a new required attribute `defaultFormatter` when you use [`Create a Leaderboard`](post-v1-gamecenterleaderboards.md), which gives all your localizations the same formatter. You can also optionally use `formatterOverride` to override a specific leaderboard localization when calling [`Create a Leaderboard Localization`](post-v1-gamecenterleaderboardlocalizations.md) or [`Modify a Leaderboard Localization`](patch-v1-gamecenterleaderboardlocalizations-_id_.md).

Before App Store Connect API version 3.0, formatters were based on localizations and were required for each localization. Legacy leaderboards created before the new addition of the Game Center APIs will not have a `defaultFormatter` value, the value would be `null` in this case. Any localizations created before the new addition of the Game Center APIs will always have a `formatterOverride`.

##### Example Request and Response

**Request**:

```None
PATCH https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/5a75be8c-225a-4fd4-b51f-d33876c2c79b -d
{
    “data”: {
        “type”: “gameCenterLeaderboardLocalizations”,
        “id”: “5a75be8c-225a-4fd4-b51f-d33876c2c79b”,
        “attributes”: {
            “formatterSuffixSingular”: “point”
        }
    }
}
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
      “formatterSuffixSingular” : “point”
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

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/{id}`

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
- [GET /v1/gameCenterLeaderboardLocalizations/{id}/relationships/gameCenterLeaderboardImage](get-v1-gamecenterleaderboardlocalizations-_id_-relationships-gamecenterleaderboardimage.md)
- [Create a Leaderboard Localization](post-v1-gamecenterleaderboardlocalizations.md)
  Add a new leaderboard localization.
- [Delete a Leaderboard Localization](delete-v1-gamecenterleaderboardlocalizations-_id_.md)
  Delete a localization that’s associated with a leaderboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterleaderboardlocalizations-_id_)*