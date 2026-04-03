# UploadMessageImage

**Framework**: Retention Messaging API  
**Kind**: dictionary

The definition of an image with its alternative text.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object UploadMessageImage
```

## Mentions

- [Setting up retention messages](setting-up-retention-messages.md)

## Properties

- `imageIdentifier` (imageIdentifier) *(required)*: The unique identifier of an image.
- `altText` (altText) *(required)*: The alternative text you provide for the corresponding image.

## See Also

- [Upload Message](upload-message.md)
  Uploads a message to use for retention messaging.
- [Delete Message](delete-message.md)
  Deletes a previously uploaded message.
- [Get Message List](get-message-list.md)
  Gets the message identifier and state of all uploaded messages.
- [object UploadMessageRequestBody](uploadmessagerequestbody.md)
  The request body for uploading a message, which includes the message text and an optional image reference and bullet points.
- [object GetMessageListResponse](getmessagelistresponse.md)
  A response that contains status information for all messages.
- [object GetMessageListResponseItem](getmessagelistresponseitem.md)
  A message identifier and status information for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/uploadmessageimage)*