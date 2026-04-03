# GetMessageListResponse

**Framework**: Retention Messaging API  
**Kind**: dictionary

A response that contains status information for all messages.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object GetMessageListResponse
```

#### Discussion

The [`Get Message List`](get-message-list.md) endpoint returns this response.

## Properties

- `messageIdentifiers` ([GetMessageListResponseItem]): An array of all message identifiers and their message states.

## See Also

- [Upload Message](upload-message.md)
  Uploads a message to use for retention messaging.
- [Delete Message](delete-message.md)
  Deletes a previously uploaded message.
- [Get Message List](get-message-list.md)
  Gets the message identifier and state of all uploaded messages.
- [object UploadMessageRequestBody](uploadmessagerequestbody.md)
  The request body for uploading a message, which includes the message text and an optional image reference and bullet points.
- [object UploadMessageImage](uploadmessageimage.md)
  The definition of an image with its alternative text.
- [object GetMessageListResponseItem](getmessagelistresponseitem.md)
  A message identifier and status information for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/getmessagelistresponse)*