# Advanced App Clip Experiences

**Framework**: App Store Connect API

Create, read, update, and delete your advanced App Clip experiences.

#### Overview

The `appClipAdvancedExperiences` resource represents an advanced App Clip experience. You use it to access an advanced App Clip experience you already created, create a new advanced App Clip experience, or update an existing advanced App Clip experience. Additionally, you can use the resource’s `PATCH` operation to delete an unreleased advanced App Clip experience.

## Topics

### Getting and Managing Advanced App Clip Experiences
- [Read advanced app clip experience information](get-v1-appclipadvancedexperiences-_id_.md)
  Get information about a specific advanced App Clip experience.
- [Create an advanced app clip experience](post-v1-appclipadvancedexperiences.md)
  Configure a new advanced App Clip experience.
- [Modify and delete an advanced app clip experience](patch-v1-appclipadvancedexperiences-_id_.md)
  Update and delete an existing advanced App Clip experience.
### Managing Advanced App Clip Experience Metadata
- [Advanced App Clip Experience Images](advanced-app-clip-experience-images.md)
  Read, create, and update imagery that appears on the App Clip card for advanced App Clip experiences.
### Objects and types
- [object AppClipAdvancedExperience](appclipadvancedexperience.md)
  A configured trigger for an App Clip experience, associated with a physical location, NFC tag, QR code, or App Store link.
- [object AppClipAdvancedExperienceResponse](appclipadvancedexperienceresponse.md)
  A response containing a single App Clip advanced experience configuration.
- [object AppClipAdvancedExperienceLocalization](appclipadvancedexperiencelocalization.md)
  The localized text and action button label for an App Clip advanced experience in a specific language.
- [object AppClipAdvancedExperienceCreateRequest](appclipadvancedexperiencecreaterequest.md)
  The request body you use to create an advanced App Clip experience.
- [object AppClipAdvancedExperienceUpdateRequest](appclipadvancedexperienceupdaterequest.md)
  The request body you use to update an advanced App Clip experience.
- [type AppClipAdvancedExperienceLanguage](appclipadvancedexperiencelanguage.md)
  A string value identifying the language for an App Clip advanced experience localization.

## See Also

- [Default App Clip Experiences](default-app-clip-experiences.md)
  Read, create, update, and delete your default App Clip experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/advanced-app-clip-experiences)*