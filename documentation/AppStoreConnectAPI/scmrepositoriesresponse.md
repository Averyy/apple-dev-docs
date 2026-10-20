# ScmRepositoriesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that list SCM repositories connected to Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object ScmRepositoriesResponse
```

## Properties

- `data` ([ScmRepository]) *(required)*: The resource data.
- `included` ([*]): The requested relationship data.

  **Allowed Types**: `ScmGitReference`, `ScmProvider`
- `links` (PagedDocumentLinks) *(required)*: The navigational links that include the self-link.
- `meta` (PagingInformation): The paging information.

## See Also

### Objects
- [object ScmRepository](./scmrepository.md)
  A source code repository connected to Xcode Cloud, used as the source for workflow builds.
- [object ScmRepositoryResponse](./scmrepositoryresponse.md)
  The response body for endpoints that read a single SCM repository connected to Xcode Cloud.
- [object ScmRepositoryGitReferencesLinkagesResponse](./scmrepositorygitreferenceslinkagesresponse.md)
- [object ScmRepositoryPullRequestsLinkagesResponse](./scmrepositorypullrequestslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmrepositoriesresponse)*