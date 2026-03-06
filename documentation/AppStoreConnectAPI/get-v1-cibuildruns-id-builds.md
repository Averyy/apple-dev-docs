# List All Builds Xcode Cloud Created in App Store Connect

**Framework**: App Store Connect API  
**Kind**: httpRequest

List All App Store Connect and TestFlight Builds when it performed a build.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciBuildRuns/{id}/builds`

## Parameters

- `fields[betaBuildLocalizations]` ([string]): Additional fields to include for each Builds resource returned by the response.
- `fields[betaTesters]` ([string]): Additional fields to include for each Builds resource returned by the response.
- `fields[buildIcons]` ([string]): Additional fields to include for each Builds resource returned by the response.
- `fields[builds]` ([string]): Additional fields to include for each Builds resource returned by the response.
- `filter[appStoreVersion]` ([string]): Filter the returned builds using the ID of the related App Store Versions resource.
- `filter[app]` ([string]): Filter the returned builds using the ID of the related Apps resource.
- `filter[betaAppReviewSubmission.betaReviewState]` ([string]): Filter the returned builds using the beta review state attribute.
- `filter[betaGroups]` ([string]): Filter the returned builds using the ID of the related Beta Groups resource.
- `filter[expired]` ([string]): Filter the returned builds using the expired attribute.
- `filter[id]` ([string]): Filter the returned builds using the ID of the Builds resource.
- `filter[preReleaseVersion.platform]` ([string]): Filter the returned builds using the platform attribute of the Pre-Release Versions resource.
- `filter[preReleaseVersion.version]` ([string]): Filter the returned builds using the version attribute of the Pre-Release Versions resource.
- `filter[preReleaseVersion]` ([string]): Filter the returned builds using the ID of the related Pre-Release Versions resource.
- `filter[processingState]` ([string]): Filter the returned builds using the processing state attribute.
- `filter[usesNonExemptEncryption]` ([string]): Filter the returned builds using the uses nonexempt encryption  attribute.
- `filter[version]` ([string]): Filter the returned builds using the version attribute.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The number of Builds resources to return.
- `limit[betaBuildLocalizations]` (integer): The number of included Builds resources to return if the beta build localization relationship is included.
- `limit[icons]` (integer): The number of included Builds resources to return if the icons relationship is included.
- `limit[individualTesters]` (integer): The number of included Builds resources to return if the individual testers relationship is included.
- `sort` ([string]): Attributes by which to sort the returned Builds resources.
- `filter[buildAudienceType]` ([string])
- `limit[buildBundles]` (integer)
- `fields[buildBundles]` ([string])
- `fields[betaGroups]` ([string])
- `limit[betaGroups]` (integer)
- `fields[betaAppReviewSubmissions]` ([string])
- `fields[buildBetaDetails]` ([string])
- `fields[preReleaseVersions]` ([string])
- `fields[appStoreVersions]` ([string])
- `fields[appEncryptionDeclarations]` ([string])
- `fields[apps]` ([string])
- `exists[usesNonExemptEncryption]` (boolean)
- `fields[buildUploads]` ([string])

## See Also

- [Read Xcode Cloud Build Information](get-v1-cibuildruns-_id_.md)
  Get information about a specific Xcode Cloud build.
- [List All Actions for an Xcode Cloud Build](get-v1-cibuildruns-_id_-actions.md)
  List all actions Xcode Cloud performed during a specific build.
- [GET /v1/ciBuildRuns/{id}/relationships/actions](get-v1-cibuildruns-_id_-relationships-actions.md)
- [GET /v1/ciBuildRuns/{id}/relationships/builds](get-v1-cibuildruns-_id_-relationships-builds.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cibuildruns-_id_-builds)*