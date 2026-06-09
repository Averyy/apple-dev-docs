# AppClipDomainStatus

**Framework**: App Store Connect API  
**Kind**: dictionary

The validation status of the associated domains configured for an App Clip, indicating whether each domain is reachable and correctly set up.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipDomainStatus
```

## Topics

### Objects
- [object AppClipDomainStatus.Attributes](appclipdomainstatus/attributes-data.dictionary.md)
  The attributes that describe the App Clip Domain Status resource.

## Properties

- `attributes` (AppClipDomainStatus.Attributes): The attributes that describe the App Clip Domain Statuses resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies an App Clip Domain Statuses resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `type` (string) *(required)*: The resource type.

## See Also

- [object BuildBundle](buildbundle.md)
  A specific binary bundle within a build, such as an app extension, App Clip, or nested app target.
- [type BuildBundleType](buildbundletype.md)
  A string that represents the possible components of a build bundle.
- [object BuildBundleFileSize](buildbundlefilesize.md)
  The estimated and actual download and install sizes for a build bundle, broken down by device type.
- [object AppClipDomainStatusResponse](appclipdomainstatusresponse.md)
  A response containing the validation status of associated domains configured for an App Clip.
- [object BetaAppClipInvocationsResponse](betaappclipinvocationsresponse.md)
  A response containing a list of TestFlight App Clip invocations for a beta build.
- [object BuildBundleFileSizesResponse](buildbundlefilesizesresponse.md)
  A response containing a list of download and install size estimates for a build’s bundles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipdomainstatus)*