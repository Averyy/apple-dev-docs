# Modify an achievement image

**Framework**: App Store Connect API  
**Kind**: httpRequest

Commit an achievement image after uploading it.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterAchievementImages/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the Game Center achievement images resource ID from the [`Read achievement information`](get-v1-gamecenterachievements-_id_.md) response.

## See Also

- [Read Game Center achievement image information](get-v2-gamecenterachievementimages-_id_.md)
  Get information about a specific Game Center achievement image.
- [Create a Game Center achievement image](post-v2-gamecenterachievementimages.md)
  Create a Game Center achievement image.
- [Modify a Game Center achievement image](patch-v2-gamecenterachievementimages-_id_.md)
  Update a specific Game Center achievement image.
- [Delete a Game Center achievement image](delete-v2-gamecenterachievementimages-_id_.md)
  Delete a specific Game Center achievement image.
- [Read achievement image information](get-v1-gamecenterachievementimages-_id_.md)
  Get information about an achievement image and its upload and processing status.
- [Create an achievement image](post-v1-gamecenterachievementimages.md)
  Add a new achievement image.
- [Delete an achievement image](delete-v1-gamecenterachievementimages-_id_.md)
  Delete an image that’s associated with an achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterachievementimages-_id_)*