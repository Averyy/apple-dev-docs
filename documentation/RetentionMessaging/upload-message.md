# Upload Message

**Framework**: Retention Messaging API  
**Kind**: httpRequest

Upload a message to use for retention messaging.

**Availability**:
- Retention Messaging API 1.0+

## Mentions

- [Setting up retention messages](setting-up-retention-messages.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

Call this endpoint to upload the text for retention messages. You provide a unique `messageIdentifier` to identify each message you upload. You can optionally include a reference to an image and its alternative text.

A message consists of four string fields:

- The header, which contains text to display above the body.
- The body, which contains the main text of the message.
- An optional [`imageIdentifier`](imageidentifier.md) that represents an image you upload. Note: This option is only for text-based messages with images.
- Alternative text for the optional image.

> ❗ **Important**: Only text-based retention messages can include images. If you’re uploading text for a promotional-offer message or a switch-plan message, don’t include an image.

Each string needs to be a UTF-8-encoded value with a maximum length as indicated below:

| Field | Maximum length | Related error code |
| --- | --- | --- |
| [`header`](header.md) | 66 | [`HeaderTooLongError`](headertoolongerror.md) |
| [`body`](body.md) | 144 | [`BodyTooLongError`](bodytoolongerror.md) |
| [`altText`](alttext.md) | 150 | [`AltTextTooLongError`](alttexttoolongerror.md) |

The maximum number of messages you can configure for each app is 2000. For example, you may choose to upload a message for a product identifier for each locale your app supports. The endpoint returns a `MaximumNumberOfMessagesReachedError` response if you exceed the maximum limit. Call [`Delete Message`](delete-message.md) to delete messages.

> 💡 **Tip**: Keep a record of the message and image contents on your system.

This endpoint isn’t idempotent. If you have a previously configured message with the same `messageIdentifier`, the endpoint returns [`MessageAlreadyExistsError`](messagealreadyexistserror.md).

##### Determine Whether a Message Is Ready to Display

Immediately after you upload an message, its [`messageState`](messagestate.md) is `PENDING`. Apple checks the message, and sets the message state to `APPROVED` to indicate the system can display it in retention messaging. Call the [`Get Message List`](get-message-list.md) endpoint to check the current state of all messages. If a message includes an image, call [`Get Image List`](get-image-list.md) to check the current state of the image separately. Both the message and its image, if any, need to be in an `APPROVED` state before the system can display a message.

In the sandbox testing environment, the system automatically sets message and image states to `APPROVED`.

## Request Body

The message text to upload.

## See Also

- [Delete Message](delete-message.md)
  Delete a previously uploaded message.
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

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/upload-message)*