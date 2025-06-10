# Default App Clip Experience Localizations

**Framework**: App Store Connect API

Read and manage the metadata of your default App Clip experience.

#### Overview

The `appClipDefaultExperienceLocalizations` resource represents metadata that appears on your App Clip card, specific to a locale, for a default App Clip experience. For example, use this resource to read and update localized text that appears on the App Clip card.

## Topics

### Getting Metadata for Your Default App Clip Experience
- [Read Localization Information of a Default App Clip Experience](get-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Get localized metadata that appears on the App Clip card of a specific default App Clip experience.
- [Read App Clip Card Image Information for a Localized Default App Clip Experience](get-v1-appclipdefaultexperiencelocalizations-_id_-appclipheaderimage.md)
  Get the image that appears on the App Clip card, specific to a locale, for a default App Clip experience.
- [GET /v1/appClipDefaultExperienceLocalizations/{id}/relationships/appClipHeaderImage](get-v1-appclipdefaultexperiencelocalizations-_id_-relationships-appclipheaderimage.md)
### Managing Your Default App Clip Experience’s Metadata
- [Create the Localized Metadata for a Default App Clip Experience](post-v1-appclipdefaultexperiencelocalizations.md)
  Provide localized metadata that appears on the App Clip card of a default App Clip experience.
- [Modify the Localization for a Default App Clip Experience](patch-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Update localized metadata for a specific default App Clip experience.
- [Delete a Default App Clip Experience Localization](delete-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Delete localized metadata that appears on the App Clip card of a default App Clip experience.
### Objects
- [object AppClipDefaultExperienceLocalization](appclipdefaultexperiencelocalization.md)
  The data structure that represents a Default App Clip Experience Localizations resource.
- [object AppClipDefaultExperienceLocalizationResponse](appclipdefaultexperiencelocalizationresponse.md)
  A response that contains a single Default App Clip Experience Localizations resource.
- [object AppClipDefaultExperienceLocalizationCreateRequest](appclipdefaultexperiencelocalizationcreaterequest.md)
  The request body you use to create a Default App Clip Experience Localization.
- [object AppClipDefaultExperienceLocalizationUpdateRequest](appclipdefaultexperiencelocalizationupdaterequest.md)
  The request body you use to update a Default App Clip Experiences resource.
- [object AppClipDefaultExperienceLocalizationsResponse](appclipdefaultexperiencelocalizationsresponse.md)
  A response that contains a list of Default App Clip Experience Localizations resources.

## See Also

- [App Clip Header Images](app-clip-header-images.md)
  Read and manage image assets that appear on the App Clip card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/default-app-clip-experience-localizations)*