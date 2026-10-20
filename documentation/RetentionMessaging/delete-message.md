# Delete Message

**Framework**: Retention Messaging API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Deletes a previously uploaded message.

**Availability**:
- Retention Messaging API 1.0+

## Mentions

- [Identifying rate limits](./identifying-rate-limits.md)

#### Discussion

Call this endpoint to delete a message. After successfully deleting the message, its `messageIdentifier` no longer exists.

To avoid errors, don’t use the `messageIdentifier` of deleted messages in [`RealtimeResponseBody`](./realtimeresponsebody.md) when your server replies to the `Get Retention Message` endpoint.

> **Note**: This endpoint isn’t idempotent. If the system doesn’t find the message, this endpoint throws an error.

To delete an image associated with a message, call [`Delete Image`](./delete-image.md) after you delete the message.

## Endpoint

`DELETE https://api.storekit-sandbox.apple.com/inApps/v1/messaging/message/{messageIdentifier}`

## Parameters

### Path Parameters

- `messageIdentifier` (messageIdentifier) *(required)*: The identifier of the message to delete.

## Responses

- `200` OK: Request succeeded.
- `400` Bad Request: The request is invalid and unacceptable.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](../AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md).
- `404` Not Found (`MessageNotFoundError`, `application/json`): The system can’t find the message.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits](./identifying-rate-limits.md).
- `500` Internal Server Error (`GeneralInternalError`, `application/json`): Server error. Try again later.

## See Also

### Message configuration
- [Upload Message](./upload-message.md)
  Uploads a message to use for retention messaging.
- [Get Message List](./get-message-list.md)
  Gets the message identifier and state of all uploaded messages.
- [object UploadMessageRequestBody](./uploadmessagerequestbody.md)
  The request body for uploading a message, which includes the message text and an optional image reference and bullet points.
- [object UploadMessageImage](./uploadmessageimage.md)
  The definition of an image with its alternative text.
- [object GetMessageListResponse](./getmessagelistresponse.md)
  A response that contains status information for all messages.
- [object GetMessageListResponseItem](./getmessagelistresponseitem.md)
  A message identifier and status information for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/delete-message)*