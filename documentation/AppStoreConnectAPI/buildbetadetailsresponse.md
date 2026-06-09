# BuildBetaDetailsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list beta testing details across builds.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BuildBetaDetailsResponse
```

## Properties

- `data` ([BuildBetaDetail]) *(required)*: The resource data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.
- `included` ([Build])

## See Also

- [List build beta details](get-v1-buildbetadetails.md)
  Find and list build beta details for all builds.
- [object BuildBetaDetail](buildbetadetail.md)
  The TestFlight distribution settings for a build, including whether it is available for external testing.
- [object BuildBetaDetailUpdateRequest](buildbetadetailupdaterequest.md)
  The request body you use to update a Build Data Detail.
- [object BuildBetaDetailResponse](buildbetadetailresponse.md)
  The response body for endpoints that read or modify beta testing details for a build.
- [type ExternalBetaState](externalbetastate.md)
  String that represents a build’s availability for external testing.
- [type InternalBetaState](internalbetastate.md)
  String that represents a build’s availability for internal testing.
- [object BuildBuildBetaDetailLinkageResponse](buildbuildbetadetaillinkageresponse.md)
- [object BuildBundleAppClipDomainCacheStatusLinkageResponse](buildbundleappclipdomaincachestatuslinkageresponse.md)
- [object BuildBundleAppClipDomainDebugStatusLinkageResponse](buildbundleappclipdomaindebugstatuslinkageresponse.md)
- [object BuildBundleBetaAppClipInvocationsLinkagesResponse](buildbundlebetaappclipinvocationslinkagesresponse.md)
- [object BuildBundleBuildBundleFileSizesLinkagesResponse](buildbundlebuildbundlefilesizeslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildbetadetailsresponse)*