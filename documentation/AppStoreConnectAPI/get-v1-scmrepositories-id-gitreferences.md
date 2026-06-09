# List all git references for a repository

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all Git references for a specific repository that Xcode Cloud can access.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/scmRepositories/{id}/gitReferences`

## Parameters

- `fields[scmGitReferences]` ([string]): Additional fields to include for each Git References resource returned by the response.
- `limit` (integer): The number of Git References resources to return.
- `fields[scmRepositories]` ([string])
- `include` ([string])

## See Also

- [List all git repositories](get-v1-scmrepositories.md)
  List all Git repositories Xcode Cloud can access.
- [Read git repository information](get-v1-scmrepositories-_id_.md)
  Get information about a Git repository that Xcode Cloud can access.
- [List Git reference IDs for an SCM repository](get-v1-scmrepositories-_id_-relationships-gitreferences.md)
- [List all pull requests for a repository](get-v1-scmrepositories-_id_-pullrequests.md)
  List all pull requests for a specific repository that Xcode Cloud can access.
- [List pull request IDs for an SCM repository](get-v1-scmrepositories-_id_-relationships-pullrequests.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-scmrepositories-_id_-gitreferences)*