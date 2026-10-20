# List all git repositories

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all Git repositories Xcode Cloud can access.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/scmRepositories`

## Parameters

### Query Parameters

- `fields[scmGitReferences]` ([string]): Additional fields to include for each Repositories resource returned by the response.

  **Allowed Values**: `name`, `canonicalName`, `isDeleted`, `kind`, `repository`
- `fields[scmProviders]` ([string]): **Allowed Values**: `scmProviderType`, `url`, `repositories`
- `fields[scmRepositories]` ([string]): Additional fields to include for each Repositories resource returned by the response.

  **Allowed Values**: `lastAccessedDate`, `httpCloneUrl`, `sshCloneUrl`, `ownerName`, `repositoryName`, `scmProvider`, `defaultBranch`, `gitReferences`, `pullRequests`
- `filter[id]` ([string]): Filter the returned repositories using the ID of the Repositories resource.
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `scmProvider`, `defaultBranch`
- `limit` (integer): The number of Repositories resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`ScmRepositoriesResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Repository Information
- [Read git repository information](./get-v1-scmrepositories-_id_.md)
  Get information about a Git repository that Xcode Cloud can access.
- [List all git references for a repository](./get-v1-scmrepositories-_id_-gitreferences.md)
  List all Git references for a specific repository that Xcode Cloud can access.
- [List Git reference IDs for an SCM repository](./get-v1-scmrepositories-_id_-relationships-gitreferences.md)
- [List all pull requests for a repository](./get-v1-scmrepositories-_id_-pullrequests.md)
  List all pull requests for a specific repository that Xcode Cloud can access.
- [List pull request IDs for an SCM repository](./get-v1-scmrepositories-_id_-relationships-pullrequests.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-scmrepositories)*