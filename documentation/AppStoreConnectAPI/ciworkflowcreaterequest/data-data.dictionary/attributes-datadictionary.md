# CiWorkflowCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes you set that describe the new Xcode Cloud workflow resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiWorkflowCreateRequest.Data.Attributes
```

## Properties

- `actions` ([CiAction]) *(required)*: The workflow’s actions.
- `clean` (boolean) *(required)*: A Boolean value that indicates whether Xcode Cloud should perform a clean build.
- `containerFilePath` (string) *(required)*: The relative path to your Xcode project or workspace.
- `description` (string) *(required)*: The workflow description.
- `isEnabled` (boolean) *(required)*: A Boolean value that indicates whether the workflow is active or deactivated.
- `name` (string) *(required)*: The name of the workflow you want to create; for example, `My New Workflow`.
- `isLockedForEditing` (boolean): A Boolean value that indicates whether edits to the workflow are restricted.
- `pullRequestStartCondition` (CiPullRequestStartCondition): A start condition that starts new builds for changes to a pull request.
- `scheduledStartCondition` (CiScheduledStartCondition): A start condition that starts new builds based on a custom schedule.
- `branchStartCondition` (CiBranchStartCondition): A start condition that starts new builds for changes to a branch.
- `tagStartCondition` (CiTagStartCondition): A start condition that starts new builds for changes to a tag.
- `manualBranchStartCondition` (CiManualBranchStartCondition)
- `manualPullRequestStartCondition` (CiManualPullRequestStartCondition)
- `manualTagStartCondition` (CiManualTagStartCondition)

## See Also

- [object CiWorkflowCreateRequest.Data.Relationships](ciworkflowcreaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciworkflowcreaterequest/data-data.dictionary/attributes-data.dictionary)*