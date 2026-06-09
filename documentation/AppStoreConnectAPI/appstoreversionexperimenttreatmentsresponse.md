# AppStoreVersionExperimentTreatmentsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list treatments for an App Store version experiment.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppStoreVersionExperimentTreatmentsResponse
```

## Properties

- `data` ([AppStoreVersionExperimentTreatment]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppStoreVersionExperimentTreatment](appstoreversionexperimenttreatment.md)
  One variant in an App Store product page A/B experiment, containing a set of alternative screenshots, previews, and promotional text.
- [object AppStoreVersionExperimentTreatmentCreateRequest](appstoreversionexperimenttreatmentcreaterequest.md)
  The request body you use to create an App Store version experiment treatment.
- [object AppStoreVersionExperimentTreatmentResponse](appstoreversionexperimenttreatmentresponse.md)
  The response body for endpoints that create, read, or modify an App Store version experiment treatment.
- [object AppStoreVersionExperimentTreatmentUpdateRequest](appstoreversionexperimenttreatmentupdaterequest.md)
  The request body you use to update an app store version experiment treatment update request.
- [object AppStoreVersionExperimentAppStoreVersionExperimentTreatmentsLinkagesResponse](appstoreversionexperimentappstoreversionexperimenttreatmentslinkagesresponse.md)
- [object AppStoreVersionExperimentTreatmentAppStoreVersionExperimentTreatmentLocalizationsLinkagesResponse](appstoreversionexperimenttreatmentappstoreversionexperimenttreatmentlocalizationslinkagesresponse.md)
- [object AppStoreVersionExperimentTreatmentLocalizationAppPreviewSetsLinkagesResponse](appstoreversionexperimenttreatmentlocalizationapppreviewsetslinkagesresponse.md)
- [object AppStoreVersionExperimentTreatmentLocalizationAppScreenshotSetsLinkagesResponse](appstoreversionexperimenttreatmentlocalizationappscreenshotsetslinkagesresponse.md)
- [object AppStoreVersionExperimentV2AppStoreVersionExperimentTreatmentsLinkagesResponse](appstoreversionexperimentv2appstoreversionexperimenttreatmentslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstoreversionexperimenttreatmentsresponse)*