# Read App Store Version Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information for a specific app store version.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 3.6 release notes](app-store-connect-api-3-6-release-notes.md)
- [Configuring and parsing App Store Connect API webhook notifications](configuring-webhook-notifications.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}`

## Parameters

- `limit[appStoreVersionLocalizations]` (integer): Number of resources to return.
- `include` ([string]): Relationship data to include in the response.
- `fields[appStoreVersions]` ([string]): Fields to return for included related types.
- `fields[appStoreVersionSubmissions]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `fields[appStoreReviewDetails]` ([string]): Fields to return for included related types.
- `fields[appStoreVersionPhasedReleases]` ([string]): Fields to return for included related types.
- `fields[routingAppCoverages]` ([string]): Fields to return for included related types.
- `fields[appStoreVersionLocalizations]` ([string]): Fields to return for included related types.
- `fields[appClipDefaultExperiences]` ([string])
- `fields[appStoreVersionExperiments]` ([string])
- `limit[appStoreVersionExperiments]` (integer)
- `limit[appStoreVersionExperimentsV2]` (integer)
- `fields[alternativeDistributionPackages]` ([string])
- `fields[gameCenterAppVersions]` ([string])

## See Also

- [List All App Store Versions for an App](get-v1-apps-_id_-appstoreversions.md)
  Get a list of all App Store versions of an app across all platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_)*