# List All Xcode Cloud Builds for a Workflow

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all builds Xcode Cloud performed for a specific workflow.

**Availability**:
- App Store Connect API 1.5+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciWorkflows/{id}/buildRuns`

## Parameters

- `fields[builds]` ([string]): Additional fields to include for each Build Runs resource returned by the response.
- `fields[ciBuildRuns]` ([string]): Additional fields to include for each Build Runs resource returned by the response.
- `filter[builds]` ([string]): Filter the returned build runs using the ID of the related Builds resource.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The number of Build Runs resources to return.
- `limit[builds]` (integer): The number of included Build Runs resources to return if the builds relationship is included.
- `fields[scmGitReferences]` ([string])
- `fields[ciWorkflows]` ([string])
- `fields[scmPullRequests]` ([string])
- `fields[ciProducts]` ([string])
- `sort` ([string])

## See Also

- [Read Xcode Cloud Workflow Information](get-v1-ciworkflows-_id_.md)
  Get information about a specific Xcode Cloud workflow.
- [Read the Repository Information for an Xcode Cloud Workflow](get-v1-ciworkflows-_id_-repository.md)
  Get information about the Git repository of a specific Xcode Cloud workflow.
- [GET /v1/ciWorkflows/{id}/relationships/buildRuns](get-v1-ciworkflows-_id_-relationships-buildruns.md)
- [GET /v1/ciWorkflows/{id}/relationships/repository](get-v1-ciworkflows-_id_-relationships-repository.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciworkflows-_id_-buildruns)*