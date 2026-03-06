# ScmRepositoriesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a list of Repositories resources.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object ScmRepositoriesResponse
```

## Properties

- `data` ([ScmRepository]) *(required)*: The resource data.
- `included` ([*]): The requested relationship data.
- `links` (PagedDocumentLinks) *(required)*: The navigational links that include the self-link.
- `meta` (PagingInformation): The paging information.

## See Also

- [object ScmRepository](scmrepository.md)
  The data structure that represents a Repositories resource.
- [object ScmRepositoryResponse](scmrepositoryresponse.md)
  A response that contains a single Repositories resource.
- [object ScmRepositoryGitReferencesLinkagesResponse](scmrepositorygitreferenceslinkagesresponse.md)
- [object ScmRepositoryPullRequestsLinkagesResponse](scmrepositorypullrequestslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmrepositoriesresponse)*