# Workflows

**Framework**: App Store Connect API

Manage Xcode Cloud workflows and view workflow details like actions and start conditions.

#### Overview

The `ciWorkflows` resource represents an Xcode Cloud workflow. Use it to:

- Read workflow information.
- Create a new workflow.
- Update an existing workflow.
- Delete a workflow you no longer need.

To learn more about workflows, see [`Xcode Cloud workflow reference`](https://developer.apple.com/documentation/Xcode/Xcode-Cloud-Workflow-Reference).

> ❗ **Important**:  Deleting a workflow also deletes associated build information and artifacts. Instead of deleting a workflow, consider deactivating it in Xcode or App Store Connect. To learn more about deactivating a workflow, see [`Developing a workflow strategy for Xcode Cloud`](https://developer.apple.com/documentation/Xcode/Developing-a-Workflow-Strategy-for-Xcode-Cloud).

 Deleting a workflow also deletes associated build information and artifacts. Instead of deleting a workflow, consider deactivating it in Xcode or App Store Connect. To learn more about deactivating a workflow, see [`Developing a workflow strategy for Xcode Cloud`](https://developer.apple.com/documentation/Xcode/Developing-a-Workflow-Strategy-for-Xcode-Cloud).

This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Xcode Cloud Workflows
- [Read Xcode Cloud Workflow Information](get-v1-ciworkflows-_id_.md)
  Get information about a specific Xcode Cloud workflow.
- [List All Xcode Cloud Builds for a Workflow](get-v1-ciworkflows-_id_-buildruns.md)
  List all builds Xcode Cloud performed for a specific workflow.
- [Read the Repository Information for an Xcode Cloud Workflow](get-v1-ciworkflows-_id_-repository.md)
  Get information about the Git repository of a specific Xcode Cloud workflow.
### Managing Xcode Cloud Workflows
- [Create a Workflow](post-v1-ciworkflows.md)
  Create a new Xcode Cloud workflow for an Xcode Cloud product.
- [Update an Xcode Cloud Workflow](patch-v1-ciworkflows-_id_.md)
  Make changes to an Xcode Cloud workflow.
- [Delete a Workflow](delete-v1-ciworkflows-_id_.md)
  Delete an Xcode Cloud workflow and all of its associated data.
### Objects and Types
- [object CiWorkflow](ciworkflow.md)
  The data structure that represents a Workflows resource.
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

## See Also

- [Products](products.md)
  Read information about the products Xcode Cloud detected or delete a product and all its associated information.
- [macOS Versions](macos-versions.md)
  Read macOS version information you configure for an Xcode Cloud workflow.
- [Xcode Versions](xcode-versions.md)
  Read Xcode version information you configure for an Xcode Cloud workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/workflows)*