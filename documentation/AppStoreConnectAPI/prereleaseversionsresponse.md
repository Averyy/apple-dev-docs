# PreReleaseVersionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of pre-release versions for an app.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object PreReleaseVersionsResponse
```

## Properties

- `data` ([PrereleaseVersion]) *(required)*: The resource data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.
- `included` ([*])

## See Also

- [List prerelease versions](get-v1-prereleaseversions.md)
  Get a list of prerelease versions for all apps.
- [object PrereleaseVersion](prereleaseversion.md)
  A pre-release version associated with a build, representing a development or beta software version before App Store submission.
- [object PrereleaseVersionResponse](prereleaseversionresponse.md)
  The response body for endpoints that read a single prerelease version of an app.
- [object PrereleaseVersionWithoutIncludesResponse](prereleaseversionwithoutincludesresponse.md)
  A response containing a single pre-release version, without related resources.
- [object PreReleaseVersionsWithoutIncludesResponse](prereleaseversionswithoutincludesresponse.md)
  A response containing a list of pre-release versions, without related resources.
- [object AppPreReleaseVersionsLinkagesResponse](appprereleaseversionslinkagesresponse.md)
- [object PrereleaseVersionAppLinkageResponse](prereleaseversionapplinkageresponse.md)
- [object PrereleaseVersionBuildsLinkagesResponse](prereleaseversionbuildslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/prereleaseversionsresponse)*