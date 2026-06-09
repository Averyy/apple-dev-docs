# List All Localizations for an Achievement

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read information about the release for specific achievement.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/304e0f56-63b2-492f-980e-bce6fafb8502/localizations
```

**Response**:

```json
{
  “data” : [ {
    “type” : “gameCenterAchievementLocalizations”,
    “id” : “772571ca-01fe-47d6-bcda-bd3ead58ea14”,
    “attributes” : {
      “locale” : “en-CA”,
      “name” : “Perfectly steamed milk”,
      “beforeEarnedDescription” : “You can earn this achievement upon steaming milk to the perfect texture.”,
      “afterEarnedDescription” : “You did it! The milk had the perfect texture.”
    },
    “relationships” : {
      “gameCenterAchievement” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/772571ca-01fe-47d6-bcda-bd3ead58ea14/relationships/gameCenterAchievement”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/772571ca-01fe-47d6-bcda-bd3ead58ea14/gameCenterAchievement”
        }
      },
      “gameCenterAchievementImage” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/772571ca-01fe-47d6-bcda-bd3ead58ea14/relationships/gameCenterAchievementImage”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/772571ca-01fe-47d6-bcda-bd3ead58ea14/gameCenterAchievementImage”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/772571ca-01fe-47d6-bcda-bd3ead58ea14”
    }
  }, {
    “type” : “gameCenterAchievementLocalizations”,
    “id” : “ca329301-e7ad-4784-97cd-02faade43c2f”,
    “attributes” : {
      “locale” : “en-US”,
      “name” : “Perfectly steamed milk”,
      “beforeEarnedDescription” : “You can earn this achievement upon steaming milk to the perfect texture.”,
      “afterEarnedDescription” : “You did it! The milk had the perfect texture.”
    },
    “relationships” : {
      “gameCenterAchievement” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f/relationships/gameCenterAchievement”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f/gameCenterAchievement”
        }
      },
      “gameCenterAchievementImage” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f/relationships/gameCenterAchievementImage”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f/gameCenterAchievementImage”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f”
    }
  } ],
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/304e0f56-63b2-492f-980e-bce6fafb8502/localizations”
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

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/{id}/localizations`

## Parameters

- `fields[gameCenterAchievementImages]` ([string])
- `fields[gameCenterAchievementLocalizations]` ([string])
- `fields[gameCenterAchievements]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [Read Game Center Achievement Information](get-v2-gamecenterachievements-_id_.md)
  Get information about a specific Game Center achievement.
- [List All Versions for a Game Center Achievement](get-v2-gamecenterachievements-_id_-versions.md)
  Get a list of versions for a specific Game Center achievement.
- [Get All Version IDs for a Game Center Achievement](get-v2-gamecenterachievements-_id_-relationships-versions.md)
  Get a list of version resource IDs for a specific Game Center achievement.
- [List All Achievements](get-v1-gamecenterdetails-_id_-gamecenterachievements.md)
  List all achievement information for a Game Center detail.
- [Read Achievement Information](get-v1-gamecenterachievements-_id_.md)
  Read information about a specific Game Center achievement.
- [Read Release Information for an Achievement](get-v1-gamecenterachievements-_id_-releases.md)
  Read the state of an achievement release and related information.
- [List release IDs for a Game Center achievement](get-v1-gamecenterachievements-_id_-relationships-releases.md)
- [List Associated Group Achievement Information for an Achievement](get-v1-gamecenterachievements-_id_-groupachievement.md)
  Read information about the group for specific achievement.
- [List Group Achievements for an Achievement](get-v1-gamecenterachievements-_id_-relationships-groupachievement.md)
  List associated group achievements for a specific achievement.
- [List achievement releases](get-v1-gamecenterdetails-_id_-achievementreleases.md)
  Read information about the achievement releases for specific Game Center detail.
- [List achievement release IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-achievementreleases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterachievements-_id_-localizations)*