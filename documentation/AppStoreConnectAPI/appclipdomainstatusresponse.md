# AppClipDomainStatusResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing the validation status of associated domains configured for an App Clip.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object AppClipDomainStatusResponse
```

## Properties

- `data` (AppClipDomainStatus) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [object BuildBundle](buildbundle.md)
  A specific binary bundle within a build, such as an app extension, App Clip, or nested app target.
- [type BuildBundleType](buildbundletype.md)
  A string that represents the possible components of a build bundle.
- [object AppClipDomainStatus](appclipdomainstatus.md)
  The validation status of the associated domains configured for an App Clip, indicating whether each domain is reachable and correctly set up.
- [object BuildBundleFileSize](buildbundlefilesize.md)
  The estimated and actual download and install sizes for a build bundle, broken down by device type.
- [object BetaAppClipInvocationsResponse](betaappclipinvocationsresponse.md)
  A response containing a list of TestFlight App Clip invocations for a beta build.
- [object BuildBundleFileSizesResponse](buildbundlefilesizesresponse.md)
  A response containing a list of download and install size estimates for a build’s bundles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipdomainstatusresponse)*