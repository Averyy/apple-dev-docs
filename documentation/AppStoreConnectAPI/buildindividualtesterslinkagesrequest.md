# BuildIndividualTestersLinkagesRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

A request body you use to add or remove a build from multiple beta groups.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BuildIndividualTestersLinkagesRequest
```

## Topics

### Objects
- [object BuildIndividualTestersLinkagesRequest.Data](buildindividualtesterslinkagesrequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` ([BuildIndividualTestersLinkagesRequest.Data]) *(required)*: The types and IDs of related resources.

## See Also

- [object Build](build.md)
  A processed binary uploaded to App Store Connect, ready for TestFlight distribution or App Store submission.
- [object BuildResponse](buildresponse.md)
  The response body for endpoints that read or modify a single build.
- [object BuildWithoutIncludesResponse](buildwithoutincludesresponse.md)
  A response containing a single build, without related resources.
- [object BuildsResponse](buildsresponse.md)
  The response body for endpoints that list builds.
- [object BuildsWithoutIncludesResponse](buildswithoutincludesresponse.md)
  A response containing a list of builds, without related resources.
- [object BuildUpdateRequest](buildupdaterequest.md)
  The request body you use to update a Build.
- [object BuildAppEncryptionDeclarationLinkageRequest](buildappencryptiondeclarationlinkagerequest.md)
  The request body you use to attach an app encryption declaration to a build.
- [object BuildAppEncryptionDeclarationLinkageResponse](buildappencryptiondeclarationlinkageresponse.md)
  A response body that contains the ID of a single related resource.
- [object BuildIndividualTestersLinkagesResponse](buildindividualtesterslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object BuildBetaGroupsLinkagesRequest](buildbetagroupslinkagesrequest.md)
  A request body you use to add or remove beta groups from a build.
- [object ImageAsset](imageasset.md)
  An image asset, including its height, width, and template URL.
- [object BetaBuildUsagesV1MetricResponse](betabuildusagesv1metricresponse.md)
  A response that contains one or more beta build metric resources.
- [object BuildAppLinkageResponse](buildapplinkageresponse.md)
- [object BuildAppStoreVersionLinkageResponse](buildappstoreversionlinkageresponse.md)
- [object BuildBetaAppReviewSubmissionLinkageResponse](buildbetaappreviewsubmissionlinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildindividualtesterslinkagesrequest)*