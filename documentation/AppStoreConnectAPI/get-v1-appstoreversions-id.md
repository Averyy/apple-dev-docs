# Read app store version information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information for a specific App Store version.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 3.6 release notes](app-store-connect-api-3-6-release-notes.md)
- [Configuring and parsing App Store Connect API webhook notifications](configuring-webhook-notifications.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}`

## Parameters

- `limit[appStoreVersionLocalizations]` (integer): The maximum number of related App Store version localization resources to return.
- `include` ([string]): The relationship data to include in the response.
- `fields[appStoreVersions]` ([string]): Additional fields to include for each App Store version resource returned by the response.
- `fields[appStoreVersionSubmissions]` ([string]): Additional fields to include for each App Store version submission resource returned by the response.
- `fields[builds]` ([string]): Additional fields to include for each build resource returned by the response.
- `fields[appStoreReviewDetails]` ([string]): Additional fields to include for each App Store review detail resource returned by the response.
- `fields[appStoreVersionPhasedReleases]` ([string]): Additional fields to include for each App Store version phased release resource returned by the response.
- `fields[routingAppCoverages]` ([string]): Additional fields to include for each routing app coverage resource returned by the response.
- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.
- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each App Clip default experience resource returned by the response.
- `fields[appStoreVersionExperiments]` ([string]): Additional fields to include for each App Store version experiment resource returned by the response.
- `limit[appStoreVersionExperiments]` (integer): The maximum number of related App Store version experiment resources to return.
- `limit[appStoreVersionExperimentsV2]` (integer): The maximum number of related App Store version experiment (v2) resources to return.
- `fields[alternativeDistributionPackages]` ([string]): Additional fields to include for each alternative distribution package resource returned by the response.
- `fields[apps]` ([string])
- `fields[gameCenterAppVersions]` ([string])

## See Also

- [List all app store versions for an app](get-v1-apps-_id_-appstoreversions.md)
  Get a list of all App Store versions of an app across all platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_)*