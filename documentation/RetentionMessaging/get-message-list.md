# Get Message List

**Framework**: Retention Messaging API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Gets the message identifier and state of all uploaded messages.

**Availability**:
- Retention Messaging API 1.0+

## Mentions

- [Identifying rate limits](./identifying-rate-limits.md)
- [Setting up retention messages](./setting-up-retention-messages.md)

#### Discussion

Call this endpoint to get a list of all uploaded message identifiers and check their current state, [`messageState`](./messagestate.md).

> **Note**: If a message includes an image, also check the image state by calling [`Get Image List`](./get-image-list.md). The system displays retention messages with images only if both the message and the image are in an `APPROVED` state.

## Endpoint

`GET https://api.storekit-sandbox.apple.com/inApps/v1/messaging/message/list`

## Responses

- `200` OK (`GetMessageListResponse`, `application/json`): Request succeeded.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits](./identifying-rate-limits.md).
- `500` Internal Server Error (`GeneralInternalError`, `application/json`): Server error. Try again later.

## See Also

### Message configuration
- [Upload Message](./upload-message.md)
  Uploads a message to use for retention messaging.
- [Delete Message](./delete-message.md)
  Deletes a previously uploaded message.
- [object UploadMessageRequestBody](./uploadmessagerequestbody.md)
  The request body for uploading a message, which includes the message text and an optional image reference and bullet points.
- [object UploadMessageImage](./uploadmessageimage.md)
  The definition of an image with its alternative text.
- [object GetMessageListResponse](./getmessagelistresponse.md)
  A response that contains status information for all messages.
- [object GetMessageListResponseItem](./getmessagelistresponseitem.md)
  A message identifier and status information for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/get-message-list)*