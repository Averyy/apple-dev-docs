# Get Message List

**Framework**: Retention Messaging API  
**Kind**: httpRequest

Get the message identifier and state of all uploaded messages.

**Availability**:
- Retention Messaging API 1.0+

## Mentions

- [Identifying rate limits](identifying-rate-limits.md)
- [Setting up retention messages](setting-up-retention-messages.md)

#### Discussion

Call this endpoint to get a list of all uploaded message identifiers and check their current state, [`messageState`](messagestate.md).

> **Note**: If a message includes an image, also check the image state by calling [`Get Image List`](get-image-list.md). The system displays retention messages with images only if both the message and the image are in an `APPROVED` state.

## See Also

- [Upload Message](upload-message.md)
  Upload a message to use for retention messaging.
- [Delete Message](delete-message.md)
  Delete a previously uploaded message.
- [object UploadMessageRequestBody](uploadmessagerequestbody.md)
  The request body for uploading a message, which includes the message text and an optional image reference.
- [object UploadMessageImage](uploadmessageimage.md)
  The definition of an image with its alternative text.
- [object GetMessageListResponse](getmessagelistresponse.md)
  A response that contains status information for all messages.
- [object GetMessageListResponseItem](getmessagelistresponseitem.md)
  A message identifier and status information for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/get-message-list)*