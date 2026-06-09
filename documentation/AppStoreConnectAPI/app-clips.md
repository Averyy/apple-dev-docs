# App Clips

**Framework**: App Store Connect API

Read App Clip and App Clip experience information.

#### Overview

The `appClips` resource represents an App Clip and its associated App Clip experiences. Use this resource to access existing App Clip metadata and to create, update, or delete App Clip experiences.

## Topics

### Reading App Clip Information
- [Read app clip information](get-v1-appclips-_id_.md)
  Get a specific App Clip.
### Getting App Clip Experiences
- [List all default app clip experiences for an app clip](get-v1-appclips-_id_-appclipdefaultexperiences.md)
  Get all default App Clip experiences for an App Clip.
- [List all advanced app clip experiences for an app clip](get-v1-appclips-_id_-appclipadvancedexperiences.md)
  Get all advanced App Clip experiences for an App Clip.
- [List App Clip advanced experience IDs for an App Clip](get-v1-appclips-_id_-relationships-appclipadvancedexperiences.md)
- [List default experience IDs for an App Clip](get-v1-appclips-_id_-relationships-appclipdefaultexperiences.md)
### Objects
- [object AppClip](appclip.md)
  A lightweight version of an app that users can launch instantly without installation, associated with a registered parent app.
- [object AppClipResponse](appclipresponse.md)
  The response body for endpoints that read an App Clip associated with an app.
- [object AppClipDefaultExperiencesResponse](appclipdefaultexperiencesresponse.md)
  The response body for endpoints that list default App Clip experiences.
- [object AppClipAdvancedExperiencesResponse](appclipadvancedexperiencesresponse.md)
  A response containing a list of configured App Clip advanced experiences.
- [object AppClipAppClipAdvancedExperiencesLinkagesResponse](appclipappclipadvancedexperienceslinkagesresponse.md)
- [object AppClipAppClipDefaultExperiencesLinkagesResponse](appclipappclipdefaultexperienceslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-clips)*