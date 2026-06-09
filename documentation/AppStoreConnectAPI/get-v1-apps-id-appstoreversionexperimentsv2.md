# List all app store experiments for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of all App Store version experiments for a specific app.

**Availability**:
- App Store Connect API 2.4+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appStoreVersionExperimentsV2`

## Parameters

- `fields[appStoreVersionExperimentTreatments]` ([string]): Additional fields to include for each App Store version experiment treatment resource returned by the response.
- `fields[appStoreVersionExperiments]` ([string]): Additional fields to include for each App Store version experiment resource returned by the response.
- `fields[appStoreVersions]` ([string]): Additional fields to include for each App Store version resource returned by the response.
- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.
- `filter[state]` ([string]): Filter the returned App Store version experiments by state.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of App Store version experiment resources to return.
- `limit[appStoreVersionExperimentTreatments]` (integer): The maximum number of related App Store version experiment treatments resources to return.
- `limit[controlVersions]` (integer): The maximum number of related control versions resources to return.

## See Also

- [List all app infos for an app](get-v1-apps-_id_-appinfos.md)
  Get information about an app that is currently live on App Store, or that goes live with the next version.
- [List app info IDs for an app](get-v1-apps-_id_-relationships-appinfos.md)
- [List all app store versions for an app](get-v1-apps-_id_-appstoreversions.md)
  Get a list of all App Store versions of an app across all platforms.
- [List App Store version IDs for an app](get-v1-apps-_id_-relationships-appstoreversions.md)
- [Read the end user license agreement information of an app](get-v1-apps-_id_-enduserlicenseagreement.md)
  Get the custom end user license agreement (EULA) for a specific app and the territories where the agreement applies.
- [Get the end user license agreement ID for an app](get-v1-apps-_id_-relationships-enduserlicenseagreement.md)
- [List All Custom Product Pages for an App](get-v1-apps-_id_-appcustomproductpages.md)
  Get a list of all custom product pages for a specific app.
- [Get all custom product page resource ids for an app](get-v1-apps-_id_-relationships-appcustomproductpages.md)
  Get a list of custom product page resource IDs associated with an app.
- [List App Store version experiment IDs for an app](get-v1-apps-_id_-relationships-appstoreversionexperimentsv2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appstoreversionexperimentsv2)*