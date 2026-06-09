# Read image information for an advanced app clip experience

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about the image that appears on the App Clip card of an advanced App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClipAdvancedExperienceImages/{id}`

## Parameters

- `fields[appClipAdvancedExperienceImages]` ([string]): Additional fields to include for each Advanced App Clip Experience Images resource returned by the response.

## See Also

- [Create an app clip card image for an advanced app clip experience](post-v1-appclipadvancedexperienceimages.md)
  Reserve an image asset that appears on the App Clip card of an advanced App Clip experience.
- [Modify the image for an advanced app clip experience](patch-v1-appclipadvancedexperienceimages-_id_.md)
  Update image information or commit the image asset of an advanced App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclipadvancedexperienceimages-_id_)*