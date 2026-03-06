# CiWorkflow

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a Workflows resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiWorkflow
```

## Topics

### Objects
- [object CiWorkflow.Attributes](ciworkflow/attributes-data.dictionary.md)
  The attributes that describe a Workflows resource.
- [object CiWorkflow.Relationships](ciworkflow/relationships-data.dictionary.md)
  The relationships of the Workflows resource you included in the request and those on which you can operate.

## Properties

- `attributes` (CiWorkflow.Attributes): The attributes that describe the Workflows resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a Workflows resource.
- `links` (ResourceLinks): The navigational links that include the self-link.
- `relationships` (CiWorkflow.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object CiAction](ciaction.md)
  The data structure that represents an Xcode Cloud workflow action resource.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciworkflow)*