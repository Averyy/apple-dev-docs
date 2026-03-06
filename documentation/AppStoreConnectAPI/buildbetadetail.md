# BuildBetaDetail

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a Build Beta Details resource.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BuildBetaDetail
```

## Topics

### Objects
- [object BuildBetaDetail.Attributes](buildbetadetail/attributes-data.dictionary.md)
  Attributes that describe a Build Beta Details resource.
- [object BuildBetaDetail.Relationships](buildbetadetail/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (BuildBetaDetail.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (BuildBetaDetail.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [object BuildBetaDetailUpdateRequest](buildbetadetailupdaterequest.md)
  The request body you use to update a Build Data Detail.
- [object BuildBetaDetailResponse](buildbetadetailresponse.md)
  A response that contains a single Build Beta Details resource.
- [object BuildBetaDetailsResponse](buildbetadetailsresponse.md)
  A response that contains a list of Build Beta Detail resources.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildbetadetail)*