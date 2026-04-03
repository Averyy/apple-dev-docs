# GetImageListResponse

**Framework**: Retention Messaging API  
**Kind**: dictionary

A response that contains status information for all images.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object GetImageListResponse
```

#### Discussion

The [`Get Image List`](get-image-list.md) endpoint returns this response.

## Properties

- `imageIdentifiers` ([GetImageListResponseItem]): An array of all image identifiers and their image state.

## See Also

- [Upload Image](upload-image.md)
  Uploads an image to use for retention messaging.
- [Delete Image](delete-image.md)
  Deletes a previously uploaded image.
- [Get Image List](get-image-list.md)
  Gets the image identifier and state for all uploaded images.
- [object GetImageListResponseItem](getimagelistresponseitem.md)
  An image identifier and state information for an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/getimagelistresponse)*