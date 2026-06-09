# List all xcode cloud builds for a workflow

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

- [Read xcode cloud workflow information](get-v1-ciworkflows-_id_.md)
  Get information about a specific Xcode Cloud workflow.
- [Read the repository information for an xcode cloud workflow](get-v1-ciworkflows-_id_-repository.md)
  Get information about the Git repository of a specific Xcode Cloud workflow.
- [List build run IDs for a CI workflow](get-v1-ciworkflows-_id_-relationships-buildruns.md)
- [Get the repository ID for a CI workflow](get-v1-ciworkflows-_id_-relationships-repository.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciworkflows-_id_-buildruns)*