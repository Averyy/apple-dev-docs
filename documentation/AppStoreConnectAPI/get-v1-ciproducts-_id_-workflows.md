# List all workflows for an xcode cloud product

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all workflows for a specific Xcode Cloud product.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciProducts/{id}/workflows`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Products resource.

### Query Parameters

- `fields[ciWorkflows]` ([string]): Additional fields to include for each Workflows resource returned by the response.

  **Allowed Values**: `name`, `description`, `branchStartCondition`, `tagStartCondition`, `pullRequestStartCondition`, `scheduledStartCondition`, `manualBranchStartCondition`, `manualTagStartCondition`, `manualPullRequestStartCondition`, `actions`, `isEnabled`, `isLockedForEditing`, `clean`, `containerFilePath`, `lastModifiedDate`, `product`, `repository`, `xcodeVersion`, `macOsVersion`, `buildRuns`
- `limit` (integer): The number of Workflows resources to return.

  **Maximum**: `200`
- `fields[ciXcodeVersions]` ([string]): **Allowed Values**: `version`, `name`, `testDestinations`, `macOsVersions`
- `fields[ciMacOsVersions]` ([string]): **Allowed Values**: `version`, `name`, `xcodeVersions`
- `fields[ciProducts]` ([string]): **Allowed Values**: `name`, `createdDate`, `productType`, `app`, `bundleId`, `workflows`, `primaryRepositories`, `additionalRepositories`, `buildRuns`
- `fields[scmRepositories]` ([string]): **Allowed Values**: `lastAccessedDate`, `httpCloneUrl`, `sshCloneUrl`, `ownerName`, `repositoryName`, `scmProvider`, `defaultBranch`, `gitReferences`, `pullRequests`
- `include` ([string]): **Allowed Values**: `product`, `repository`, `xcodeVersion`, `macOsVersion`

## Responses

- `200` OK (`CiWorkflowsResponse`, `application/json`): The request completed successfully.
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
- [List all xcode cloud builds for an xcode cloud product](./get-v1-ciproducts-_id_-buildruns.md)
  List all builds Xcode Cloud performed for a specific product.
- [List build run IDs for a CI product](./get-v1-ciproducts-_id_-relationships-buildruns.md)
- [List all primary git repositories for an xcode cloud product](./get-v1-ciproducts-_id_-primaryrepositories.md)
  List all primary Git repositories for a specific Xcode Cloud product.
- [List primary repository IDs for a CI product](./get-v1-ciproducts-_id_-relationships-primaryrepositories.md)
- [List workflow IDs for a CI product](./get-v1-ciproducts-_id_-relationships-workflows.md)
- [Read the xcode cloud product for an app](./get-v1-apps-_id_-ciproduct.md)
  Get the Xcode Cloud product information for an app you build with Xcode Cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciproducts-_id_-workflows)*