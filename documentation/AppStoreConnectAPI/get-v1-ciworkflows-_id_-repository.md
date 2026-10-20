# Read the repository information for an xcode cloud workflow

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about the Git repository of a specific Xcode Cloud workflow.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below retrieves information about an Xcode Cloud workflow’s repository. Use the data provided in the response to read additional information; for example, pull request information.

##### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/ciWorkflows/3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f/repository
```

**Response**:

```json
{
    "data": {
      "type": "scmRepositories",
      "id": "a2b04ba9-85fa-478c-87a2-b6d19626b870",
      "attributes": {
        "lastAccessedDate": null,
        "httpCloneUrl": "https://github.com/foo/bar.git",
        "sshCloneUrl": "ssh://git@github.com/foo/bar.git",
        "ownerName": "foo",
        "repositoryName": "bar"
      },
      "relationships": {
        "gitReferences": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/scmRepositories/a2b04ba9-85fa-478c-87a2-b6d19626b870/relationships/gitReferences",
            "related": "https://api.appstoreconnect.apple.com/v1/scmRepositories/a2b04ba9-85fa-478c-87a2-b6d19626b870/gitReferences"
          }
        },
        "pullRequests": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/scmRepositories/a2b04ba9-85fa-478c-87a2-b6d19626b870/relationships/pullRequests",
            "related": "https://api.appstoreconnect.apple.com/v1/scmRepositories/a2b04ba9-85fa-478c-87a2-b6d19626b870/pullRequests"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/scmRepositories/a2b04ba9-85fa-478c-87a2-b6d19626b870"
      }
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/scmRepositories/a2b04ba9-85fa-478c-87a2-b6d19626b870"
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciWorkflows/{id}/repository`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Workflows  resource.

### Query Parameters

- `fields[scmRepositories]` ([string]): Additional fields to include for the Repositories resource returned by the response.

  **Allowed Values**: `lastAccessedDate`, `httpCloneUrl`, `sshCloneUrl`, `ownerName`, `repositoryName`, `scmProvider`, `defaultBranch`, `gitReferences`, `pullRequests`
- `fields[scmGitReferences]` ([string]): **Allowed Values**: `name`, `canonicalName`, `isDeleted`, `kind`, `repository`
- `fields[scmProviders]` ([string]): **Allowed Values**: `scmProviderType`, `url`, `repositories`
- `include` ([string]): **Allowed Values**: `scmProvider`, `defaultBranch`

## Responses

- `200` OK (`ScmRepositoryResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Xcode Cloud Workflows
- [Read xcode cloud workflow information](./get-v1-ciworkflows-_id_.md)
  Get information about a specific Xcode Cloud workflow.
- [List all xcode cloud builds for a workflow](./get-v1-ciworkflows-_id_-buildruns.md)
  List all builds Xcode Cloud performed for a specific workflow.
- [List build run IDs for a CI workflow](./get-v1-ciworkflows-_id_-relationships-buildruns.md)
- [Get the repository ID for a CI workflow](./get-v1-ciworkflows-_id_-relationships-repository.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciworkflows-_id_-repository)*