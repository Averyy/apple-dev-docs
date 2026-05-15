# Create an Achievement Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add Game Center achievement localized information for a new locale.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
POST https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations -d {
    “data”: {
        “type”: “gameCenterAchievementLocalizations”,
        “attributes”: {
            “locale”: “en-US”,
            “name”: “Perfectly steamed milk”,
            “afterEarnedDescription”: “You did it! The milk had the perfect texture.”,
            “beforeEarnedDescription”: “You will earn this achievement upon steaming milk to the perfect texture.”
        },
        “relationships”: {
            “gameCenterAchievement”: {
                “data”: {
                    “type”: “gameCenterAchievements”,
                    “id”: “304e0f56-63b2-492f-980e-bce6fafb8502”
                }
            }
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
      “beforeEarnedDescription” : “You will earn this achievement upon steaming milk to the perfect texture.”,
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
    “self” : “https://appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations”
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations`

## See Also

- [Create a Game Center Achievement Localization](post-v2-gamecenterachievementlocalizations.md)
  Create a Game Center achievement localization.
- [Modify a Game Center Achievement Localization](patch-v2-gamecenterachievementlocalizations-_id_.md)
  Update a specific Game Center achievement localization.
- [Delete a Game Center Achievement Localization](delete-v2-gamecenterachievementlocalizations-_id_.md)
  Delete a specific Game Center achievement localization.
- [Edit an Achievement Localization](patch-v1-gamecenterachievementlocalizations-_id_.md)
  Modify localized Game Center achievement information for a particular language.
- [Delete an Achievement Localization](delete-v1-gamecenterachievementlocalizations-_id_.md)
  Delete localization metadata that’s associated with an achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-gamecenterachievementlocalizations)*