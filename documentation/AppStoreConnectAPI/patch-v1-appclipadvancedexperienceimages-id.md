# Modify the image for an advanced app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update image information or commit the image asset of an advanced App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appClipAdvancedExperienceImages/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the advanced App Clip experience image resource ID from the [`Create an app clip card image for an advanced app clip experience`](post-v1-appclipadvancedexperienceimages.md) response.

## Request Body

The request body you use to update the image asset for an advanced App Clip experience.

## See Also

- [Read image information for an advanced app clip experience](get-v1-appclipadvancedexperienceimages-_id_.md)
  Get information about the image that appears on the App Clip card of an advanced App Clip experience.
- [Create an app clip card image for an advanced app clip experience](post-v1-appclipadvancedexperienceimages.md)
  Reserve an image asset that appears on the App Clip card of an advanced App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appclipadvancedexperienceimages-_id_)*