# AppStoreReviewAttachmentResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify a file attached to an App Store review submission.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppStoreReviewAttachmentResponse
```

## Properties

- `data` (AppStoreReviewAttachment) *(required)*
- `links` (DocumentLinks) *(required)*
- `included` ([AppStoreReviewDetail])

## See Also

- [object AppStoreReviewAttachment](appstorereviewattachment.md)
  A file attached to an App Store review submission to provide reviewers with additional context, such as demo credentials or notes.
- [object AppStoreReviewAttachmentCreateRequest](appstorereviewattachmentcreaterequest.md)
  The request body you use to create an App Store Review Attachment.
- [object AppStoreReviewAttachmentUpdateRequest](appstorereviewattachmentupdaterequest.md)
  The request body you use to update an App Store Review Attachment.
- [object AppStoreReviewAttachmentsResponse](appstorereviewattachmentsresponse.md)
  The response body for endpoints that list files attached to an App Store review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstorereviewattachmentresponse)*