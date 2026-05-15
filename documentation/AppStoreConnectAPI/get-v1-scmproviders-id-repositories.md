# List All Repositories for a Source Code Management Provider

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all Git repositories for a specific source code management provider you connected to Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/scmProviders/{id}/repositories`

## Parameters

- `fields[scmRepositories]` ([string]): Additional fields to include for each Repositories resource returned by the response.
- `filter[id]` ([string]): Filter the returned repositories using the ID of the Repositories resource.
- `limit` (integer): The number of Repositories resources to return.
- `fields[scmGitReferences]` ([string])
- `fields[scmProviders]` ([string])
- `include` ([string])

## See Also

- [List All Source Code Management Providers](get-v1-scmproviders.md)
  List all source code management providers you connected to Xcode Cloud.
- [Get a Source Code Management Provider](get-v1-scmproviders-_id_.md)
  Get information about a specific source code management provider you connected to Xcode Cloud.
- [GET /v1/scmProviders/{id}/relationships/repositories](get-v1-scmproviders-_id_-relationships-repositories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-scmproviders-_id_-repositories)*