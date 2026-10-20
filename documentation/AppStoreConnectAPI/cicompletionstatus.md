# CiCompletionStatus

**Framework**: App Store Connect API  
**Kind**: typealias  
**Role**: Type

A string that represents the completion status of an Xcode Cloud build.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
string CiCompletionStatus
```

## Possible Values

- `SUCCEEDED`: Xcode Cloud successfully completed a build.
- `FAILED`: The Xcode Cloud build failed; for example, if you configure the Required to Pass setting for a test action and a unit test fails. For more information, see [Add a Test Action in Configuring your Xcode Cloud workflow’s actions](../Xcode/configuring-your-xcode-cloud-workflow-s-actions.md#Add-a-test-action).
- `ERRORED`: Xcode Cloud encountered an internal error when it performed the build.
- `CANCELED`: Xcode Cloud canceled the build because you manually canceled an ongoing build or because you enabled the Auto-cancel Builds setting for a workflow. For more information about the Auto-cancel Builds setting, see [Xcode Cloud workflow reference](../Xcode/xcode-cloud-workflow-reference.md).
- `SKIPPED`: Xcode Cloud skipped the build; for example, if you configure the Auto-cancel Builds setting for a workflow and push many changes in quick succession.

## See Also

### Objects
- [object CiProduct](./ciproduct.md)
  An app or framework registered in Xcode Cloud that has one or more workflows and build history.
- [object CiProductResponse](./ciproductresponse.md)
  The response body for endpoints that read a single Xcode Cloud product.
- [object CiProductsResponse](./ciproductsresponse.md)
  The response body for endpoints that list Xcode Cloud products.
- [object CiProductAdditionalRepositoriesLinkagesResponse](./ciproductadditionalrepositorieslinkagesresponse.md)
- [object CiProductAppLinkageResponse](./ciproductapplinkageresponse.md)
- [object CiProductBuildRunsLinkagesResponse](./ciproductbuildrunslinkagesresponse.md)
- [object CiProductPrimaryRepositoriesLinkagesResponse](./ciproductprimaryrepositorieslinkagesresponse.md)
- [object CiProductWorkflowsLinkagesResponse](./ciproductworkflowslinkagesresponse.md)
- [object CiBranchStartCondition](./cibranchstartcondition.md)
  Settings for a start condition that starts a build if a branch changes.
- [object CiFilesAndFoldersRule](./cifilesandfoldersrule.md)
  Settings Xcode Cloud uses to determine whether a change should start a new build or not.
- [object CiGitUser](./cigituser.md)
  The Git identity (name and email) of the person who authored or committed the code change that triggered an Xcode Cloud build.
- [object CiIssueCounts](./ciissuecounts.md)
  A summary of the warnings, errors, analyzer warnings, and test failures in an Xcode Cloud build run.
- [object CiPullRequestStartCondition](./cipullrequeststartcondition.md)
  Settings for a start condition that starts a build if a pull request changes.
- [object CiScheduledStartCondition](./cischeduledstartcondition.md)
  Settings for a start condition that starts a build based on a schedule.
- [object CiTagStartCondition](./citagstartcondition.md)
  Settings for a start condition that starts a build if a Git tag changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cicompletionstatus)*