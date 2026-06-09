# PreReleaseVersionsWithoutIncludesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of pre-release versions, without related resources.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object PreReleaseVersionsWithoutIncludesResponse
```

## Properties

- `data` ([PrereleaseVersion]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object PrereleaseVersion](prereleaseversion.md)
  A pre-release version associated with a build, representing a development or beta software version before App Store submission.
- [object PrereleaseVersionResponse](prereleaseversionresponse.md)
  The response body for endpoints that read a single prerelease version of an app.
- [object PreReleaseVersionsResponse](prereleaseversionsresponse.md)
  A response containing a list of pre-release versions for an app.
- [object PrereleaseVersionWithoutIncludesResponse](prereleaseversionwithoutincludesresponse.md)
  A response containing a single pre-release version, without related resources.
- [object AppPreReleaseVersionsLinkagesResponse](appprereleaseversionslinkagesresponse.md)
- [object PrereleaseVersionAppLinkageResponse](prereleaseversionapplinkageresponse.md)
- [object PrereleaseVersionBuildsLinkagesResponse](prereleaseversionbuildslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/prereleaseversionswithoutincludesresponse)*