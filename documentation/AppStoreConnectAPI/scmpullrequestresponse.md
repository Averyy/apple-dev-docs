# ScmPullRequestResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a single Pull Requests resource.

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
  The data structure that represents a Pull Requests resource.
- [object ScmPullRequestsResponse](scmpullrequestsresponse.md)
  A response that contains a list of Pull Requests resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmpullrequestresponse)*