# CiBuildRunCreateRequest.Data.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships to other resources that you can set with this request.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiBuildRunCreateRequest.Data.Relationships
```

## Topics

### Objects
- [object CiBuildRunCreateRequest.Data.Relationships.BuildRun](./relationships-data.dictionary/buildrun-data.dictionary.md)
  The relationship to the Build Runs resource you can set with the request that creates a Build Runs resource.
- [object CiBuildRunCreateRequest.Data.Relationships.PullRequest](./relationships-data.dictionary/pullrequest-data.dictionary.md)
  The relationship to the Pull Requests resource you can set with the request that creates a Build Runs resource.
- [object CiBuildRunCreateRequest.Data.Relationships.SourceBranchOrTag](./relationships-data.dictionary/sourcebranchortag-data.dictionary.md)
  The relationship to the Git References resource that represents the source branch or tag you can set with the request that creates a Build Runs resource.
- [object CiBuildRunCreateRequest.Data.Relationships.Workflow](./relationships-data.dictionary/workflow-data.dictionary.md)
  The relationship to the Workflows resource you can set with the request that creates a Build Runs resource.

## Properties

- `workflow` (CiBuildRunCreateRequest.Data.Relationships.Workflow): The related Workflows resource.
- `buildRun` (CiBuildRunCreateRequest.Data.Relationships.BuildRun): The related Build Runs resource.
- `pullRequest` (CiBuildRunCreateRequest.Data.Relationships.PullRequest): The related Pull Requests resource.
- `sourceBranchOrTag` (CiBuildRunCreateRequest.Data.Relationships.SourceBranchOrTag): The related Git References resource.

## See Also

### Objects
- [object CiBuildRunCreateRequest.Data.Attributes](./attributes-data.dictionary.md)
  The attributes you set that describe the new Build Runs resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildruncreaterequest/data-data.dictionary/relationships-data.dictionary)*