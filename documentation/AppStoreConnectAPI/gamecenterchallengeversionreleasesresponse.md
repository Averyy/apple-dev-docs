# GameCenterChallengeVersionReleasesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a list of challenge resources.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object GameCenterChallengeVersionReleasesResponse
```

## Properties

- `data` ([GameCenterChallengeVersionRelease]) *(required)*
- `included` ([GameCenterChallengeVersion])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object GameCenterChallengeVersionRelease](gamecenterchallengeversionrelease.md)
  The data structure that represent a challenge version release.
- [object GameCenterChallengeVersionReleaseCreateRequest](gamecenterchallengeversionreleasecreaterequest.md)
  The request body you use to create a challenge resource.
- [object GameCenterChallengeVersionReleaseResponse](gamecenterchallengeversionreleaseresponse.md)
  A response that contains a single challenge resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecenterchallengeversionreleasesresponse)*