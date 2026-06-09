# Read app information for an xcode cloud product

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the app in App Store Connect that’s related to an Xcode Cloud product.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciProducts/{id}/app`

## Parameters

- `fields[appInfos]` ([string]): Additional fields to include for each Apps resource returned by the response.
- `fields[appStoreVersions]` ([string]): Additional fields to include for each Apps resource returned by the response.
- `fields[apps]` ([string]): Additional fields to include for each Apps resource returned by the response.
- `fields[betaAppLocalizations]` ([string]): Additional fields to include for each Apps resource returned by the response.
- `fields[betaGroups]` ([string]): Additional fields to include for each Apps resource returned by the response.
- `fields[builds]` ([string]): Additional fields to include for each Apps resource returned by the response.
- `fields[gameCenterEnabledVersions]` ([string]): Additional fields to include for each Apps resource returned by the response.
- `fields[inAppPurchases]` ([string]): Additional fields to include for each Apps resource returned by the response.
- `fields[preReleaseVersions]` ([string]): Additional fields to include for each Apps resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[appInfos]` (integer): The number of included Apps resources to return if the app info relationship is included.
- `limit[appStoreVersions]` (integer): The number of included Apps resources to return if the App Store versions relationship is included.
- `limit[betaAppLocalizations]` (integer): The number of included Apps resources to return if the beta app localizations relationship is included.
- `limit[betaGroups]` (integer): The number of included Apps resources to return if the beta groups relationship is included.
- `limit[builds]` (integer): The number of included Apps resources to return if the builds relationship is included.
- `limit[gameCenterEnabledVersions]` (integer): The number of included Apps resources to return if the Game Center enabled versions relationship is included.
- `limit[inAppPurchases]` (integer): The number of included Apps resources to return if the in-app purchases relationship is included.
- `limit[preReleaseVersions]` (integer): The number of included Apps resources to return if the pre-release versions relationship is included.
- `limit[appClips]` (integer)
- `fields[appClips]` ([string])
- `fields[reviewSubmissions]` ([string])
- `fields[appCustomProductPages]` ([string])
- `fields[appEvents]` ([string])
- `limit[appCustomProductPages]` (integer)
- `limit[appEvents]` (integer)
- `limit[reviewSubmissions]` (integer)
- `fields[betaLicenseAgreements]` ([string])
- `fields[betaAppReviewDetails]` ([string])
- `fields[ciProducts]` ([string])
- `fields[endUserLicenseAgreements]` ([string])
- `fields[subscriptionGracePeriods]` ([string])
- `fields[subscriptionGroups]` ([string])
- `fields[promotedPurchases]` ([string])
- `limit[subscriptionGroups]` (integer)
- `limit[inAppPurchasesV2]` (integer)
- `limit[promotedPurchases]` (integer)
- `fields[appStoreVersionExperiments]` ([string])
- `limit[appStoreVersionExperimentsV2]` (integer)
- `fields[appEncryptionDeclarations]` ([string])
- `limit[appEncryptionDeclarations]` (integer)
- `fields[gameCenterDetails]` ([string])
- `fields[androidToIosAppMappingDetails]` ([string])
- `fields[buildIcons]` ([string])
- `limit[androidToIosAppMappingDetails]` (integer)

## See Also

- [List all xcode cloud products](get-v1-ciproducts.md)
  Get a list of all products you created in Xcode Cloud.
- [Read xcode cloud product information](get-v1-ciproducts-_id_.md)
  Get information about a specific Xcode Cloud product.
- [List all additional repositories for an xcode cloud product](get-v1-ciproducts-_id_-additionalrepositories.md)
  List all additional Git repositories you associated with an Xcode Cloud product.
- [List additional repository IDs for a CI product](get-v1-ciproducts-_id_-relationships-additionalrepositories.md)
- [Get the app ID for a CI product](get-v1-ciproducts-_id_-relationships-app.md)
- [List all xcode cloud builds for an xcode cloud product](get-v1-ciproducts-_id_-buildruns.md)
  List all builds Xcode Cloud performed for a specific product.
- [List build run IDs for a CI product](get-v1-ciproducts-_id_-relationships-buildruns.md)
- [List all primary git repositories for an xcode cloud product](get-v1-ciproducts-_id_-primaryrepositories.md)
  List all primary Git repositories for a specific Xcode Cloud product.
- [List primary repository IDs for a CI product](get-v1-ciproducts-_id_-relationships-primaryrepositories.md)
- [List all workflows for an xcode cloud product](get-v1-ciproducts-_id_-workflows.md)
  List all workflows for a specific Xcode Cloud product.
- [List workflow IDs for a CI product](get-v1-ciproducts-_id_-relationships-workflows.md)
- [Read the xcode cloud product for an app](get-v1-apps-_id_-ciproduct.md)
  Get the Xcode Cloud product information for an app you build with Xcode Cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciproducts-_id_-app)*