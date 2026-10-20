# CiBuildRun.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships of the Build Runs resource you included in the request and those on which you can operate.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiBuildRun.Relationships
```

## Topics

### Objects
- [object CiBuildRun.Relationships.Builds](./relationships-data.dictionary/builds-data.dictionary.md)
  The data, links, and paging information that describe the relationship between the Build Runs and the Builds resources.
- [object CiBuildRun.Relationships.DestinationBranch](./relationships-data.dictionary/destinationbranch-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs resource and the Git References resource that represents the destination branch.
- [object CiBuildRun.Relationships.Product](./relationships-data.dictionary/product-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Products resources.
- [object CiBuildRun.Relationships.PullRequest](./relationships-data.dictionary/pullrequest-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Pull Requests resources.
- [object CiBuildRun.Relationships.SourceBranchOrTag](./relationships-data.dictionary/sourcebranchortag-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Git References resources.
- [object CiBuildRun.Relationships.Workflow](./relationships-data.dictionary/workflow-data.dictionary.md)
  The data and links that describe the relationship between the Build Runs and the Workflows resources.
### Dictionaries
- [object CiBuildRun.Relationships.Actions](./relationships-data.dictionary/actions-data.dictionary.md)

## Properties

- `destinationBranch` (CiBuildRun.Relationships.DestinationBranch): The data and links that describe the relationship between the Build Runs resource and the Git References resource that represents the destination branch.
- `product` (CiBuildRun.Relationships.Product): The data and links that describe the relationship between the Build Runs and the Products resources.
- `pullRequest` (CiBuildRun.Relationships.PullRequest): The data and links that describe the relationship between the Build Runs and the Pull Requests resources.
- `sourceBranchOrTag` (CiBuildRun.Relationships.SourceBranchOrTag): The data and links that describe the relationship between the Build Runs resource and the Git References resource that represents the source branch or tag.
- `workflow` (CiBuildRun.Relationships.Workflow): The data and links that describe the relationship between the Build Runs and the Workflows resources.
- `builds` (CiBuildRun.Relationships.Builds): The data and links that describe the relationship between the Build Runs and the Builds resources.
- `actions` (CiBuildRun.Relationships.Actions)

## See Also

### Objects
- [object CiBuildRun.Attributes](./attributes-data.dictionary.md)
  The attributes that describe a Build Runs resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildrun/relationships-data.dictionary)*