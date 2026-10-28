# creationRequestForAsset(from:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Creates a request for adding a new image asset to the Photos library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
class func creationRequestForAsset(from image: UIImage) -> Self
```

*macOS*

```swift
class func creationRequestForAsset(from image: NSImage) -> Self
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
+ (instancetype) creationRequestForAssetFromImage:(UIImage *) image;
```

*macOS*

```objc
+ (instancetype) creationRequestForAssetFromImage:(NSImage *) image;
```

## Mentions

- [Requesting Changes to the Photo Library](../../PhotoKit/requesting-changes-to-the-photo-library.md)

## Return Value

An asset creation request.

## Discussion

Call this method within a photo library change block to create a new asset. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

To reference the newly created asset later in the same change block or after the change block completes, use the [`placeholderForCreatedAsset`](./placeholderforcreatedasset.md) property to retrieve a placeholder object.

> ❗ **Important**:  A [`UIImage`](../../UIKit/uiimage.md) object does not contain all metadata associated with the image file it was originally loaded from (for example, Exif tags such as geographic location, camera model, and exposure parameters). To ensure such metadata is saved in the Photos library, instead use the [`creationRequestForAssetFromImage(atFileURL:)`](./creationrequestforassetfromimage%28atfileurl%29.md) method or the [`PHAssetCreationRequest`](../phassetcreationrequest.md) class. To copy metadata from one file to another, see [Image I/O](../../ImageIO/ImageIO.md).

## Parameters

- `image`: An image.

## See Also

### Adding New Assets
- [class func creationRequestForAssetFromImage(atFileURL: URL) -> Self?](./creationrequestforassetfromimage%28atfileurl%29.md)
  Creates a request for adding a new image asset to the Photos library, using the image file at the specified URL.
- [class func creationRequestForAssetFromVideo(atFileURL: URL) -> Self?](./creationrequestforassetfromvideo%28atfileurl%29.md)
  Creates a request for adding a new video asset to the Photos library, using the video file at the specified URL.
- [var placeholderForCreatedAsset: PHObjectPlaceholder?](./placeholderforcreatedasset.md)
  A placeholder object for the asset that the change request creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetchangerequest/creationrequestforasset(from:))*