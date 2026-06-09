# PrereleaseVersionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read a single prerelease version of an app.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object PrereleaseVersionResponse
```

## Properties

- `data` (PrereleaseVersion) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.
- `included` ([*])

## See Also

- [Read the prerelease version of a build](get-v1-builds-_id_-prereleaseversion.md)
  Get the prerelease version for a specific build.
- [object PrereleaseVersion](prereleaseversion.md)
  A pre-release version associated with a build, representing a development or beta software version before App Store submission.
- [object PreReleaseVersionsResponse](prereleaseversionsresponse.md)
  A response containing a list of pre-release versions for an app.
- [object PrereleaseVersionWithoutIncludesResponse](prereleaseversionwithoutincludesresponse.md)
  A response containing a single pre-release version, without related resources.
- [object PreReleaseVersionsWithoutIncludesResponse](prereleaseversionswithoutincludesresponse.md)
  A response containing a list of pre-release versions, without related resources.
- [object AppPreReleaseVersionsLinkagesResponse](appprereleaseversionslinkagesresponse.md)
- [object PrereleaseVersionAppLinkageResponse](prereleaseversionapplinkageresponse.md)
- [object PrereleaseVersionBuildsLinkagesResponse](prereleaseversionbuildslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/prereleaseversionresponse)*