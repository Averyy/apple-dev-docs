# Modify the Group for an Achievement

**Framework**: App Store Connect API  
**Kind**: httpRequest

Modify the achievement group for a specific achievement.

**Availability**:
- App Store Connect API 3.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/{id}/relationships/groupAchievement`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List All Achievements`](get-v1-gamecenterdetails-_id_-gamecenterachievements.md) response.

## See Also

- [Create a Game Center Achievement](post-v2-gamecenterachievements.md)
  Create a Game Center achievement.
- [Modify a Game Center Achievement](patch-v2-gamecenterachievements-_id_.md)
  Update a specific Game Center achievement.
- [Modify the Activity for a Game Center Achievement](patch-v2-gamecenterachievements-_id_-relationships-activity.md)
  Update the activity relationship for a specific Game Center achievement.
- [Delete a Game Center Achievement](delete-v2-gamecenterachievements-_id_.md)
  Delete a specific Game Center achievement.
- [Create an Achievement](post-v1-gamecenterachievements.md)
  Add an achievement to a Game Center detail.
- [Modify an Achievement](patch-v1-gamecenterachievements-_id_.md)
  Modify properties for a specific achievement.
- [Modify the activity for a Game Center achievement](patch-v1-gamecenterachievements-_id_-relationships-activity.md)
- [Delete an Achievement](delete-v1-gamecenterachievements-_id_.md)
  Delete a specific achievement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-gamecenterachievements-_id_-relationships-groupachievement)*