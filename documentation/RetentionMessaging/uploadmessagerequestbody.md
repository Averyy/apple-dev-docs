# UploadMessageRequestBody

**Framework**: Retention Messaging API  
**Kind**: dictionary

The request body for uploading a message, which includes the message text and an optional image reference.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object UploadMessageRequestBody
```

#### Discussion

This is the request body for the [`Upload Message`](upload-message.md) endpoint.

Include an `image`, as well as the `header` and `body`, to upload a text-based message with an image.

Don’t include an `image` when you upload the text for the following retention message types:

- A text-based retention message
- A promotional-offer retention message
- A switch-plan retention message

## See Also

- [Upload Message](upload-message.md)
  Upload a message to use for retention messaging.
- [Delete Message](delete-message.md)
  Delete a previously uploaded message.
- [Get Message List](get-message-list.md)
  Get the message identifier and state of all uploaded messages.
- [object UploadMessageImage](uploadmessageimage.md)
  The definition of an image with its alternative text.
- [object GetMessageListResponse](getmessagelistresponse.md)
  A response that contains status information for all messages.
- [object GetMessageListResponseItem](getmessagelistresponseitem.md)
  A message identifier and status information for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/uploadmessagerequestbody)*