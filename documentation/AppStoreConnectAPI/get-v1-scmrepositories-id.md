# Read git repository information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a Git repository that Xcode Cloud can access.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below retrieves information about a specific Git repository that Xcode Cloud can access. Use the data provided in the response to read additional information; for example, pull request information.

##### Example Request and Response

**Request**:

```None
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

- `fields[scmGitReferences]` ([string]): Additional fields to include for the Repositories resource returned by the response.
- `fields[scmRepositories]` ([string]): Additional fields to include for the Repositories resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[scmProviders]` ([string])

## See Also

- [List all git repositories](get-v1-scmrepositories.md)
  List all Git repositories Xcode Cloud can access.
- [List all git references for a repository](get-v1-scmrepositories-_id_-gitreferences.md)
  List all Git references for a specific repository that Xcode Cloud can access.
- [List Git reference IDs for an SCM repository](get-v1-scmrepositories-_id_-relationships-gitreferences.md)
- [List all pull requests for a repository](get-v1-scmrepositories-_id_-pullrequests.md)
  List all pull requests for a specific repository that Xcode Cloud can access.
- [List pull request IDs for an SCM repository](get-v1-scmrepositories-_id_-relationships-pullrequests.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-scmrepositories-_id_)*