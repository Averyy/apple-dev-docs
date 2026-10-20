# List all repositories for a source code management provider

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all Git repositories for a specific source code management provider you connected to Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/scmProviders/{id}/repositories`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Providers  resource.

### Query Parameters

- `fields[scmRepositories]` ([string]): Additional fields to include for each Repositories resource returned by the response.

  **Allowed Values**: `lastAccessedDate`, `httpCloneUrl`, `sshCloneUrl`, `ownerName`, `repositoryName`, `scmProvider`, `defaultBranch`, `gitReferences`, `pullRequests`
- `filter[id]` ([string]): Filter the returned repositories using the ID of the Repositories resource.
- `limit` (integer): The number of Repositories resources to return.

  **Maximum**: `200`
- `fields[scmGitReferences]` ([string]): **Allowed Values**: `name`, `canonicalName`, `isDeleted`, `kind`, `repository`
- `fields[scmProviders]` ([string]): **Allowed Values**: `scmProviderType`, `url`, `repositories`
- `include` ([string]): **Allowed Values**: `scmProvider`, `defaultBranch`

## Responses

- `200` OK (`ScmRepositoriesResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Provider Information
- [List all source code management providers](./get-v1-scmproviders.md)
  List all source code management providers you connected to Xcode Cloud.
- [Get a source code management provider](./get-v1-scmproviders-_id_.md)
  Get information about a specific source code management provider you connected to Xcode Cloud.
- [List repository IDs for an SCM provider](./get-v1-scmproviders-_id_-relationships-repositories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-scmproviders-_id_-repositories)*