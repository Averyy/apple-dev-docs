# Default App Clip Experience Localizations

**Framework**: App Store Connect API

Read and manage the metadata of your default App Clip experience.

#### Overview

The `appClipDefaultExperienceLocalizations` resource represents metadata that appears on your App Clip card, specific to a locale, for a default App Clip experience. For example, use this resource to read and update localized text that appears on the App Clip card.

## Topics

### Getting Metadata for Your Default App Clip Experience
- [Read localization information of a default app clip experience](get-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Get localized metadata that appears on the App Clip card of a specific default App Clip experience.
- [Read app clip card image information for a localized default app clip experience](get-v1-appclipdefaultexperiencelocalizations-_id_-appclipheaderimage.md)
  Get the image that appears on the App Clip card, specific to a locale, for a default App Clip experience.
- [Get the header image ID for an App Clip default experience localization](get-v1-appclipdefaultexperiencelocalizations-_id_-relationships-appclipheaderimage.md)
### Managing Your Default App Clip Experience’s Metadata
- [Create the localized metadata for a default app clip experience](post-v1-appclipdefaultexperiencelocalizations.md)
  Provide localized metadata that appears on the App Clip card of a default App Clip experience.
- [Modify the localization for a default app clip experience](patch-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Update localized metadata for a specific default App Clip experience.
- [Delete a default app clip experience localization](delete-v1-appclipdefaultexperiencelocalizations-_id_.md)
  Delete localized metadata that appears on the App Clip card of a default App Clip experience.
### Objects
- [object AppClipDefaultExperienceLocalization](appclipdefaultexperiencelocalization.md)
  The localized metadata for a default App Clip experience, including the subtitle displayed on the App Clip card.
- [object AppClipDefaultExperienceLocalizationResponse](appclipdefaultexperiencelocalizationresponse.md)
  The response body for endpoints that create, read, or modify a localized App Clip card subtitle.
- [object AppClipDefaultExperienceLocalizationCreateRequest](appclipdefaultexperiencelocalizationcreaterequest.md)
  The request body you use to create a Default App Clip Experience Localization.
- [object AppClipDefaultExperienceLocalizationUpdateRequest](appclipdefaultexperiencelocalizationupdaterequest.md)
  The request body for updating the localized subtitle and action button label for a default App Clip experience.
- [object AppClipDefaultExperienceLocalizationsResponse](appclipdefaultexperiencelocalizationsresponse.md)
  The response body for endpoints that list localized App Clip card subtitles for a default experience.

## See Also

- [App Clip Header Images](app-clip-header-images.md)
  Read and manage image assets that appear on the App Clip card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/default-app-clip-experience-localizations)*