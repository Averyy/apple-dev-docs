# Products

**Framework**: App Store Connect API

Read information about the products Xcode Cloud detected or delete a product and all its associated information.

#### Overview

The `ciProducts` resource represents the products [`Xcode Cloud`](https://developer.apple.com/documentation/xcode/xcode-cloud) detected when you started using Xcode Cloud. The resource includes information associated with the product like your app, workflows, builds, and Git repositories.

In addition to viewing your product and its associated information, you can use the `ciProducts` resource to delete a product and its associated data.

> ❗ **Important**:  Deleting a product deletes all associated data, including build information like build artifacts, and can’t be undone.

This resource supports JSON web tokens with a lifetime of up to six months. For more information, see [`Determine the Appropriate Token Lifetime`](generating-tokens-for-api-requests#Determine-the-Appropriate-Token-Lifetime.md).

## Topics

### Getting Xcode Cloud Products
- [List all xcode cloud products](get-v1-ciproducts.md)
  Get a list of all products you created in Xcode Cloud.
- [Read xcode cloud product information](get-v1-ciproducts-_id_.md)
  Get information about a specific Xcode Cloud product.
- [List all additional repositories for an xcode cloud product](get-v1-ciproducts-_id_-additionalrepositories.md)
  List all additional Git repositories you associated with an Xcode Cloud product.
- [List additional repository IDs for a CI product](get-v1-ciproducts-_id_-relationships-additionalrepositories.md)
- [Read app information for an xcode cloud product](get-v1-ciproducts-_id_-app.md)
  Get the app in App Store Connect that’s related to an Xcode Cloud product.
- [Get the app ID for a CI product](get-v1-ciproducts-_id_-relationships-app.md)
- [List all xcode cloud builds for an xcode cloud product](get-v1-ciproducts-_id_-buildruns.md)
  List all builds Xcode Cloud performed for a specific product.
- [List build run IDs for a CI product](get-v1-ciproducts-_id_-relationships-buildruns.md)
- [List all primary git repositories for an xcode cloud product](get-v1-ciproducts-_id_-primaryrepositories.md)
  List all primary Git repositories for a specific Xcode Cloud product.
- [List primary repository IDs for a CI product](get-v1-ciproducts-_id_-relationships-primaryrepositories.md)
- [List all workflows for an xcode cloud product](get-v1-ciproducts-_id_-workflows.md)
  List all workflows for a specific Xcode Cloud product.
- [List workflow IDs for a CI product](get-v1-ciproducts-_id_-relationships-workflows.md)
- [Read the xcode cloud product for an app](get-v1-apps-_id_-ciproduct.md)
  Get the Xcode Cloud product information for an app you build with Xcode Cloud.
### Deleting Xcode Cloud Products
- [Delete a product](delete-v1-ciproducts-_id_.md)
  Delete an Xcode Cloud product and all of its associated workflows, builds, and artifacts.
### Objects
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
- [type CiActionType](ciactiontype.md)
  A string that represents the type of an Xcode Cloud workflow’s action.
- [type CiCompletionStatus](cicompletionstatus.md)
  A string that represents the completion status of an Xcode Cloud build.
- [type CiExecutionProgress](ciexecutionprogress.md)
  A string that represents the progress of an ongoing Xcode Cloud build.
- [type CiTestDestinationKind](citestdestinationkind.md)
  The string that represents the kind of a test destination.
- [type CiTestStatus](citeststatus.md)
  A string that represents test status information.

## See Also

- [Workflows](workflows.md)
  Manage Xcode Cloud workflows and view workflow details like actions and start conditions.
- [macOS Versions](macos-versions.md)
  Read macOS version information you configure for an Xcode Cloud workflow.
- [Xcode Versions](xcode-versions.md)
  Read Xcode version information you configure for an Xcode Cloud workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/products)*