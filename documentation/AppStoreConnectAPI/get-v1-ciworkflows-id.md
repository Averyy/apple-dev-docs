# Read Xcode Cloud Workflow Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific Xcode Cloud workflow.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below accesses information about an Xcode Cloud workflow. Display the workflow data provided in the response on a dashboard or use it to read additional information; for example, detailed data about builds Xcode Cloud performed.

##### Example Request and Response

## See Also

- [List All Xcode Cloud Builds for a Workflow](get-v1-ciworkflows-_id_-buildruns.md)
  List all builds Xcode Cloud performed for a specific workflow.
- [Read the Repository Information for an Xcode Cloud Workflow](get-v1-ciworkflows-_id_-repository.md)
  Get information about the Git repository of a specific Xcode Cloud workflow.
- [GET /v1/ciWorkflows/{id}/relationships/buildRuns](get-v1-ciworkflows-_id_-relationships-buildruns.md)
- [GET /v1/ciWorkflows/{id}/relationships/repository](get-v1-ciworkflows-_id_-relationships-repository.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciworkflows-_id_)*