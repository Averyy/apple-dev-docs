# Delete Message

**Framework**: Retention Messaging API  
**Kind**: httpRequest

Delete a previously uploaded message.

**Availability**:
- Retention Messaging API 1.0+

## Mentions

- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

Call this endpoint to delete a message. After successfully deleting the message, its `messageIdentifier` no longer exists.

To avoid errors, don’t use the `messageIdentifier` of deleted messages in [`RealtimeResponseBody`](realtimeresponsebody.md) when your server replies to the `Get Retention Message` endpoint.

> **Note**: This endpoint isn’t idempotent. If the system doesn’t find the message, this endpoint throws an error.

To delete an image associated with a message, call [`Delete Image`](delete-image.md) after you delete the message.

## See Also

- [Upload Message](upload-message.md)
  Upload a message to use for retention messaging.
- [Get Message List](get-message-list.md)
  Get the message identifier and state of all uploaded messages.
- [object UploadMessageRequestBody](uploadmessagerequestbody.md)
  The request body for uploading a message, which includes the message text and an optional image reference.
- [object UploadMessageImage](uploadmessageimage.md)
  The definition of an image with its alternative text.
- [object GetMessageListResponse](getmessagelistresponse.md)
  A response that contains status information for all messages.
- [object GetMessageListResponseItem](getmessagelistresponseitem.md)
  A message identifier and status information for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/delete-message)*