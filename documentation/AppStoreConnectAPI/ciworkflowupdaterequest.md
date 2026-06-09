# CiWorkflowUpdateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to update an Xcode Cloud workflow.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiWorkflowUpdateRequest
```

## Topics

### Objects
- [object CiWorkflowUpdateRequest.Data](ciworkflowupdaterequest/data-data.dictionary.md)
  The data element of the request you use to update an Xcode Cloud workflow.

## Properties

- `data` (CiWorkflowUpdateRequest.Data) *(required)*: The resource data.

## See Also

- [object CiWorkflow](ciworkflow.md)
  An Xcode Cloud automation configuration specifying when to build, which actions to run, and how to distribute the output.
- [object CiAction](ciaction.md)
  A step within an Xcode Cloud workflow, such as building, running tests, analyzing, or deploying an app.
- [object CiWorkflowCreateRequest](ciworkflowcreaterequest.md)
  The request body you use to create a new Xcode Cloud workflow.
- [object CiWorkflowResponse](ciworkflowresponse.md)
  The response body for endpoints that create, read, or modify an Xcode Cloud workflow.
- [object CiWorkflowsResponse](ciworkflowsresponse.md)
  The response body for endpoints that list Xcode Cloud workflows for a product.
- [object CiBuildRunsResponse](cibuildrunsresponse.md)
  The response body for endpoints that list build runs for an Xcode Cloud workflow.
- [object CiManualBranchStartCondition](cimanualbranchstartcondition.md)
  A workflow start condition that triggers an Xcode Cloud build when a specified branch is manually selected.
- [object CiManualPullRequestStartCondition](cimanualpullrequeststartcondition.md)
  A workflow start condition that triggers an Xcode Cloud build for a manually specified pull request.
- [object CiManualTagStartCondition](cimanualtagstartcondition.md)
  A workflow start condition that triggers an Xcode Cloud build when a specified tag is manually selected.
- [object CiWorkflowBuildRunsLinkagesResponse](ciworkflowbuildrunslinkagesresponse.md)
- [object CiWorkflowRepositoryLinkageResponse](ciworkflowrepositorylinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciworkflowupdaterequest)*