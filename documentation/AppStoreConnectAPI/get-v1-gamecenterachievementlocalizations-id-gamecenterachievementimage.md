# Read the image for a specific achievement localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read the achievement image associated with specific localized information.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f/gameCenterAchievementImage
```

**Response**:

```json
{
  “data” : {
    “type” : “gameCenterAchievementImages”,
    “id” : “38e6d9a7-9cbf-45f8-8246-1ef4728aecda”,
    “attributes” : {
      “fileSize” : 357407,
      “fileName” : “coffee1.png”,
      “imageAsset” : {
        “templateUrl” : “https://isq11.mzstatic.com/image/thumb/PurpleSource113/v4/64/14/07/641407e3-602f-ce23-10b8-c91b1762986c/38e6d9a7-9cbf-45f8-8246-1ef4728aecda_coffee1.png/{w}x{h}bb.{f}”,
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
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementImages/38e6d9a7-9cbf-45f8-8246-1ef4728aecda”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f/gameCenterAchievementImage”
  }

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/{id}/gameCenterAchievementImage`

## Parameters

- `fields[gameCenterAchievementImages]` ([string])
- `fields[gameCenterAchievementLocalizations]` ([string])
- `include` ([string])

## See Also

- [Read Game Center achievement localization information](get-v2-gamecenterachievementlocalizations-_id_.md)
  Get information about a specific Game Center achievement localization.
- [List all images for a Game Center achievement localization](get-v2-gamecenterachievementlocalizations-_id_-image.md)
  Get a list of images for a specific Game Center achievement localization.
- [Get all image IDs for a Game Center achievement localization](get-v2-gamecenterachievementlocalizations-_id_-relationships-image.md)
  Get a list of image resource IDs for a specific Game Center achievement localization.
- [List all localizations for an achievement](get-v1-gamecenterachievements-_id_-localizations.md)
  Read information about the release for specific achievement.
- [GET /v1/gameCenterAchievements/{id}/relationships/localizations](get-v1-gamecenterachievements-_id_-relationships-localizations.md)
- [Read achievement localization information](get-v1-gamecenterachievementlocalizations-_id_.md)
  Read localized information for a specific locale for a specific achievement.
- [Read the achievement localization information](get-v1-gamecenterachievementlocalizations-_id_-gamecenterachievement.md)
  Read the achievement associated with specific localized information.
- [Read the achievement ID for a  localization](get-v1-gamecenterachievementlocalizations-_id_-relationships-gamecenterachievement.md)
  Read the achievement ID associated with specific localized information.
- [GET /v1/gameCenterAchievementLocalizations/{id}/relationships/gameCenterAchievementImage](get-v1-gamecenterachievementlocalizations-_id_-relationships-gamecenterachievementimage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterachievementlocalizations-_id_-gamecenterachievementimage)*