# Read Achievement Localization Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read localized information for a specific locale for a specific achievement.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f
```

**Response**:

```json
{
  “data” : {
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
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f”
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/{id}`

## Parameters

- `fields[gameCenterAchievementImages]` ([string])
- `fields[gameCenterAchievementLocalizations]` ([string])
- `fields[gameCenterAchievements]` ([string])
- `include` ([string])

## See Also

- [Read Game Center Achievement Localization Information](get-v2-gamecenterachievementlocalizations-_id_.md)
  Get information about a specific Game Center achievement localization.
- [List All Images for a Game Center Achievement Localization](get-v2-gamecenterachievementlocalizations-_id_-image.md)
  Get a list of images for a specific Game Center achievement localization.
- [Get All Image IDs for a Game Center Achievement Localization](get-v2-gamecenterachievementlocalizations-_id_-relationships-image.md)
  Get a list of image resource IDs for a specific Game Center achievement localization.
- [List All Localizations for an Achievement](get-v1-gamecenterachievements-_id_-localizations.md)
  Read information about the release for specific achievement.
- [GET /v1/gameCenterAchievements/{id}/relationships/localizations](get-v1-gamecenterachievements-_id_-relationships-localizations.md)
- [Read the Achievement Localization Information](get-v1-gamecenterachievementlocalizations-_id_-gamecenterachievement.md)
  Read the achievement associated with specific localized information.
- [Read the Achievement ID for a Localization](get-v1-gamecenterachievementlocalizations-_id_-relationships-gamecenterachievement.md)
  Read the achievement ID associated with specific localized information.
- [Read the Image for a Specific Achievement Localization](get-v1-gamecenterachievementlocalizations-_id_-gamecenterachievementimage.md)
  Read the achievement image associated with specific localized information.
- [GET /v1/gameCenterAchievementLocalizations/{id}/relationships/gameCenterAchievementImage](get-v1-gamecenterachievementlocalizations-_id_-relationships-gamecenterachievementimage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterachievementlocalizations-_id_)*