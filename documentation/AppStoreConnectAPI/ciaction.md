# CiAction

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents an Xcode Cloud workflow action resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiAction
```

## Topics

### Objects
- [object CiAction.TestConfiguration](ciaction/testconfiguration-data.dictionary.md)
  The test configuration for a test action.

## Properties

- `actionType` (CiActionType): The type of the action.
- `buildDistributionAudience` (BuildAudienceType): A type that indicates whether a build’s artifact is eligible for release on the App Store.
- `destination` (string): A string that describes the destination Xcode Cloud uses for an action.
- `isRequiredToPass` (boolean): A Boolean value that indicates whether the action must succeed in order for a build to succeed.
- `name` (string): The name of the action; for example, archive or test.
- `platform` (string): The platform Xcode Cloud uses for the action.
- `scheme` (string): The name of the scheme that Xcode Cloud uses to perform the action.
- `testConfiguration` (CiAction.TestConfiguration): An action’s test configuration. Only set this field for test actions.

## See Also

- [object CiWorkflow](ciworkflow.md)
  The data structure that represents a Workflows resource.
- [object CiWorkflowCreateRequest](ciworkflowcreaterequest.md)
  The request body you use to create a new Xcode Cloud workflow.
- [object CiWorkflowUpdateRequest](ciworkflowupdaterequest.md)
  The request body you use to update an Xcode Cloud workflow.
- [object CiWorkflowResponse](ciworkflowresponse.md)
  A response that contains a single Workflows resource.
- [object CiWorkflowsResponse](ciworkflowsresponse.md)
  A response that contains a list of Workflows resources.
- [object CiBuildRunsResponse](cibuildrunsresponse.md)
  A response that contains a list of Build Runs resources.
- [object CiManualBranchStartCondition](cimanualbranchstartcondition.md)
- [object CiManualPullRequestStartCondition](cimanualpullrequeststartcondition.md)
- [object CiManualTagStartCondition](cimanualtagstartcondition.md)
- [object CiWorkflowBuildRunsLinkagesResponse](ciworkflowbuildrunslinkagesresponse.md)
- [object CiWorkflowRepositoryLinkageResponse](ciworkflowrepositorylinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciaction)*