# AppStoreVersionSubmissionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that submit an App Store version for review.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 1.7

> **Deprecated**: This object is deprecated. Use [`ReviewSubmissionResponse`](./reviewsubmissionresponse.md) instead.

## Declaration

```
object AppStoreVersionSubmissionResponse
```

## Mentions

- [App Store Connect API 1.7 release notes](./app-store-connect-api-1-7-release-notes.md)

## Properties

- `data` (AppStoreVersionSubmission) *(required)* *(deprecated)*
- `links` (DocumentLinks) *(required)*
- `included` ([AppStoreVersion])

## See Also

### Objects
- [object AppStoreVersionSubmission](./appstoreversionsubmission.md)
  A submission of an App Store version to Apple’s review queue, triggering the review process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstoreversionsubmissionresponse)*