# ScmPullRequestResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read a single SCM pull request linked to Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object ScmPullRequestResponse
```

## Properties

- `data` (ScmPullRequest) *(required)*: The resource data.
- `included` ([ScmRepository]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: The navigational links that include the self-link.

## See Also

- [object ScmPullRequest](scmpullrequest.md)
  A pull request in a source code repository connected to Xcode Cloud, which can automatically trigger workflow builds.
- [object ScmPullRequestsResponse](scmpullrequestsresponse.md)
  The response body for endpoints that list SCM pull requests linked to Xcode Cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmpullrequestresponse)*