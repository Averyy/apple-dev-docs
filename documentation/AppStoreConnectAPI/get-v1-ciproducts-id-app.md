# Read App Information for an Xcode Cloud Product

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

- [List All Xcode Cloud Products](get-v1-ciproducts.md)
  Get a list of all products you created in Xcode Cloud.
- [Read Xcode Cloud Product Information](get-v1-ciproducts-_id_.md)
  Get information about a specific Xcode Cloud product.
- [List All Additional Repositories for an Xcode Cloud Product](get-v1-ciproducts-_id_-additionalrepositories.md)
  List all additional Git repositories you associated with an Xcode Cloud product.
- [GET /v1/ciProducts/{id}/relationships/additionalRepositories](get-v1-ciproducts-_id_-relationships-additionalrepositories.md)
- [GET /v1/ciProducts/{id}/relationships/app](get-v1-ciproducts-_id_-relationships-app.md)
- [List All Xcode Cloud Builds for an Xcode Cloud Product](get-v1-ciproducts-_id_-buildruns.md)
  List all builds Xcode Cloud performed for a specific product.
- [GET /v1/ciProducts/{id}/relationships/buildRuns](get-v1-ciproducts-_id_-relationships-buildruns.md)
- [List All Primary Git Repositories for an Xcode Cloud Product](get-v1-ciproducts-_id_-primaryrepositories.md)
  List all primary Git repositories for a specific Xcode Cloud product.
- [GET /v1/ciProducts/{id}/relationships/primaryRepositories](get-v1-ciproducts-_id_-relationships-primaryrepositories.md)
- [List All Workflows for an Xcode Cloud Product](get-v1-ciproducts-_id_-workflows.md)
  List all workflows for a specific Xcode Cloud product.
- [GET /v1/ciProducts/{id}/relationships/workflows](get-v1-ciproducts-_id_-relationships-workflows.md)
- [Read the Xcode Cloud Product for an App](get-v1-apps-_id_-ciproduct.md)
  Get the Xcode Cloud product information for an app you build with Xcode Cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciproducts-_id_-app)*