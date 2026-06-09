# ScmRepositoryResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read a single SCM repository connected to Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object ScmRepositoryResponse
```

## Properties

- `data` (ScmRepository) *(required)*: The resource data.
- `included` ([*]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: The navigational links that include the self-link.

## See Also

- [object ScmRepository](scmrepository.md)
  A source code repository connected to Xcode Cloud, used as the source for workflow builds.
- [object ScmRepositoriesResponse](scmrepositoriesresponse.md)
  The response body for endpoints that list SCM repositories connected to Xcode Cloud.
- [object ScmRepositoryGitReferencesLinkagesResponse](scmrepositorygitreferenceslinkagesresponse.md)
- [object ScmRepositoryPullRequestsLinkagesResponse](scmrepositorypullrequestslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmrepositoryresponse)*