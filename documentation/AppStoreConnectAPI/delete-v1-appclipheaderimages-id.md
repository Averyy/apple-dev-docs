# Delete a default app clip experience image

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete the image asset that appears on the App Clip card for a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appClipHeaderImages/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app clip header image resource ID from the [`Create an app clip card image for a default app clip experience`](post-v1-appclipheaderimages.md) response.

## See Also

- [Read the app clip card image](get-v1-appclipheaderimages-_id_.md)
  Get the image that appears on the App Clip card of a default App Clip experience.
- [Create an app clip card image for a default app clip experience](post-v1-appclipheaderimages.md)
  Reserve an image asset that appears on the App Clip card of a default App Clip experience.
- [Modify an app clip card image](patch-v1-appclipheaderimages-_id_.md)
  Change the image that appears on the App Clip card of a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appclipheaderimages-_id_)*