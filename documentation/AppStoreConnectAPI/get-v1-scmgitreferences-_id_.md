# Read git reference information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific Git reference.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/scmGitReferences/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Git References resource.

### Query Parameters

- `fields[scmGitReferences]` ([string]): Additional fields to include for the Git References resource returned by the response.

  **Allowed Values**: `name`, `canonicalName`, `isDeleted`, `kind`, `repository`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `repository`
- `fields[scmRepositories]` ([string]): **Allowed Values**: `lastAccessedDate`, `httpCloneUrl`, `sshCloneUrl`, `ownerName`, `repositoryName`, `scmProvider`, `defaultBranch`, `gitReferences`, `pullRequests`

## Responses

- `200` OK (`ScmGitReferenceResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-scmgitreferences-_id_)*