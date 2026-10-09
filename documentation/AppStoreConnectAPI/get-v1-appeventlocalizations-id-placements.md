# List related placements

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the placements for an in-app event localization.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [App Store Connect API 4.5.1 release notes](app-store-connect-api-4-5-1-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appEventLocalizations/{id}/placements`

## Parameters

- `filter[placementType]` ([string]): Filter the returned app asset library placements by placement type.
- `filter[placementGroup]` ([string]): Filter the returned app asset library placements by placement group.
- `filter[state]` ([string]): Filter the returned app asset library placements by state.
- `filter[image]` ([string]): Filter the returned app asset library placements by image.
- `filter[video]` ([string]): Filter the returned app asset library placements by video.
- `filter[appStoreVersionLocalization]` ([string]): Filter the returned app asset library placements by App Store version localization.
- `filter[appCustomProductPageLocalization]` ([string]): Filter the returned app asset library placements by app custom product page localization.
- `filter[appStoreVersionExperimentTreatmentLocalization]` ([string]): Filter the returned app asset library placements by App Store version experiment treatment localization.
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

- [Read app event localization information](get-v1-appeventlocalizations-_id_.md)
  Get information about a specific app event localization.
- [List all video clips for an app event localization](get-v1-appeventlocalizations-_id_-appeventvideoclips.md)
  Get a list of video clips for a specific app event localization.
- [List app event video clip IDs for an app event localization](get-v1-appeventlocalizations-_id_-relationships-appeventvideoclips.md)
- [List all screenshots for an app event localization](get-v1-appeventlocalizations-_id_-appeventscreenshots.md)
  Get a list of screenshots for a specific app event localization.
- [List app event screenshot IDs for an app event localization](get-v1-appeventlocalizations-_id_-relationships-appeventscreenshots.md)
- [Modify an app event localization](patch-v1-appeventlocalizations-_id_.md)
  Update the localized metadata for a specific in-app event.
- [Create an app event localization](post-v1-appeventlocalizations.md)
  Add a new localization for an in-app event.
- [Delete an app event localization](delete-v1-appeventlocalizations-_id_.md)
  Delete localized metadata that you configured for an in-app event.
- [List the placement IDs for an in-app event localization](get-v1-appeventlocalizations-_id_-relationships-placements.md)
  Get a list of placement resource IDs for a specific in-app event localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appeventlocalizations-_id_-placements)*