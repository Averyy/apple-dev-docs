# BuildBundleFileSize

**Framework**: App Store Connect API  
**Kind**: dictionary

The estimated and actual download and install sizes for a build bundle, broken down by device type.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object BuildBundleFileSize
```

## Topics

### Objects
- [object BuildBundleFileSize.Attributes](buildbundlefilesize/attributes-data.dictionary.md)
  The attributes that describe a Build Bundle File Sizes resource.

## Properties

- `attributes` (BuildBundleFileSize.Attributes): The attributes that describe the Build Bundle File Sizes resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a Build Bundles File Sizes resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `type` (string) *(required)*: The resource type.

## See Also

- [object BuildBundle](buildbundle.md)
  A specific binary bundle within a build, such as an app extension, App Clip, or nested app target.
- [type BuildBundleType](buildbundletype.md)
  A string that represents the possible components of a build bundle.
- [object AppClipDomainStatus](appclipdomainstatus.md)
  The validation status of the associated domains configured for an App Clip, indicating whether each domain is reachable and correctly set up.
- [object AppClipDomainStatusResponse](appclipdomainstatusresponse.md)
  A response containing the validation status of associated domains configured for an App Clip.
- [object BetaAppClipInvocationsResponse](betaappclipinvocationsresponse.md)
  A response containing a list of TestFlight App Clip invocations for a beta build.
- [object BuildBundleFileSizesResponse](buildbundlefilesizesresponse.md)
  A response containing a list of download and install size estimates for a build’s bundles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildbundlefilesize)*