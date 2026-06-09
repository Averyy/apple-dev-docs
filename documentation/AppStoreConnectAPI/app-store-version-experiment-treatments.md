# App Store Version Experiment Treatments

**Framework**: App Store Connect API

Create and update the metadata and the optional icon that represent the treatment you apply to an App Store version experiment.

## Topics

### Endpoints
- [List all treatments for an app store experiment](get-v2-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments.md)
  Get a list of all treatments for a specific App Store version experiment.
- [List treatment IDs for an app store version experiment](get-v2-appstoreversionexperiments-_id_-relationships-appstoreversionexperimenttreatments.md)
  Get a list of experiment treatment IDs for a specific App Store version experiment.
- [Read app store version experiment treatment information](get-v1-appstoreversionexperimenttreatments-_id_.md)
  Get information about a specific App Store version experiment treatment.
- [List all localizations for an app store version experiment treatment](get-v1-appstoreversionexperimenttreatments-_id_-appstoreversionexperimenttreatmentlocalizations.md)
  Get a list of all localizations for a specific App Store version experiment treatment.
- [List localization IDs for an App Store version experiment treatment](get-v1-appstoreversionexperimenttreatments-_id_-relationships-appstoreversionexperimenttreatmentlocalizations.md)
- [Modify an app store version experiment treatment](patch-v1-appstoreversionexperimenttreatments-_id_.md)
  Update the name and app icon name for a specific App Store version experiment.
- [Create an app store version experiment treatment](post-v1-appstoreversionexperimenttreatments.md)
  Add a new treatment to an App Store version experiment.
- [Delete a treatment for an app store version experiment](delete-v1-appstoreversionexperimenttreatments-_id_.md)
  Delete metadata that you configured for an App Store Version experiment.
### Objects
- [object AppStoreVersionExperimentTreatment](appstoreversionexperimenttreatment.md)
  One variant in an App Store product page A/B experiment, containing a set of alternative screenshots, previews, and promotional text.
- [object AppStoreVersionExperimentTreatmentCreateRequest](appstoreversionexperimenttreatmentcreaterequest.md)
  The request body you use to create an App Store version experiment treatment.
- [object AppStoreVersionExperimentTreatmentResponse](appstoreversionexperimenttreatmentresponse.md)
  The response body for endpoints that create, read, or modify an App Store version experiment treatment.
- [object AppStoreVersionExperimentTreatmentUpdateRequest](appstoreversionexperimenttreatmentupdaterequest.md)
  The request body you use to update an app store version experiment treatment update request.
- [object AppStoreVersionExperimentTreatmentsResponse](appstoreversionexperimenttreatmentsresponse.md)
  The response body for endpoints that list treatments for an App Store version experiment.
- [object AppStoreVersionExperimentAppStoreVersionExperimentTreatmentsLinkagesResponse](appstoreversionexperimentappstoreversionexperimenttreatmentslinkagesresponse.md)
- [object AppStoreVersionExperimentTreatmentAppStoreVersionExperimentTreatmentLocalizationsLinkagesResponse](appstoreversionexperimenttreatmentappstoreversionexperimenttreatmentlocalizationslinkagesresponse.md)
- [object AppStoreVersionExperimentTreatmentLocalizationAppPreviewSetsLinkagesResponse](appstoreversionexperimenttreatmentlocalizationapppreviewsetslinkagesresponse.md)
- [object AppStoreVersionExperimentTreatmentLocalizationAppScreenshotSetsLinkagesResponse](appstoreversionexperimenttreatmentlocalizationappscreenshotsetslinkagesresponse.md)
- [object AppStoreVersionExperimentV2AppStoreVersionExperimentTreatmentsLinkagesResponse](appstoreversionexperimentv2appstoreversionexperimenttreatmentslinkagesresponse.md)

## See Also

- [App Store version experiments](app-store-version-experiments.md)
  Test elements of your App Store product page.
- [App Store Version Experiment Treatment Localizations](app-store-version-experiment-treatment-localizations.md)
  Manage the localized assets, including screenshots and previews, for an App Store version experiment treatment.
- [App Store Version Promotions](app-store-version-promotions.md)
  Apply a version experiment treatment to your app’s product page in the App Store, or to your upcoming App Store version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-version-experiment-treatments)*