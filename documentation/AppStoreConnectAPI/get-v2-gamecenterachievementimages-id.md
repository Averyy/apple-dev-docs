# Read Game Center Achievement Image Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific Game Center achievement image.

**Availability**:
- App Store Connect API 3.6+

#### Overview

- id:
- fields[gameCenterAchievementImages]:
- include:
- 200:
- 400:
- 401:
- 403:
- 404:
- 429:

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/gameCenterAchievementImages/{id}`

## Parameters

- `fields[gameCenterAchievementImages]` ([string])
- `fields[gameCenterAchievementLocalizations]` ([string])
- `include` ([string])

## See Also

- [Create a Game Center Achievement Image](post-v2-gamecenterachievementimages.md)
  Create a Game Center achievement image.
- [Modify a Game Center Achievement Image](patch-v2-gamecenterachievementimages-_id_.md)
  Update a specific Game Center achievement image.
- [Delete a Game Center Achievement Image](delete-v2-gamecenterachievementimages-_id_.md)
  Delete a specific Game Center achievement image.
- [Read Achievement Image Information](get-v1-gamecenterachievementimages-_id_.md)
  Get information about an achievement image and its upload and processing status.
- [Create an Achievement Image](post-v1-gamecenterachievementimages.md)
  Add a new achievement image.
- [Modify an Achievement Image](patch-v1-gamecenterachievementimages-_id_.md)
  Commit an achievement image after uploading it.
- [Delete an Achievement Image](delete-v1-gamecenterachievementimages-_id_.md)
  Delete an image that’s associated with an achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-gamecenterachievementimages-_id_)*