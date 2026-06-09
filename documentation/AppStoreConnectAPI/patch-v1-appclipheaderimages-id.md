# Modify an app clip card image

**Framework**: App Store Connect API  
**Kind**: httpRequest

Change the image that appears on the App Clip card of a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appClipHeaderImages/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app clip header image resource ID from the [`Create an app clip card image for a default app clip experience`](post-v1-appclipheaderimages.md) response.

## Request Body

The request body you use to update the image asset of an App Clip experience.

## See Also

- [Read the app clip card image](get-v1-appclipheaderimages-_id_.md)
  Get the image that appears on the App Clip card of a default App Clip experience.
- [Create an app clip card image for a default app clip experience](post-v1-appclipheaderimages.md)
  Reserve an image asset that appears on the App Clip card of a default App Clip experience.
- [Delete a default app clip experience image](delete-v1-appclipheaderimages-_id_.md)
  Delete the image asset that appears on the App Clip card for a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appclipheaderimages-_id_)*