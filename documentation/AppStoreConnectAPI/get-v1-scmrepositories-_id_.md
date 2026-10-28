# Read git repository information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a Git repository that Xcode Cloud can access.

**Availability**:
- App Store Connect API 1.5+

## Discussion

The example request below retrieves information about a specific Git repository that Xcode Cloud can access. Use the data provided in the response to read additional information; for example, pull request information.

### Example Request and Response

**Request**:

```
GET https://api.appstoreconnect.apple.com/v1/scmRepositories/a2b04ba9-85fa-478c-87a2-b6d19626b870
```

**Response**:

```json
{
    “data”: {
      “type”: “scmRepositories”,
      “id”: “a2b04ba9-85fa-478c-87a2-b6d19626b870”,
      “attributes”: {
        “lastAccessedDate”: null,
        “httpCloneUrl”: “https://github.com/foo/bar.git”,
        “sshCloneUrl”: “ssh://git@github.com/foo/bar.git”,
        “ownerName”: “foo”,
        “repositoryName”: “bar”
      },
      “relationships”: {
        “gitReferences”: {
          “links”: {
            “self”: “https://api.appstoreconnect.apple.com/v1/scmRepositories/a2b04ba9-85fa-478c-87a2-b6d19626b870/relationships/gitReferences”,
            “related”: “https://api.appstoreconnect.apple.com/v1/scmRepositories/a2b04ba9-85fa-478c-87a2-b6d19626b870/gitReferences”
          }
        },
        “pullRequests”: {
          “links”: {
            “self”: “https://api.appstoreconnect.apple.com/v1/scmRepositories/a2b04ba9-85fa-478c-87a2-b6d19626b870/relationships/pullRequests”,
            “related”: “https://api.appstoreconnect.apple.com/v1/scmRepositories/a2b04ba9-85fa-478c-87a2-b6d19626b870/pullRequests”
          }
        }
      },
      “links”: {
        “self”: “https://api.appstoreconnect.apple.com/v1/scmRepositories/a2b04ba9-85fa-478c-87a2-b6d19626b870”
      }
    },
    “links”: {
      “self”: “https://api.appstoreconnect.apple.com/v1/scmRepositories/a2b04ba9-85fa-478c-87a2-b6d19626b870”
    }
  }
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/scmRepositories/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Repositories resource.

### Query Parameters

- `fields[scmGitReferences]` ([string]): Additional fields to include for the Repositories resource returned by the response.

  **Allowed Values**: `name`, `canonicalName`, `isDeleted`, `kind`, `repository`
- `fields[scmRepositories]` ([string]): Additional fields to include for the Repositories resource returned by the response.

  **Allowed Values**: `lastAccessedDate`, `httpCloneUrl`, `sshCloneUrl`, `ownerName`, `repositoryName`, `scmProvider`, `defaultBranch`, `gitReferences`, `pullRequests`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `scmProvider`, `defaultBranch`
- `fields[scmProviders]` ([string]): **Allowed Values**: `scmProviderType`, `url`, `repositories`

## Responses

- `200` OK (`ScmRepositoryResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Repository Information
- [List all git repositories](./get-v1-scmrepositories.md)
  List all Git repositories Xcode Cloud can access.
- [List all git references for a repository](./get-v1-scmrepositories-_id_-gitreferences.md)
  List all Git references for a specific repository that Xcode Cloud can access.
- [List Git reference IDs for an SCM repository](./get-v1-scmrepositories-_id_-relationships-gitreferences.md)
- [List all pull requests for a repository](./get-v1-scmrepositories-_id_-pullrequests.md)
  List all pull requests for a specific repository that Xcode Cloud can access.
- [List pull request IDs for an SCM repository](./get-v1-scmrepositories-_id_-relationships-pullrequests.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-scmrepositories-_id_)*