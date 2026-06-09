# List All Localizations for a Leaderboard

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of localized metadata for a leaderboard.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/9b999364-308b-4ca3-8214-0af6cf5a6d51/localizations
```

**Response**:

```json
{
  “data” : [ {
    “type” : “gameCenterLeaderboardLocalizations”,
    “id” : “9b999364-308b-4ca3-8214-0af6cf5a6d51”,
    “attributes” : {
      “locale” : “en-CA”,
      “name” : “Best Latte Art”,
      “formatterOverride” : “INTEGER”,
      “formatterSuffix” : “points”,
      “formatterSuffixSingular” : “points”
    },
    “relationships” : {
      “gameCenterLeaderboardImage” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/9b999364-308b-4ca3-8214-0af6cf5a6d51/relationships/gameCenterLeaderboardImage”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/9b999364-308b-4ca3-8214-0af6cf5a6d51/gameCenterLeaderboardImage”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboardLocalizations/9b999364-308b-4ca3-8214-0af6cf5a6d51”
    }
  }, {
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
  } ],
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/843189c3-61a6-480a-a9d2-760a41299829/localizations”
  },
  “meta” : {
    “paging” : {
      “total” : 2,
      “limit” : 50
    }
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterLeaderboards/{id}/localizations`

## Parameters

- `fields[gameCenterLeaderboardImages]` ([string])
- `fields[gameCenterLeaderboardLocalizations]` ([string])
- `fields[gameCenterLeaderboards]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [Read Game Center Leaderboard Information](get-v2-gamecenterleaderboards-_id_.md)
  Get information about a specific Game Center leaderboard.
- [List All Versions for a Game Center Leaderboard](get-v2-gamecenterleaderboards-_id_-versions.md)
  Get a list of versions for a specific Game Center leaderboard.
- [Get All Version IDs for a Game Center Leaderboard](get-v2-gamecenterleaderboards-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center leaderboard.
- [Read Leaderboard Information](get-v1-gamecenterleaderboards-_id_.md)
  Read information about a specific leaderboard.
- [Read Group Information for a Leaderboard](get-v1-gamecenterleaderboards-_id_-groupleaderboard.md)
  Read the group leadboard to which a leaderboard belongs.
- [List localization IDs for a Game Center leaderboard](get-v1-gamecenterleaderboards-_id_-relationships-localizations.md)
- [List all groups to which a leaderboard belongs](get-v1-gamecenterleaderboards-_id_-relationships-groupleaderboard.md)
  List associated group leaderboards for a specific leaderboard.
- [List Releases for a Leaderboard](get-v1-gamecenterleaderboards-_id_-releases.md)
  Read the state of releases for a leaderboard and related information.
- [List release IDs for a Game Center leaderboard](get-v1-gamecenterleaderboards-_id_-relationships-releases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterleaderboards-_id_-localizations)*