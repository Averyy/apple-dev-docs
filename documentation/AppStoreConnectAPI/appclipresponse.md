# AppClipResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that read an App Clip associated with an app.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```
object AppClipResponse
```

## Properties

- `data` (AppClip) *(required)*: The resource data.
- `included` ([*]): The requested relationship data.

  **Allowed Types**: `AppClipDefaultExperience`, `App`
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

### Objects
- [object AppClip](./appclip.md)
  A lightweight version of an app that users can launch instantly without installation, associated with a registered parent app.
- [object AppClipDefaultExperiencesResponse](./appclipdefaultexperiencesresponse.md)
  The response body for endpoints that list default App Clip experiences.
- [object AppClipAdvancedExperiencesResponse](./appclipadvancedexperiencesresponse.md)
  A response containing a list of configured App Clip advanced experiences.
- [object AppClipAppClipAdvancedExperiencesLinkagesResponse](./appclipappclipadvancedexperienceslinkagesresponse.md)
- [object AppClipAppClipDefaultExperiencesLinkagesResponse](./appclipappclipdefaultexperienceslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipresponse)*