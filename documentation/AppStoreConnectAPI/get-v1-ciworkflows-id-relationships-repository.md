# Get the repository ID for a CI workflow

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciWorkflows/{id}/relationships/repository`

## Parameters

- `id` (string) *(required)*

## See Also

- [Read xcode cloud workflow information](get-v1-ciworkflows-_id_.md)
  Get information about a specific Xcode Cloud workflow.
- [List all xcode cloud builds for a workflow](get-v1-ciworkflows-_id_-buildruns.md)
  List all builds Xcode Cloud performed for a specific workflow.
- [Read the repository information for an xcode cloud workflow](get-v1-ciworkflows-_id_-repository.md)
  Get information about the Git repository of a specific Xcode Cloud workflow.
- [List build run IDs for a CI workflow](get-v1-ciworkflows-_id_-relationships-buildruns.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciworkflows-_id_-relationships-repository)*