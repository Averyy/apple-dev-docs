# PrereleaseVersion

**Framework**: App Store Connect API  
**Kind**: dictionary

A pre-release version associated with a build, representing a development or beta software version before App Store submission.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object PrereleaseVersion
```

## Topics

### Objects
- [object PrereleaseVersion.Attributes](prereleaseversion/attributes-data.dictionary.md)
  Attributes that describe a Prerelease Versions resource.
- [object PrereleaseVersion.Relationships](prereleaseversion/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (PrereleaseVersion.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (PrereleaseVersion.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object PrereleaseVersionResponse](prereleaseversionresponse.md)
  The response body for endpoints that read a single prerelease version of an app.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/prereleaseversion)*