# Get the repository ID for a CI workflow

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciWorkflows/{id}/relationships/repository`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`CiWorkflowRepositoryLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Xcode Cloud Workflows
- [Read xcode cloud workflow information](./get-v1-ciworkflows-_id_.md)
  Get information about a specific Xcode Cloud workflow.
- [List all xcode cloud builds for a workflow](./get-v1-ciworkflows-_id_-buildruns.md)
  List all builds Xcode Cloud performed for a specific workflow.
- [Read the repository information for an xcode cloud workflow](./get-v1-ciworkflows-_id_-repository.md)
  Get information about the Git repository of a specific Xcode Cloud workflow.
- [List build run IDs for a CI workflow](./get-v1-ciworkflows-_id_-relationships-buildruns.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciworkflows-_id_-relationships-repository)*