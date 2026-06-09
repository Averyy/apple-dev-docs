# BuildBetaDetailUpdateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to update a Build Data Detail.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BuildBetaDetailUpdateRequest
```

## Topics

### Objects
- [object BuildBetaDetailUpdateRequest.Data](buildbetadetailupdaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (BuildBetaDetailUpdateRequest.Data) *(required)*: The resource data.

## See Also

- [object BuildBetaDetail](buildbetadetail.md)
  The TestFlight distribution settings for a build, including whether it is available for external testing.
- [object BuildBetaDetailResponse](buildbetadetailresponse.md)
  The response body for endpoints that read or modify beta testing details for a build.
- [object BuildBetaDetailsResponse](buildbetadetailsresponse.md)
  The response body for endpoints that list beta testing details across builds.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildbetadetailupdaterequest)*