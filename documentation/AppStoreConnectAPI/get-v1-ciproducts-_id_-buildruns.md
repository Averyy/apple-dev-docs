# List all xcode cloud builds for an xcode cloud product

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all builds Xcode Cloud performed for a specific product.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciProducts/{id}/buildRuns`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Products resource.

### Query Parameters

- `fields[builds]` ([string]): Additional fields to include for each Build Runs resource returned by the response.

  **Allowed Values**: `version`, `uploadedDate`, `expirationDate`, `expired`, `minOsVersion`, `lsMinimumSystemVersion`, `computedMinMacOsVersion`, `computedMinVisionOsVersion`, `iconAssetToken`, `processingState`, `buildAudienceType`, `usesNonExemptEncryption`, `preReleaseVersion`, `individualTesters`, `betaGroups`, `betaBuildLocalizations`, `appEncryptionDeclaration`, `betaAppReviewSubmission`, `app`, `buildBetaDetail`, `appStoreVersion`, `icons`, `buildBundles`, `buildUpload`, `perfPowerMetrics`, `diagnosticSignatures`
- `fields[ciBuildRuns]` ([string]): Additional fields to include for each Build Runs resource returned by the response.

  **Allowed Values**: `number`, `createdDate`, `startedDate`, `finishedDate`, `sourceCommit`, `destinationCommit`, `isPullRequestBuild`, `issueCounts`, `executionProgress`, `completionStatus`, `startReason`, `cancelReason`, `builds`, `workflow`, `product`, `sourceBranchOrTag`, `destinationBranch`, `actions`, `pullRequest`
- `filter[builds]` ([string]): Filter the returned build runs using the ID of the related Builds resource.
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `builds`, `workflow`, `product`, `sourceBranchOrTag`, `destinationBranch`, `pullRequest`
- `limit` (integer): The number of Build Runs resources to return.

  **Maximum**: `200`
- `limit[builds]` (integer): The number of included Build Runs resources to return if the builds relationship is included.

  **Maximum**: `50`
- `fields[scmGitReferences]` ([string]): **Allowed Values**: `name`, `canonicalName`, `isDeleted`, `kind`, `repository`
- `fields[ciWorkflows]` ([string]): **Allowed Values**: `name`, `description`, `branchStartCondition`, `tagStartCondition`, `pullRequestStartCondition`, `scheduledStartCondition`, `manualBranchStartCondition`, `manualTagStartCondition`, `manualPullRequestStartCondition`, `actions`, `isEnabled`, `isLockedForEditing`, `clean`, `containerFilePath`, `lastModifiedDate`, `product`, `repository`, `xcodeVersion`, `macOsVersion`, `buildRuns`
- `fields[scmPullRequests]` ([string]): **Allowed Values**: `title`, `number`, `webUrl`, `sourceRepositoryOwner`, `sourceRepositoryName`, `sourceBranchName`, `destinationRepositoryOwner`, `destinationRepositoryName`, `destinationBranchName`, `isClosed`, `isCrossRepository`, `repository`
- `fields[ciProducts]` ([string]): **Allowed Values**: `name`, `createdDate`, `productType`, `app`, `bundleId`, `workflows`, `primaryRepositories`, `additionalRepositories`, `buildRuns`
- `sort` ([string]): **Allowed Values**: `number`, `-number`

## Responses

- `200` OK (`CiBuildRunsResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Xcode Cloud Products
- [List all xcode cloud products](./get-v1-ciproducts.md)
  Get a list of all products you created in Xcode Cloud.
- [Read xcode cloud product information](./get-v1-ciproducts-_id_.md)
  Get information about a specific Xcode Cloud product.
- [List all additional repositories for an xcode cloud product](./get-v1-ciproducts-_id_-additionalrepositories.md)
  List all additional Git repositories you associated with an Xcode Cloud product.
- [List additional repository IDs for a CI product](./get-v1-ciproducts-_id_-relationships-additionalrepositories.md)
- [Read app information for an xcode cloud product](./get-v1-ciproducts-_id_-app.md)
  Get the app in App Store Connect that’s related to an Xcode Cloud product.
- [Get the app ID for a CI product](./get-v1-ciproducts-_id_-relationships-app.md)
- [List build run IDs for a CI product](./get-v1-ciproducts-_id_-relationships-buildruns.md)
- [List all primary git repositories for an xcode cloud product](./get-v1-ciproducts-_id_-primaryrepositories.md)
  List all primary Git repositories for a specific Xcode Cloud product.
- [List primary repository IDs for a CI product](./get-v1-ciproducts-_id_-relationships-primaryrepositories.md)
- [List all workflows for an xcode cloud product](./get-v1-ciproducts-_id_-workflows.md)
  List all workflows for a specific Xcode Cloud product.
- [List workflow IDs for a CI product](./get-v1-ciproducts-_id_-relationships-workflows.md)
- [Read the xcode cloud product for an app](./get-v1-apps-_id_-ciproduct.md)
  Get the Xcode Cloud product information for an app you build with Xcode Cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciproducts-_id_-buildruns)*