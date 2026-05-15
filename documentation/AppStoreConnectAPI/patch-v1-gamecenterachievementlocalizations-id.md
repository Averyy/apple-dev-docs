# Edit an Achievement Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Modify localized Game Center achievement information for a particular language.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
PATCH https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f -d
{
    “data”: {
        “type”: “gameCenterAchievementLocalizations”,
        “id”: “ca329301-e7ad-4784-97cd-02faade43c2f”,
        “attributes”: {
            “beforeEarnedDescription”: “You can earn this achievement upon steaming milk to the perfect texture.”
        }
    }
}
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
          “self” : “https://appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f/relationships/gameCenterAchievement”,
          “related” : “https://appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f/gameCenterAchievement”
        }
      },
      “gameCenterAchievementImage” : {
        “links” : {
          “self” : “https://appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f/relationships/gameCenterAchievementImage”,
          “related” : “https://appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f/gameCenterAchievementImage”
        }
      }
    },
    “links” : {
      “self” : “https://appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f”
    }
  },
  “links” : {
    “self” : “https://appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f”
  }
}
```

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List All Localizations for an Achievement`](get-v1-gamecenterachievements-_id_-localizations.md) response.

## See Also

- [Create a Game Center Achievement Localization](post-v2-gamecenterachievementlocalizations.md)
  Create a Game Center achievement localization.
- [Modify a Game Center Achievement Localization](patch-v2-gamecenterachievementlocalizations-_id_.md)
  Update a specific Game Center achievement localization.
- [Delete a Game Center Achievement Localization](delete-v2-gamecenterachievementlocalizations-_id_.md)
  Delete a specific Game Center achievement localization.
- [Create an Achievement Localization](post-v1-gamecenterachievementlocalizations.md)
  Add Game Center achievement localized information for a new locale.
- [Delete an Achievement Localization](delete-v1-gamecenterachievementlocalizations-_id_.md)
  Delete localization metadata that’s associated with an achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterachievementlocalizations-_id_)*