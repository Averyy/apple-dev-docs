# Read Activity Localization Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information for a specific Game Center activity localization.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterActivityLocalizations/{id}`

## Parameters

- `fields[gameCenterActivityImages]` ([string])
- `fields[gameCenterActivityLocalizations]` ([string])
- `include` ([string])
- `fields[gameCenterActivityVersions]` ([string])

## See Also

- [Read Image Information for an Activity Localization](get-v1-gamecenteractivitylocalizations-_id_-image.md)
  Get details about the image for a specific Game Center activity localization.
- [GET /v1/gameCenterActivityLocalizations/{id}/relationships/image](get-v1-gamecenteractivitylocalizations-_id_-relationships-image.md)
- [Add an Activity Localization](post-v1-gamecenteractivitylocalizations.md)
  Add a localization for a specific Game Center activity.
- [Modify an Activity Localization](patch-v1-gamecenteractivitylocalizations-_id_.md)
  Update localization information for a specific Game Center activity.
- [Delete an Activity Localization](delete-v1-gamecenteractivitylocalizations-_id_.md)
  Remove a specific localization from a Game Center activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenteractivitylocalizations-_id_)*