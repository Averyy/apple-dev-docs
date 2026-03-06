# CiCompletionStatus

**Framework**: App Store Connect API  
**Kind**: typealias

A string that represents the completion status of an Xcode Cloud build.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
string CiCompletionStatus
```

#### Possible Values

- **SUCCEEDED**: Xcode Cloud successfully completed a build.
- **FAILED**: The Xcode Cloud build failed; for example, if you configure the Required to Pass setting for a test action and a unit test fails. For more information, see Add a Test Action in Configuring your Xcode Cloud workflow’s actions.
- **ERRORED**: Xcode Cloud encountered an internal error when it performed the build.
- **CANCELED**: Xcode Cloud canceled the build because you manually canceled an ongoing build or because you enabled the Auto-cancel Builds setting for a workflow. For more information about the Auto-cancel Builds setting, see Xcode Cloud workflow reference.
- **SKIPPED**: Xcode Cloud skipped the build; for example, if you configure the Auto- termcancel Builds setting for a workflow and push many changes in quick succession.

## See Also

- [object CiProduct](ciproduct.md)
  The data structure that represents a Products resource.
- [object CiProductResponse](ciproductresponse.md)
  A response that contains a single Products resource.
- [object CiProductsResponse](ciproductsresponse.md)
  A response that contains a list of Products resources.
- [object CiProductAdditionalRepositoriesLinkagesResponse](ciproductadditionalrepositorieslinkagesresponse.md)
- [object CiProductAppLinkageResponse](ciproductapplinkageresponse.md)
- [object CiProductBuildRunsLinkagesResponse](ciproductbuildrunslinkagesresponse.md)
- [object CiProductPrimaryRepositoriesLinkagesResponse](ciproductprimaryrepositorieslinkagesresponse.md)
- [object CiProductWorkflowsLinkagesResponse](ciproductworkflowslinkagesresponse.md)
- [object CiBranchStartCondition](cibranchstartcondition.md)
  Settings for a start condition that starts a build if a branch changes.
- [object CiFilesAndFoldersRule](cifilesandfoldersrule.md)
  Settings Xcode Cloud uses to determine whether a change should start a new build or not.
- [object CiGitUser](cigituser.md)
  The data structure that represents a Git Users resource.
- [object CiIssueCounts](ciissuecounts.md)
  The data structure that represents an Issue Counts resource.
- [object CiPullRequestStartCondition](cipullrequeststartcondition.md)
  Settings for a start condition that starts a build if a pull request changes.
- [object CiScheduledStartCondition](cischeduledstartcondition.md)
  Settings for a start condition that starts a build based on a schedule.
- [object CiTagStartCondition](citagstartcondition.md)
  Settings for a start condition that starts a build if a Git tag changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cicompletionstatus)*