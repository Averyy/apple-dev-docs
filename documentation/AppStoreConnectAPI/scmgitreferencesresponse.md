# ScmGitReferencesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a list of Git References resources.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object ScmGitReferencesResponse
```

## Properties

- `data` ([ScmGitReference]) *(required)*: The resource data.
- `included` ([ScmRepository]): The requested relationship data.
- `links` (PagedDocumentLinks) *(required)*: The navigational links that include the self-link.
- `meta` (PagingInformation): The paging information.

## See Also

- [object ScmGitReference](scmgitreference.md)
  The data structure that represents a Git References resource.
- [object ScmGitReferenceResponse](scmgitreferenceresponse.md)
  A response that contains a single Git References resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmgitreferencesresponse)*