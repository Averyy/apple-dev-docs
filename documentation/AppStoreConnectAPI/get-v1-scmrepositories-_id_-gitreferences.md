# List all git references for a repository

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all Git references for a specific repository that Xcode Cloud can access.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/scmRepositories/{id}/gitReferences`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Repositories resource.

### Query Parameters

- `fields[scmGitReferences]` ([string]): Additional fields to include for each Git References resource returned by the response.

  **Allowed Values**: `name`, `canonicalName`, `isDeleted`, `kind`, `repository`
- `limit` (integer): The number of Git References resources to return.

  **Maximum**: `200`
- `fields[scmRepositories]` ([string]): **Allowed Values**: `lastAccessedDate`, `httpCloneUrl`, `sshCloneUrl`, `ownerName`, `repositoryName`, `scmProvider`, `defaultBranch`, `gitReferences`, `pullRequests`
- `include` ([string]): **Allowed Values**: `repository`

## Responses

- `200` OK (`ScmGitReferencesResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Repository Information
- [List all git repositories](./get-v1-scmrepositories.md)
  List all Git repositories Xcode Cloud can access.
- [Read git repository information](./get-v1-scmrepositories-_id_.md)
  Get information about a Git repository that Xcode Cloud can access.
- [List Git reference IDs for an SCM repository](./get-v1-scmrepositories-_id_-relationships-gitreferences.md)
- [List all pull requests for a repository](./get-v1-scmrepositories-_id_-pullrequests.md)
  List all pull requests for a specific repository that Xcode Cloud can access.
- [List pull request IDs for an SCM repository](./get-v1-scmrepositories-_id_-relationships-pullrequests.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-scmrepositories-_id_-gitreferences)*