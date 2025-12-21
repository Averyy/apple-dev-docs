# Upload Image

**Framework**: Retention Messaging API  
**Kind**: httpRequest

Upload an image to use for retention messaging.

**Availability**:
- Retention Messaging API 1.0+

## Mentions

- [Identifying rate limits](identifying-rate-limits.md)
- [Setting up retention messages](setting-up-retention-messages.md)

#### Discussion

Call this endpoint to upload an image that you can associate with a message. You provide a unique `imageIdentifier` to identify each image you upload.

You can upload image files that meet the following requirements:

- Format: PNG
- Size: 3840 × 2160 pixels
- Doesn’t have transparency

You can add alternative text for images when you call [`Upload Message`](upload-message.md) and associate an image with a message.

The maximum number of images you can configure for each app is 2000. The endpoint returns a `MaximumNumberOfImagesReachedError` response if an attempt to upload an image exceeds this limit. Call [`Delete Image`](delete-image.md) to delete images.

> **Note**: This endpoint isn’t idempotent. If you have a previously configured image with the same `imageIdentifier`, the endpoint returns the [`ImageAlreadyExistsError`](imagealreadyexistserror.md) response.

##### Determine Whether an Image Is Ready to Display

Immediately after you upload an image, its [`imageState`](imagestate.md) is `PENDING`. Apple checks the images, and sets the image state to `APPROVED` to indicate the system can display them in retention messaging. Call the [`Get Image List`](get-image-list.md) endpoint to check the current state of images you upload.

In the sandbox testing environment, the system automatically sets the message and image states to `APPROVED`.

## Request Body

The image file to upload.

## See Also

- [Delete Image](delete-image.md)
  Delete a previously uploaded image.
- [Get Image List](get-image-list.md)
  Get the image identifier and state for all uploaded images.
- [object GetImageListResponse](getimagelistresponse.md)
  A response that contains status information for all images.
- [object GetImageListResponseItem](getimagelistresponseitem.md)
  An image identifier and state information for an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/upload-image)*