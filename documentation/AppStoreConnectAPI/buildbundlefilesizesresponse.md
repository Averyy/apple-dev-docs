# BuildBundleFileSizesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of download and install size estimates for a build’s bundles.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object BuildBundleFileSizesResponse
```

## Properties

- `data` ([BuildBundleFileSize]) *(required)*: The resource data.
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
- [object BetaAppClipInvocationsResponse](betaappclipinvocationsresponse.md)
  A response containing a list of TestFlight App Clip invocations for a beta build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildbundlefilesizesresponse)*