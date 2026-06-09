# AppStoreVersionSubmission

**Framework**: App Store Connect API  
**Kind**: dictionary

A submission of an App Store version to Apple’s review queue, triggering the review process.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppStoreVersionSubmission
```

## Mentions

- [App Store Connect API 1.7 release notes](app-store-connect-api-1-7-release-notes.md)

## Topics

### Objects
- [object AppStoreVersionSubmission.Relationships](appstoreversionsubmission/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppStoreVersionSubmission.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppStoreVersionSubmissionResponse](appstoreversionsubmissionresponse.md)
  The response body for endpoints that submit an App Store version for review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstoreversionsubmission)*