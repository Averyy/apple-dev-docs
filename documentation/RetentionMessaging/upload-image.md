# Upload Image

**Framework**: Retention Messaging API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Uploads an image to use for retention messaging.

**Availability**:
- Retention Messaging API 1.0+

## Mentions

- [Identifying rate limits](./identifying-rate-limits.md)
- [Retention Messaging API changelog](./retention-messaging-changelog.md)
- [Setting up retention messages](./setting-up-retention-messages.md)

## Discussion

Call this endpoint to upload an image that you can associate with a message or a bullet point within the message. You provide a unique `imageIdentifier` to identify each image you upload.

You can upload image files that meet the following requirements:

- Format: PNG
- Doesn’t have transparency

> **Note**: Ensure the images you upload work equally well with both light and dark modes.

The maximum number of images you can configure for each app is 2000. The endpoint returns a `MaximumNumberOfImagesReachedError` response if an attempt to upload an image exceeds this limit. Call [`Delete Image`](./delete-image.md) to delete images.

Use full-size images for a message, or the smaller bullet point-size images to use as bullet points.

### Upload full-size images

A full-size image is up to 3840 × 2160 pixels, where the width must be 3840 pixels, and the height can be between 160 to 2160 pixels.

You can add alternative text for images when you call [`Upload Message`](./upload-message.md) and associate an image with a message using [`UploadMessageImage`](./uploadmessageimage.md).

### Upload images for bullet points

Images you use for bullet points are 1024 x 1024 pixels. You can add alternative text for the bullet point images when you supply `bulletPoints` in the [`UploadMessageRequestBody`](./uploadmessagerequestbody.md).

> **Note**: This endpoint isn’t idempotent. If you attempt to upload an image and reuse a previously configured `imageIdentifier`, the endpoint returns the [`ImageAlreadyExistsError`](./imagealreadyexistserror.md) response.

### Determine whether an image is ready to display

Immediately after you upload an image, its [`imageState`](./imagestate.md) is `PENDING`. Apple checks the images, and sets the image state to `APPROVED` to indicate the system can display them in retention messaging. Call the [`Get Image List`](./get-image-list.md) endpoint to check the current state of images you upload.

In the sandbox testing environment, the system automatically sets the message and image states to `APPROVED`.

## Endpoint

`PUT https://api.storekit-sandbox.apple.com/inApps/v1/messaging/image/{imageIdentifier}`

## Parameters

### Path Parameters

- `imageIdentifier` (imageIdentifier) *(required)*: A UUID you provide to uniquely identify the image you upload.

### Query Parameters

- `imageSize` (imageSize): The size of the image you upload.

  **Default**: `FULL_SIZE`

## Request Body

**Content-Type**: `image/png`  
**Type**: `binary`

The image file to upload.

## Responses

- `200` OK: Request succeeded.
- `400` Bad Request (`InvalidImageError`, `application/json`): The request is invalid and unacceptable.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](../AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md).
- `403` Forbidden (`MaximumNumberOfMessagesReachedError`, `application/json`): The request is forbidden because the system reached the maximum number of uploaded images.
- `409` Conflict (`ImageAlreadyExistsError`, `application/json`): The image identifier already exists.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits](./identifying-rate-limits.md).
- `500` Internal Server Error (`GeneralInternalError`, `application/json`): Server error. Try again later.

## See Also

### Image configuration
- [Delete Image](./delete-image.md)
  Deletes a previously uploaded image.
- [Get Image List](./get-image-list.md)
  Gets the image identifier and state for all uploaded images.
- [object GetImageListResponse](./getimagelistresponse.md)
  A response that contains status information for all images.
- [object GetImageListResponseItem](./getimagelistresponseitem.md)
  An image identifier and state information for an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/upload-image)*