# Get Image List

**Framework**: Retention Messaging API  
**Kind**: httpRequest

Get the image identifier and state for all uploaded images.

**Availability**:
- Retention Messaging API 1.0+

## Mentions

- [Identifying rate limits](identifying-rate-limits.md)
- [Setting up retention messages](setting-up-retention-messages.md)

#### Discussion

Call this endpoint to get all uploaded image identifiers and check their current state, [`imageState`](imagestate.md).

Images need to be in an `APPROVED` state before the system can display messages that contain them.

## See Also

- [Upload Image](upload-image.md)
  Upload an image to use for retention messaging.
- [Delete Image](delete-image.md)
  Delete a previously uploaded image.
- [object GetImageListResponse](getimagelistresponse.md)
  A response that contains status information for all images.
- [object GetImageListResponseItem](getimagelistresponseitem.md)
  An image identifier and state information for an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/get-image-list)*