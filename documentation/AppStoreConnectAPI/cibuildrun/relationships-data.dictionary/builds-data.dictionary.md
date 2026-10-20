# CiBuildRun.Relationships.Builds

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data, links, and paging information that describe the relationship between the Build Runs and the Builds resources.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiBuildRun.Relationships.Builds
```

## Topics

### Objects
- [object CiBuildRun.Relationships.Builds.Data](./builds-data.dictionary/data-data.dictionary.md)
  The type and ID of a related Builds resource.

## Properties

- `data` ([CiBuildRun.Relationships.Builds.Data]): The ID and type of the related Builds resource.
- `links` (RelationshipLinks): The navigational links that include the self-link.
- `meta` (PagingInformation): The paging information.

## See Also

### Objects
- [object CiBuildRun.Relationships.DestinationBranch](./destinationbranch-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs resource and the Git References resource that represents the destination branch.
- [object CiBuildRun.Relationships.Product](./product-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Products resources.
- [object CiBuildRun.Relationships.PullRequest](./pullrequest-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Pull Requests resources.
- [object CiBuildRun.Relationships.SourceBranchOrTag](./sourcebranchortag-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Git References resources.
- [object CiBuildRun.Relationships.Workflow](./workflow-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Workflows resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildrun/relationships-data.dictionary/builds-data.dictionary)*