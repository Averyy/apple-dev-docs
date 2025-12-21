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

## See Also

- [Upload Message](upload-message.md)
  Upload a message to use for retention messaging.
- [Delete Message](delete-message.md)
  Delete a previously uploaded message.
- [Get Message List](get-message-list.md)
  Get the message identifier and state of all uploaded messages.
- [object UploadMessageRequestBody](uploadmessagerequestbody.md)
  The request body for uploading a message, which includes the message text and an optional image reference.
- [object UploadMessageImage](uploadmessageimage.md)
  The definition of an image with its alternative text.
- [object GetMessageListResponseItem](getmessagelistresponseitem.md)
  A message identifier and status information for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/getmessagelistresponse)*