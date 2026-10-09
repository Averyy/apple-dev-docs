# List related placements

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the placements for an App Store version experiment treatment localization.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5.1 release notes](app-store-connect-api-4-5-1-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionExperimentTreatmentLocalizations/{id}/placements`

## Parameters

- `filter[placementType]` ([string]): Filter the returned app asset library placements by placement type.
- `filter[placementGroup]` ([string]): Filter the returned app asset library placements by placement group.
- `filter[state]` ([string]): Filter the returned app asset library placements by state.
- `filter[image]` ([string]): Filter the returned app asset library placements by image.
- `filter[video]` ([string]): Filter the returned app asset library placements by video.
- `filter[appEventLocalization]` ([string]): Filter the returned app asset library placements by in-app event localization.
- `filter[appStoreVersionLocalization]` ([string]): Filter the returned app asset library placements by App Store version localization.
- `filter[appCustomProductPageLocalization]` ([string]): Filter the returned app asset library placements by app custom product page localization.
- `filter[id]` ([string]): Filter the returned app asset library placements by resource ID.
- `sort` ([string]): Attributes by which to sort.
- `fields[appAssetLibraryPlacements]` ([string]): Additional fields to include for each app asset library placement resource returned by the response.
- `fields[appAssetLibraryImages]` ([string]): Additional fields to include for each app asset library image resource returned by the response.
- `fields[appAssetLibraryVideos]` ([string]): Additional fields to include for each app asset library video resource returned by the response.
- `fields[appEventLocalizations]` ([string]): Additional fields to include for each in-app event localization resource returned by the response.
- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.
- `fields[appCustomProductPageLocalizations]` ([string]): Additional fields to include for each app custom product page localization resource returned by the response.
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string]): Additional fields to include for each App Store version experiment treatment localization resource returned by the response.
- `limit` (integer): The maximum number of app asset library placement resources to return.
- `include` ([string]): The relationship data to include in the response.

## See Also

- [Read app store version experiment treatment localization information](get-v1-appstoreversionexperimenttreatmentlocalizations-_id_.md)
  Get information about a specific App Store version experiment treatment localization.
- [List all screenshot sets for an experiment treatment localization](get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-appscreenshotsets.md)
  Get a list of screenshot sets for a specific App Store version experiment treatment localization.
- [List all preview sets for an experiment treatment localization](get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-apppreviewsets.md)
  Get a list of preview sets for a specific App Store version experiment treatment localization.
- [List preview set IDs for an App Store version experiment treatment localization](get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-relationships-apppreviewsets.md)
- [List screenshot set IDs for an App Store version experiment treatment localization](get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-relationships-appscreenshotsets.md)
- [Create an app store version experiment treatment localization](post-v1-appstoreversionexperimenttreatmentlocalizations.md)
  Add a new localization for an App Store version experiment treatment.
- [Delete a treatment localization for an app store version experiment](delete-v1-appstoreversionexperimenttreatmentlocalizations-_id_.md)
  Delete localized metatdata that you configured for an App Store Version experiment treatment.
- [List the placement IDs for an App Store version experiment treatment localization](get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-relationships-placements.md)
  Get a list of placement resource IDs for a specific App Store version experiment treatment localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionexperimenttreatmentlocalizations-_id_-placements)*