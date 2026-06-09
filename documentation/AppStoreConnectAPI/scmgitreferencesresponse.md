# ScmGitReferencesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list Git references in an Xcode Cloud repository.

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
  A Git branch, tag, or commit reference in a source code repository connected to Xcode Cloud.
- [object ScmGitReferenceResponse](scmgitreferenceresponse.md)
  The response body for endpoints that read a single SCM Git reference in Xcode Cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmgitreferencesresponse)*