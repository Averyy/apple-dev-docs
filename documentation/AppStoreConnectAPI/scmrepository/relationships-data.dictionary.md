# ScmRepository.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships of the Repositories resource you included in the request and those on which you can operate.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object ScmRepository.Relationships
```

## Topics

### Objects
- [object ScmRepository.Relationships.DefaultBranch](./relationships-data.dictionary/defaultbranch-data.dictionary.md)
  The data and links that describe the relationship between the Repositories resource and the Git References resource that represents the default branch.
- [object ScmRepository.Relationships.ScmProvider](./relationships-data.dictionary/scmprovider-data.dictionary.md)
  The data and links that describe the relationship between the Repositories and the Source Code Management Provider resources.
### Dictionaries
- [object ScmRepository.Relationships.GitReferences](./relationships-data.dictionary/gitreferences-data.dictionary.md)
- [object ScmRepository.Relationships.PullRequests](./relationships-data.dictionary/pullrequests-data.dictionary.md)

## Properties

- `defaultBranch` (ScmRepository.Relationships.DefaultBranch): The Git repository’s default branch.
- `gitReferences` (ScmRepository.Relationships.GitReferences)
- `pullRequests` (ScmRepository.Relationships.PullRequests)
- `scmProvider` (ScmRepository.Relationships.ScmProvider): The related Providers resource.

## See Also

### Objects
- [object ScmRepository.Attributes](./attributes-data.dictionary.md)
  The attributes that describe a Repositories resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmrepository/relationships-data.dictionary)*