# CiBuildRun.Relationships.SourceBranchOrTag

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data and links that describe the relationship between the Build Runs and the Git References resources.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiBuildRun.Relationships.SourceBranchOrTag
```

## Topics

### Objects
- [object CiBuildRun.Relationships.SourceBranchOrTag.Data](./sourcebranchortag-data.dictionary/data-data.dictionary.md)
  The type and ID of a related Git References resource that represents the source branch or tag.

## Properties

- `data` (CiBuildRun.Relationships.SourceBranchOrTag.Data): The ID and type of the related Git References resource that represents the source branch or tag.

## See Also

### Objects
- [object CiBuildRun.Relationships.Builds](./builds-data.dictionary.md)
  The data, links, and paging information that describe the relationship between the Build Runs and the Builds resources.
- [object CiBuildRun.Relationships.DestinationBranch](./destinationbranch-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs resource and the Git References resource that represents the destination branch.
- [object CiBuildRun.Relationships.Product](./product-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Products resources.
- [object CiBuildRun.Relationships.PullRequest](./pullrequest-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Pull Requests resources.
- [object CiBuildRun.Relationships.Workflow](./workflow-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Workflows resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildrun/relationships-data.dictionary/sourcebranchortag-data.dictionary)*