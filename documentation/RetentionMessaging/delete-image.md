# Delete Image

**Framework**: Retention Messaging API  
**Kind**: httpRequest

Delete a previously uploaded image.

**Availability**:
- Retention Messaging API 1.0+

## Mentions

- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

Call this endpoint to delete an image. After successfully deleting the image, its `imageIdentifier` no longer exists. Don’t use the `imageIdentifier` of a deleted image in any new messages.

> **Note**: When you include an image in a message, you need to delete the message before you can delete the image.

This endpoint isn’t idempotent. If the system doesn’t find the image, this endpoint throws an error.

## See Also

- [Upload Image](upload-image.md)
  Upload an image to use for retention messaging.
- [Get Image List](get-image-list.md)
  Get the image identifier and state for all uploaded images.
- [object GetImageListResponse](getimagelistresponse.md)
  A response that contains status information for all images.
- [object GetImageListResponseItem](getimagelistresponseitem.md)
  An image identifier and state information for an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/delete-image)*