# CiTestDestination

**Framework**: App Store Connect API  
**Kind**: dictionary

The test destination of a test action that Xcode Cloud performs.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiTestDestination
```

## Properties

- `deviceTypeIdentifier` (string): A string that uniquely identifies the simulated device Xcode Cloud uses for a test action, for example, `com.apple.CoreSimulator.SimDeviceType.iPhone-12`.
- `deviceTypeName` (string): The display name of the simulated device that Xcode Cloud uses for a test action, for example, iPhone 12.
- `kind` (CiTestDestinationKind): A string that indicates whether a test destination is a simulated device or a Mac.
- `runtimeIdentifier` (string): A string that identifies the simulated environment that Xcode Cloud uses for a test action.
- `runtimeName` (string): The name of the operating system of the simulated environment that Xcode Cloud uses for a test action.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/citestdestination)*