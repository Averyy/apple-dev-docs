# AppClipHeaderImageResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a single header image for a default App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipHeaderImageResponse
```

## Properties

- `data` (AppClipHeaderImage) *(required)*: The resource data.
- `included` ([AppClipDefaultExperienceLocalization]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [object AppClipHeaderImage](appclipheaderimage.md)
  The image displayed on the App Clip card for a default App Clip experience, uploaded as part of App Clip configuration.
- [object AppClipHeaderImageCreateRequest](appclipheaderimagecreaterequest.md)
  The request body you use to reserve an image asset that appears on the App Clip card of a default App Clip experience.
- [object AppClipHeaderImageUpdateRequest](appclipheaderimageupdaterequest.md)
  The request body you use to commit the image asset for a default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipheaderimageresponse)*