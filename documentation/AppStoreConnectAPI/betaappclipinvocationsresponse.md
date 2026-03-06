# BetaAppClipInvocationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a list of Beta App Clip Invocations resources.

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
  The data structure that represents Build Bundles resource.
- [type BuildBundleType](buildbundletype.md)
  A string that represents the possible components of a build bundle.
- [object AppClipDomainStatus](appclipdomainstatus.md)
  The data structure that represents the App Clip Domain Statuses resource.
- [object BuildBundleFileSize](buildbundlefilesize.md)
  The data structure that represents a Build Bundle File Sizes resource.
- [object AppClipDomainStatusResponse](appclipdomainstatusresponse.md)
  A response that contains a single App Clip Domain Statuses resource.
- [object BuildBundleFileSizesResponse](buildbundlefilesizesresponse.md)
  A response that contains a list of Build Bundle File Sizes resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappclipinvocationsresponse)*