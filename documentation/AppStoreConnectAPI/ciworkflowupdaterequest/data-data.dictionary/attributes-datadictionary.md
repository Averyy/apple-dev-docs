# CiWorkflowUpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes of the Workflows resource you’re changing with the update request.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiWorkflowUpdateRequest.Data.Attributes
```

## Properties

- `actions` ([CiAction]): The workflow’s actions.
- `clean` (boolean): A Boolean value that indicates whether Xcode Cloud should perform a clean build.
- `containerFilePath` (string): The path to your Xcode project or workspace.
- `description` (string): The workflow description.
- `isEnabled` (boolean): A Boolean value that indicates whether the workflow is active or deactivated.
- `name` (string): The name of the workflow you want to create; for example, `My Workflow`.
- `isLockedForEditing` (boolean): A Boolean value that indicates whether edits to the workflow are restricted.
- `pullRequestStartCondition` (CiPullRequestStartCondition): The workflow’s start condition for pull request changes.
- `scheduledStartCondition` (CiScheduledStartCondition): The workflow’s start condition that starts new builds on a custom schedule.
- `branchStartCondition` (CiBranchStartCondition): The workflow’s start condition that starts new builds for changes to a branch.
- `tagStartCondition` (CiTagStartCondition): The workflow’s start condition that starts new builds for changes to a tag.
- `manualBranchStartCondition` (CiManualBranchStartCondition)
- `manualPullRequestStartCondition` (CiManualPullRequestStartCondition)
- `manualTagStartCondition` (CiManualTagStartCondition)

## See Also

- [object CiWorkflowUpdateRequest.Data.Relationships](ciworkflowupdaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciworkflowupdaterequest/data-data.dictionary/attributes-data.dictionary)*