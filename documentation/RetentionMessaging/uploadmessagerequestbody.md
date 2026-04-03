# UploadMessageRequestBody

**Framework**: Retention Messaging API  
**Kind**: dictionary

The request body for uploading a message, which includes the message text and an optional image reference and bullet points.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object UploadMessageRequestBody
```

## Mentions

- [Retention Messaging API changelog](retention-messaging-changelog.md)

#### Discussion

This is the request body for the [`Upload Message`](upload-message.md) endpoint.

All messages require `body` and `header` text.

Don’t include an `image` or `bulletPoints` when you upload the text for the following retention message types:

- A promotional-offer retention message
- A switch-plan retention message

All default retention messages require body text and header text, and may optionally include an image and bullet points. To place header text above an image, include an image, and set the value of [`headerPosition`](uploadmessagerequestbody/headerposition.md) to `ABOVE_IMAGE`. Otherwise, the header text appears above the message body, which is below the image.

## Properties

- `header` (header) *(required)*: The header text of the retention message that the system displays to customers.
- `body` (body) *(required)*: The body text of the retention message that the system displays to customers.
- `image` (UploadMessageImage): The optional image identifier and its alternative text to appear as part of a text-based message with an image.
- `bulletPoints` ([BulletPoint]): An optional array of bullet points.
- `headerPosition` (headerPosition): The position of header text, which defaults to placing header text above the body.

## See Also

- [Upload Message](upload-message.md)
  Uploads a message to use for retention messaging.
- [Delete Message](delete-message.md)
  Deletes a previously uploaded message.
- [Get Message List](get-message-list.md)
  Gets the message identifier and state of all uploaded messages.
- [object UploadMessageImage](uploadmessageimage.md)
  The definition of an image with its alternative text.
- [object GetMessageListResponse](getmessagelistresponse.md)
  A response that contains status information for all messages.
- [object GetMessageListResponseItem](getmessagelistresponseitem.md)
  A message identifier and status information for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/uploadmessagerequestbody)*