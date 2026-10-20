# CiAction

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A step within an Xcode Cloud workflow, such as building, running tests, analyzing, or deploying an app.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiAction
```

## Topics

### Objects
- [object CiAction.TestConfiguration](./ciaction/testconfiguration-data.dictionary.md)
  The test configuration for a test action.

## Properties

- `actionType` (CiActionType): The type of the action.
- `buildDistributionAudience` (BuildAudienceType): A type that indicates whether a build’s artifact is eligible for release on the App Store.
- `destination` (string): A string that describes the destination Xcode Cloud uses for an action.

  **Allowed Values**: `ANY_IOS_DEVICE`, `ANY_IOS_SIMULATOR`, `ANY_TVOS_DEVICE`, `ANY_TVOS_SIMULATOR`, `ANY_WATCHOS_DEVICE`, `ANY_WATCHOS_SIMULATOR`, `ANY_MAC`, `ANY_MAC_CATALYST`, `ANY_VISIONOS_DEVICE`, `ANY_VISIONOS_SIMULATOR`
- `isRequiredToPass` (boolean): A Boolean value that indicates whether the action must succeed in order for a build to succeed.
- `name` (string): The name of the action; for example, archive or test.
- `platform` (string): The platform Xcode Cloud uses for the action.

  **Allowed Values**: `MACOS`, `IOS`, `TVOS`, `WATCHOS`, `VISIONOS`
- `scheme` (string): The name of the scheme that Xcode Cloud uses to perform the action.
- `testConfiguration` (CiAction.TestConfiguration): An action’s test configuration. Only set this field for test actions.

## See Also

### Objects and types
- [object CiWorkflow](./ciworkflow.md)
  An Xcode Cloud automation configuration specifying when to build, which actions to run, and how to distribute the output.
- [object CiWorkflowCreateRequest](./ciworkflowcreaterequest.md)
  The request body you use to create a new Xcode Cloud workflow.
- [object CiWorkflowUpdateRequest](./ciworkflowupdaterequest.md)
  The request body you use to update an Xcode Cloud workflow.
- [object CiWorkflowResponse](./ciworkflowresponse.md)
  The response body for endpoints that create, read, or modify an Xcode Cloud workflow.
- [object CiWorkflowsResponse](./ciworkflowsresponse.md)
  The response body for endpoints that list Xcode Cloud workflows for a product.
- [object CiBuildRunsResponse](./cibuildrunsresponse.md)
  The response body for endpoints that list build runs for an Xcode Cloud workflow.
- [object CiManualBranchStartCondition](./cimanualbranchstartcondition.md)
  A workflow start condition that triggers an Xcode Cloud build when a specified branch is manually selected.
- [object CiManualPullRequestStartCondition](./cimanualpullrequeststartcondition.md)
  A workflow start condition that triggers an Xcode Cloud build for a manually specified pull request.
- [object CiManualTagStartCondition](./cimanualtagstartcondition.md)
  A workflow start condition that triggers an Xcode Cloud build when a specified tag is manually selected.
- [object CiWorkflowBuildRunsLinkagesResponse](./ciworkflowbuildrunslinkagesresponse.md)
- [object CiWorkflowRepositoryLinkageResponse](./ciworkflowrepositorylinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciaction)*