# Read the app clip card image

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the image that appears on the App Clip card of a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipHeaderImages/{id}`

## Parameters

- `fields[appClipHeaderImages]` ([string]): Additional fields to include for each app clip header image resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[appClipDefaultExperienceLocalizations]` ([string])

## See Also

- [Create an app clip card image for a default app clip experience](post-v1-appclipheaderimages.md)
  Reserve an image asset that appears on the App Clip card of a default App Clip experience.
- [Modify an app clip card image](patch-v1-appclipheaderimages-_id_.md)
  Change the image that appears on the App Clip card of a default App Clip experience.
- [Delete a default app clip experience image](delete-v1-appclipheaderimages-_id_.md)
  Delete the image asset that appears on the App Clip card for a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipheaderimages-_id_)*