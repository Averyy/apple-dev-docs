# App Store version experiments

**Framework**: App Store Connect API

Test elements of your App Store product page.

## Topics

### Managing App Store version experiments
- [List all experiments for an app store version v1](get-v1-appstoreversions-_id_-appstoreversionexperiments.md)
  Get a list of all experiments for an App Store version of an app across all platforms.
- [List all experiments ids for an app store version v1](get-v1-appstoreversions-_id_-relationships-appstoreversionexperiments.md)
  Get a list of all experiments IDs for an App Store version of an app across all platforms.
- [List all experiments for an app store version](get-v1-appstoreversions-_id_-appstoreversionexperimentsv2.md)
  Get a list of all experiments for an App Store version of an app across all platforms.
- [List all experiment ids for an app store version](get-v1-appstoreversions-_id_-relationships-appstoreversionexperimentsv2.md)
  Get a list of all experiments IDs for an App Store version across all platforms.
- [Read app store experiment information](get-v2-appstoreversionexperiments-_id_.md)
  Get information for a specific App Store version experiment.
- [List all treatments for an app store experiment](get-v2-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments.md)
  Get a list of all treatments for a specific App Store version experiment.
- [List treatment IDs for an app store version experiment](get-v2-appstoreversionexperiments-_id_-relationships-appstoreversionexperimenttreatments.md)
  Get a list of experiment treatment IDs for a specific App Store version experiment.
- [Create an app store experiment](post-v2-appstoreversionexperiments.md)
  Add a new experiment to an App Store version.
- [Modify an app store experiment](patch-v2-appstoreversionexperiments-_id_.md)
  Update the name, the started state, and the proportion of traffic to send to an App Store experiment.
- [Delete an app store experiment](delete-v2-appstoreversionexperiments-_id_.md)
  Delete a specific App Store version experiment before it starts.
- [Read app store experiment information v1](get-v1-appstoreversionexperiments-_id_.md)
  Get information for a specific App Store version experiment.
- [List all treatments for an app store experiment v1](get-v1-appstoreversionexperiments-_id_-appstoreversionexperimenttreatments.md)
  Get a list of all treatments for a specific App Store version experiment.
- [List treatment IDs for an App Store version experiment](get-v1-appstoreversionexperiments-_id_-relationships-appstoreversionexperimenttreatments.md)
- [Modify an app store experiment v1](patch-v1-appstoreversionexperiments-_id_.md)
  Update the name, the started state, and the proportion of traffic to send to an App Store experiment.
- [Create an app store experiment v1](post-v1-appstoreversionexperiments.md)
  Add a new experiment to an App Store version.
- [Delete an app store version experiment v1](delete-v1-appstoreversionexperiments-_id_.md)
  Delete a specific App Store version experiment before it starts.
### Objects
- [object AppStoreVersionExperimentV2](appstoreversionexperimentv2.md)
  An A/B test comparing two product page variants for an App Store version to determine which drives more downloads.
- [object AppStoreVersionExperimentV2CreateRequest](appstoreversionexperimentv2createrequest.md)
  The request body you use to create an App Store version experiment.
- [object AppStoreVersionExperimentV2Response](appstoreversionexperimentv2response.md)
  A response containing a single App Store product page A/B experiment.
- [object AppStoreVersionExperimentV2UpdateRequest](appstoreversionexperimentv2updaterequest.md)
  The request body you use to update an app store version experiment v2update request.
- [object AppStoreVersionExperimentsV2Response](appstoreversionexperimentsv2response.md)
  A response containing a list of A/B product page experiments for an App Store version.
- [object AppStoreVersionExperiment](appstoreversionexperiment.md)
- [object AppStoreVersionExperimentCreateRequest](appstoreversionexperimentcreaterequest.md)
- [object AppStoreVersionExperimentResponse](appstoreversionexperimentresponse.md)
- [object AppStoreVersionExperimentUpdateRequest](appstoreversionexperimentupdaterequest.md)
- [object AppStoreVersionExperimentsResponse](appstoreversionexperimentsresponse.md)
- [object AppStoreVersionExperimentAppStoreVersionExperimentTreatmentsLinkagesResponse](appstoreversionexperimentappstoreversionexperimenttreatmentslinkagesresponse.md)
- [object AppStoreVersionExperimentTreatmentAppStoreVersionExperimentTreatmentLocalizationsLinkagesResponse](appstoreversionexperimenttreatmentappstoreversionexperimenttreatmentlocalizationslinkagesresponse.md)
- [object AppStoreVersionExperimentTreatmentLocalizationAppPreviewSetsLinkagesResponse](appstoreversionexperimenttreatmentlocalizationapppreviewsetslinkagesresponse.md)
- [object AppStoreVersionExperimentTreatmentLocalizationAppScreenshotSetsLinkagesResponse](appstoreversionexperimenttreatmentlocalizationappscreenshotsetslinkagesresponse.md)
- [object AppStoreVersionExperimentV2AppStoreVersionExperimentTreatmentsLinkagesResponse](appstoreversionexperimentv2appstoreversionexperimenttreatmentslinkagesresponse.md)

## See Also

- [App Store Version Experiment Treatments](app-store-version-experiment-treatments.md)
  Create and update the metadata and the optional icon that represent the treatment you apply to an App Store version experiment.
- [App Store Version Experiment Treatment Localizations](app-store-version-experiment-treatment-localizations.md)
  Manage the localized assets, including screenshots and previews, for an App Store version experiment treatment.
- [App Store Version Promotions](app-store-version-promotions.md)
  Apply a version experiment treatment to your app’s product page in the App Store, or to your upcoming App Store version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-version-experiments)*