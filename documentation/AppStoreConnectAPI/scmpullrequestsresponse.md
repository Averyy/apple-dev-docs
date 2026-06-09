# ScmPullRequestsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list SCM pull requests linked to Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object ScmPullRequestsResponse
```

## Properties

- `data` ([ScmPullRequest]) *(required)*: The resource data.
- `included` ([ScmRepository]): The requested relationship data.
- `links` (PagedDocumentLinks) *(required)*: The navigational links that include the self-link.
- `meta` (PagingInformation): The paging information.

## See Also

- [object ScmPullRequest](scmpullrequest.md)
  A pull request in a source code repository connected to Xcode Cloud, which can automatically trigger workflow builds.
- [object ScmPullRequestResponse](scmpullrequestresponse.md)
  The response body for endpoints that read a single SCM pull request linked to Xcode Cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmpullrequestsresponse)*