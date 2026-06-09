# BetaAppClipInvocationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of TestFlight App Clip invocations for a beta build.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object BetaAppClipInvocationsResponse
```

## Properties

- `data` ([BetaAppClipInvocation]) *(required)*: The resource data.
- `included` ([BetaAppClipInvocationLocalization]): The requested relationship data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): The paging information.

## See Also

- [object BuildBundle](buildbundle.md)
  A specific binary bundle within a build, such as an app extension, App Clip, or nested app target.
- [type BuildBundleType](buildbundletype.md)
  A string that represents the possible components of a build bundle.
- [object AppClipDomainStatus](appclipdomainstatus.md)
  The validation status of the associated domains configured for an App Clip, indicating whether each domain is reachable and correctly set up.
- [object BuildBundleFileSize](buildbundlefilesize.md)
  The estimated and actual download and install sizes for a build bundle, broken down by device type.
- [object AppClipDomainStatusResponse](appclipdomainstatusresponse.md)
  A response containing the validation status of associated domains configured for an App Clip.
- [object BuildBundleFileSizesResponse](buildbundlefilesizesresponse.md)
  A response containing a list of download and install size estimates for a build’s bundles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappclipinvocationsresponse)*