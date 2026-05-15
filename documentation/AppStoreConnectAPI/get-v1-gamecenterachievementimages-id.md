# Read Achievement Image Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about an achievement image and its upload and processing status.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/gameCenterAchievementImages/38e6d9a7-9cbf-45f8-8246-1ef4728aecda
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
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAchievementImages/38e6d9a7-9cbf-45f8-8246-1ef4728aecda”
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAchievementImages/{id}`

## Parameters

- `fields[gameCenterAchievementImages]` ([string])
- `include` ([string])
- `fields[gameCenterAchievementLocalizations]` ([string])

## See Also

- [Read Game Center Achievement Image Information](get-v2-gamecenterachievementimages-_id_.md)
  Get information about a specific Game Center achievement image.
- [Create a Game Center Achievement Image](post-v2-gamecenterachievementimages.md)
  Create a Game Center achievement image.
- [Modify a Game Center Achievement Image](patch-v2-gamecenterachievementimages-_id_.md)
  Update a specific Game Center achievement image.
- [Delete a Game Center Achievement Image](delete-v2-gamecenterachievementimages-_id_.md)
  Delete a specific Game Center achievement image.
- [Create an Achievement Image](post-v1-gamecenterachievementimages.md)
  Add a new achievement image.
- [Modify an Achievement Image](patch-v1-gamecenterachievementimages-_id_.md)
  Commit an achievement image after uploading it.
- [Delete an Achievement Image](delete-v1-gamecenterachievementimages-_id_.md)
  Delete an image that’s associated with an achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterachievementimages-_id_)*