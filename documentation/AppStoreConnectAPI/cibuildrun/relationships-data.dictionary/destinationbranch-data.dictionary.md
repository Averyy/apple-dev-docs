# CiBuildRun.Relationships.DestinationBranch

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data and links that describe the relationship between the Build Runs resource and the Git References resource that represents the destination branch.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiBuildRun.Relationships.DestinationBranch
```

## Topics

### Objects
- [object CiBuildRun.Relationships.DestinationBranch.Data](./destinationbranch-data.dictionary/data-data.dictionary.md)
  The type and ID of a related Git References resource that represents the build run’s destination branch.

## Properties

- `data` (CiBuildRun.Relationships.DestinationBranch.Data): The ID of the related Git References resource that represents the destination branch.

## See Also

### Objects
- [object CiBuildRun.Relationships.Builds](./builds-data.dictionary.md)
  The data, links, and paging information that describe the relationship between the Build Runs and the Builds resources.
- [object CiBuildRun.Relationships.Product](./product-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Products resources.
- [object CiBuildRun.Relationships.PullRequest](./pullrequest-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Pull Requests resources.
- [object CiBuildRun.Relationships.SourceBranchOrTag](./sourcebranchortag-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Git References resources.
- [object CiBuildRun.Relationships.Workflow](./workflow-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Workflows resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildrun/relationships-data.dictionary/destinationbranch-data.dictionary)*