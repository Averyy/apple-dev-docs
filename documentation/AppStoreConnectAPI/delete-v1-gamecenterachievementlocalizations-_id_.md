# Delete an Achievement Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete localization metadata that’s associated with an achievement.

**Availability**:
- App Store Connect API 3.0+ - Deprecated in 4.3

> **Deprecated**: This endpoint is deprecated. Use [`Delete a Game Center Achievement Localization`](./delete-v2-gamecenterachievementlocalizations-_id_.md) instead.

## Discussion

### Example Request and Response

**Request**:

```
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

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List All Localizations for an Achievement`](./get-v1-gamecenterachievements-_id_-localizations.md) response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, modifying, and deleting achievements localizations
- [Create a Game Center Achievement Localization](./post-v2-gamecenterachievementlocalizations.md)
  Create a Game Center achievement localization.
- [Modify a Game Center Achievement Localization](./patch-v2-gamecenterachievementlocalizations-_id_.md)
  Update a specific Game Center achievement localization.
- [Delete a Game Center Achievement Localization](./delete-v2-gamecenterachievementlocalizations-_id_.md)
  Delete a specific Game Center achievement localization.
- [Create an Achievement Localization](./post-v1-gamecenterachievementlocalizations.md)
  Add Game Center achievement localized information for a new locale.
- [Edit an Achievement Localization](./patch-v1-gamecenterachievementlocalizations-_id_.md)
  Modify localized Game Center achievement information for a particular language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecenterachievementlocalizations-_id_)*