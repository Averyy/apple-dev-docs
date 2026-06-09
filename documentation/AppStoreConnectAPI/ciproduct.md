# CiProduct

**Framework**: App Store Connect API  
**Kind**: dictionary

An app or framework registered in Xcode Cloud that has one or more workflows and build history.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiProduct
```

## Topics

### Objects
- [object CiProduct.Attributes](ciproduct/attributes-data.dictionary.md)
  The attributes that describe a Products resource.
- [object CiProduct.Relationships](ciproduct/relationships-data.dictionary.md)
  The relationships of the Products resource you included in the request and those on which you can operate.

## Properties

- `attributes` (CiProduct.Attributes): The attributes that describe the Products resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a Products resource.
- `links` (ResourceLinks): The navigational links that include the self-link.
- `relationships` (CiProduct.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object CiProductResponse](ciproductresponse.md)
  The response body for endpoints that read a single Xcode Cloud product.
- [object CiProductsResponse](ciproductsresponse.md)
  The response body for endpoints that list Xcode Cloud products.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciproduct)*