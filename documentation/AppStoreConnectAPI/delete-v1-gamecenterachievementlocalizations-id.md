# Delete an achievement localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete localization metadata that’s associated with an achievement.

**Availability**:
- App Store Connect API 3.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
DELETE https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/ca329301-e7ad-4784-97cd-02faade43c2f -d
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
HTTP/1.1 204 No Content
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterAchievementLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List all localizations for an achievement`](get-v1-gamecenterachievements-_id_-localizations.md) response.

## See Also

- [Create a Game Center achievement localization](post-v2-gamecenterachievementlocalizations.md)
  Create a Game Center achievement localization.
- [Modify a Game Center achievement localization](patch-v2-gamecenterachievementlocalizations-_id_.md)
  Update a specific Game Center achievement localization.
- [Delete a Game Center achievement localization](delete-v2-gamecenterachievementlocalizations-_id_.md)
  Delete a specific Game Center achievement localization.
- [Create an achievement localization](post-v1-gamecenterachievementlocalizations.md)
  Add Game Center achievement localized information for a new locale.
- [Edit an achievement localization](patch-v1-gamecenterachievementlocalizations-_id_.md)
  Modify localized Game Center achievement information for a particular language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecenterachievementlocalizations-_id_)*