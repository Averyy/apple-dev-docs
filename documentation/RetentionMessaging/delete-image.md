# Delete Image

**Framework**: Retention Messaging API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Deletes a previously uploaded image.

**Availability**:
- Retention Messaging API 1.0+

## Mentions

- [Identifying rate limits](./identifying-rate-limits.md)

#### Discussion

Call this endpoint to delete an image. After successfully deleting the image, its `imageIdentifier` no longer exists. Don’t use the `imageIdentifier` of a deleted image in any new messages.

> **Note**: When you include an image in a message, you need to delete the message before you can delete the image.

This endpoint isn’t idempotent. If the system doesn’t find the image, this endpoint throws an error.

## Endpoint

`DELETE https://api.storekit-sandbox.apple.com/inApps/v1/messaging/image/{imageIdentifier}`

## Parameters

### Path Parameters

- `imageIdentifier` (imageIdentifier) *(required)*: The identifier of the image to delete.

## Responses

- `200` OK: Request succeeded.
- `400` Bad Request: The request is invalid and unacceptable.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](../AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md)..
- `403` Forbidden (`ImageInUseError`, `application/json`): The request is forbidden because the image is in use.
- `404` Not Found (`ImageNotFoundError`, `application/json`): The system can’t find the image.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits](./identifying-rate-limits.md).
- `500` Internal Server Error (`GeneralInternalError`, `application/json`): Server error. Try again later.

## See Also

### Image configuration
- [Upload Image](./upload-image.md)
  Uploads an image to use for retention messaging.
- [Get Image List](./get-image-list.md)
  Gets the image identifier and state for all uploaded images.
- [object GetImageListResponse](./getimagelistresponse.md)
  A response that contains status information for all images.
- [object GetImageListResponseItem](./getimagelistresponseitem.md)
  An image identifier and state information for an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/delete-image)*