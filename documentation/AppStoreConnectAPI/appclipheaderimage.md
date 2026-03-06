# AppClipHeaderImage

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents the image that appears on the App Clip card of a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipHeaderImage
```

## Topics

### Objects
- [object AppClipHeaderImage.Attributes](appclipheaderimage/attributes-data.dictionary.md)
  The attributes that describe the image that appears on the App Clip card of a default App Clip experience.
- [object AppClipHeaderImage.Relationships](appclipheaderimage/relationships-data.dictionary.md)
  The relationships of the App Clip Header Images resource you included in the request and those on which you can operate.

## Properties

- `attributes` (AppClipHeaderImage.Attributes): The attributes that describe the App Clip Header Images resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies an App Clip Header Images resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (AppClipHeaderImage.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object AppClipHeaderImageResponse](appclipheaderimageresponse.md)
  A response that contains a single App Clip Header Images resource.
- [object AppClipHeaderImageCreateRequest](appclipheaderimagecreaterequest.md)
  The request body you use to reserve an image asset that appears on the App Clip card of a default App Clip experience.
- [object AppClipHeaderImageUpdateRequest](appclipheaderimageupdaterequest.md)
  The request body you use to commit the image asset for a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipheaderimage)*