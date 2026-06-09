# AppStoreReviewAttachment

**Framework**: App Store Connect API  
**Kind**: dictionary

A file attached to an App Store review submission to provide reviewers with additional context, such as demo credentials or notes.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppStoreReviewAttachment
```

## Topics

### Objects
- [object AppStoreReviewAttachment.Attributes](appstorereviewattachment/attributes-data.dictionary.md)
  Attributes that describe an App Store Review Attachments resource.
- [object AppStoreReviewAttachment.Relationships](appstorereviewattachment/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppStoreReviewAttachment.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppStoreReviewAttachment.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppStoreReviewAttachmentCreateRequest](appstorereviewattachmentcreaterequest.md)
  The request body you use to create an App Store Review Attachment.
- [object AppStoreReviewAttachmentResponse](appstorereviewattachmentresponse.md)
  The response body for endpoints that create, read, or modify a file attached to an App Store review submission.
- [object AppStoreReviewAttachmentUpdateRequest](appstorereviewattachmentupdaterequest.md)
  The request body you use to update an App Store Review Attachment.
- [object AppStoreReviewAttachmentsResponse](appstorereviewattachmentsresponse.md)
  The response body for endpoints that list files attached to an App Store review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstorereviewattachment)*