# ScmRepository

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a Repositories resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object ScmRepository
```

## Topics

### Objects
- [object ScmRepository.Attributes](scmrepository/attributes-data.dictionary.md)
  The attributes that describe a Repositories resource.
- [object ScmRepository.Relationships](scmrepository/relationships-data.dictionary.md)
  The relationships of the Repositories resource you included in the request and those on which you can operate.

## Properties

- `attributes` (ScmRepository.Attributes): The attributes that describe the Repositories resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a Repositories resource.
- `links` (ResourceLinks): The navigational links that include the self-link.
- `relationships` (ScmRepository.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object ScmRepositoryResponse](scmrepositoryresponse.md)
  A response that contains a single Repositories resource.
- [object ScmRepositoriesResponse](scmrepositoriesresponse.md)
  A response that contains a list of Repositories resources.
- [object ScmRepositoryGitReferencesLinkagesResponse](scmrepositorygitreferenceslinkagesresponse.md)
- [object ScmRepositoryPullRequestsLinkagesResponse](scmrepositorypullrequestslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmrepository)*