# InternalBetaState

**Framework**: App Store Connect API  
**Kind**: typealias

String that represents a build’s availability for internal testing.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
string InternalBetaState
```

#### Discussion

-`PROCESSING`: -`PROCESSING_EXCEPTION`: -`MISSING_EXPORT_COMPLIANCE`: -`READY_FOR_BETA_TESTING`: -`IN_BETA_TESTING`: -`EXPIRED`: -`IN_EXPORT_COMPLIANCE_REVIEW`:

## See Also

- [object BuildBetaDetail](buildbetadetail.md)
  The TestFlight distribution settings for a build, including whether it is available for external testing.
- [object BuildBetaDetailUpdateRequest](buildbetadetailupdaterequest.md)
  The request body you use to update a Build Data Detail.
- [object BuildBetaDetailResponse](buildbetadetailresponse.md)
  The response body for endpoints that read or modify beta testing details for a build.
- [object BuildBetaDetailsResponse](buildbetadetailsresponse.md)
  The response body for endpoints that list beta testing details across builds.
- [type ExternalBetaState](externalbetastate.md)
  String that represents a build’s availability for external testing.
- [object BuildBuildBetaDetailLinkageResponse](buildbuildbetadetaillinkageresponse.md)
- [object BuildBundleAppClipDomainCacheStatusLinkageResponse](buildbundleappclipdomaincachestatuslinkageresponse.md)
- [object BuildBundleAppClipDomainDebugStatusLinkageResponse](buildbundleappclipdomaindebugstatuslinkageresponse.md)
- [object BuildBundleBetaAppClipInvocationsLinkagesResponse](buildbundlebetaappclipinvocationslinkagesresponse.md)
- [object BuildBundleBuildBundleFileSizesLinkagesResponse](buildbundlebuildbundlefilesizeslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/internalbetastate)*