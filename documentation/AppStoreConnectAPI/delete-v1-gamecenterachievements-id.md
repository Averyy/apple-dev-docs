# Delete an achievement

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a specific achievement.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
DELETE https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/082314fb-8b23-49db-b62a-08aad519e5aa
```

**Response**:

```json
HTTP/1.1 204 No Content
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterAchievements/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List all achievements`](get-v1-gamecenterdetails-_id_-gamecenterachievements.md) response.

## See Also

- [Create a Game Center achievement](post-v2-gamecenterachievements.md)
  Create a Game Center achievement.
- [Modify a Game Center achievement](patch-v2-gamecenterachievements-_id_.md)
  Update a specific Game Center achievement.
- [Modify the activity for a Game Center achievement](patch-v2-gamecenterachievements-_id_-relationships-activity.md)
  Update the activity relationship for a specific Game Center achievement.
- [Delete a Game Center achievement](delete-v2-gamecenterachievements-_id_.md)
  Delete a specific Game Center achievement.
- [Create an achievement](post-v1-gamecenterachievements.md)
  Add an achievement to a Game Center detail.
- [Modify an achievement](patch-v1-gamecenterachievements-_id_.md)
  Modify properties for a specific achievement.
- [Modify the group for an achievement](patch-v1-gamecenterachievements-_id_-relationships-groupachievement.md)
  Modify the achievement group for a specific achievement.
- [PATCH /v1/gameCenterAchievements/{id}/relationships/activity](patch-v1-gamecenterachievements-_id_-relationships-activity.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecenterachievements-_id_)*