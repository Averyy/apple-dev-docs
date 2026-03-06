# CiTestStatus

**Framework**: App Store Connect API  
**Kind**: typealias

A string that represents test status information.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
string CiTestStatus
```

#### Possible Values

- **SUCCESS**: The tests passed.
- **FAILURE**: The tests failed.
- **MIXED**: Some tests passed and some failed.
- **SKIPPED**: Xcode Cloud skipped some tests.
- **EXPECTED_FAILURE**: Tests failed that you marked as expected to fail with [XCTExpectFailure](https://developer.apple.com/documentation/xctest/3726077- termxctexpectfailure).

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/citeststatus)*