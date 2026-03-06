# ScmGitReferenceResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a single Git References resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object ScmGitReferenceResponse
```

## Properties

- `data` (ScmGitReference) *(required)*: The resource data.
- `included` ([ScmRepository]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: The navigational links that include the self-link.

## See Also

- [object ScmGitReference](scmgitreference.md)
  The data structure that represents a Git References resource.
- [object ScmGitReferencesResponse](scmgitreferencesresponse.md)
  A response that contains a list of Git References resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmgitreferenceresponse)*