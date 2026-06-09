# AppClipAdvancedExperiencesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of configured App Clip advanced experiences.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipAdvancedExperiencesResponse
```

## Properties

- `data` ([AppClipAdvancedExperience]) *(required)*: The resource data.
- `included` ([*]): The requested relationship data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): The paging information.

## See Also

- [object AppClip](appclip.md)
  A lightweight version of an app that users can launch instantly without installation, associated with a registered parent app.
- [object AppClipResponse](appclipresponse.md)
  The response body for endpoints that read an App Clip associated with an app.
- [object AppClipDefaultExperiencesResponse](appclipdefaultexperiencesresponse.md)
  The response body for endpoints that list default App Clip experiences.
- [object AppClipAppClipAdvancedExperiencesLinkagesResponse](appclipappclipadvancedexperienceslinkagesresponse.md)
- [object AppClipAppClipDefaultExperiencesLinkagesResponse](appclipappclipdefaultexperienceslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipadvancedexperiencesresponse)*