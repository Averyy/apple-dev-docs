# CiBranchStartCondition

**Framework**: App Store Connect API  
**Kind**: dictionary

Settings for a start condition that starts a build if a branch changes.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiBranchStartCondition
```

## Topics

### Objects
- [object CiBranchPatterns](cibranchpatterns.md)
  Case-sensitive patterns Xcode Cloud uses to determine if a change meets branch names you configure for a workflow’s start condition.

## Properties

- `autoCancel` (boolean): A Boolean value that indicates whether Xcode Cloud automatically cancels or skips builds.
- `filesAndFoldersRule` (CiFilesAndFoldersRule): Settings Xcode Cloud uses to determine whether a change to a branch should start a new build or not.
- `source` (CiBranchPatterns): The source branch name and custom patterns you configure for a workflow that starts a new build for changes to a branch.

## See Also

- [object CiProduct](ciproduct.md)
  An app or framework registered in Xcode Cloud that has one or more workflows and build history.
- [object CiProductResponse](ciproductresponse.md)
  The response body for endpoints that read a single Xcode Cloud product.
- [object CiProductsResponse](ciproductsresponse.md)
  The response body for endpoints that list Xcode Cloud products.
- [object CiProductAdditionalRepositoriesLinkagesResponse](ciproductadditionalrepositorieslinkagesresponse.md)
- [object CiProductAppLinkageResponse](ciproductapplinkageresponse.md)
- [object CiProductBuildRunsLinkagesResponse](ciproductbuildrunslinkagesresponse.md)
- [object CiProductPrimaryRepositoriesLinkagesResponse](ciproductprimaryrepositorieslinkagesresponse.md)
- [object CiProductWorkflowsLinkagesResponse](ciproductworkflowslinkagesresponse.md)
- [object CiFilesAndFoldersRule](cifilesandfoldersrule.md)
  Settings Xcode Cloud uses to determine whether a change should start a new build or not.
- [object CiGitUser](cigituser.md)
  The Git identity (name and email) of the person who authored or committed the code change that triggered an Xcode Cloud build.
- [object CiIssueCounts](ciissuecounts.md)
  A summary of the warnings, errors, analyzer warnings, and test failures in an Xcode Cloud build run.
- [object CiPullRequestStartCondition](cipullrequeststartcondition.md)
  Settings for a start condition that starts a build if a pull request changes.
- [object CiScheduledStartCondition](cischeduledstartcondition.md)
  Settings for a start condition that starts a build based on a schedule.
- [object CiTagStartCondition](citagstartcondition.md)
  Settings for a start condition that starts a build if a Git tag changes.
- [object CiTestDestination](citestdestination.md)
  The test destination of a test action that Xcode Cloud performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibranchstartcondition)*