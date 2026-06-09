# AppStoreVersionExperimentTreatmentLocalizationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list localized treatments for an App Store version experiment.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppStoreVersionExperimentTreatmentLocalizationsResponse
```

## Properties

- `data` ([AppStoreVersionExperimentTreatmentLocalization]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppStoreVersionExperimentTreatmentLocalization](appstoreversionexperimenttreatmentlocalization.md)
  The localized screenshots, previews, and text for one treatment variant in an App Store product page A/B experiment.
- [object AppStoreVersionExperimentTreatmentLocalizationCreateRequest](appstoreversionexperimenttreatmentlocalizationcreaterequest.md)
  The request body you use to create an App Store version experiment treatment localization.
- [object AppStoreVersionExperimentTreatmentLocalizationResponse](appstoreversionexperimenttreatmentlocalizationresponse.md)
  The response body for endpoints that create, read, or modify a localized treatment for an App Store experiment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstoreversionexperimenttreatmentlocalizationsresponse)*