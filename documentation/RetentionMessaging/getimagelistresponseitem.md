# GetImageListResponseItem

**Framework**: Retention Messaging API  
**Kind**: dictionary

An image identifier and state information for an image.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object GetImageListResponseItem
```

## Mentions

- [Retention Messaging API changelog](retention-messaging-changelog.md)

#### Discussion

The [`Get Image List`](get-image-list.md) endpoint returns an array of these values in its response.

## Properties

- `imageIdentifier` (imageIdentifier): The identifier of the image.
- `imageSize` (imageSize): The size of the image.
- `imageState` (imageState): The current state of the image.

## See Also

- [Upload Image](upload-image.md)
  Uploads an image to use for retention messaging.
- [Delete Image](delete-image.md)
  Deletes a previously uploaded image.
- [Get Image List](get-image-list.md)
  Gets the image identifier and state for all uploaded images.
- [object GetImageListResponse](getimagelistresponse.md)
  A response that contains status information for all images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/getimagelistresponseitem)*