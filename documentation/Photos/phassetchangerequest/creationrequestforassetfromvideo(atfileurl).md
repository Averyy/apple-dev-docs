# creationRequestForAssetFromVideo(atFileURL:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Creates a request for adding a new video asset to the Photos library, using the video file at the specified URL.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func creationRequestForAssetFromVideo(atFileURL fileURL: URL) -> Self?
```

```objc
+ (instancetype) creationRequestForAssetFromVideoAtFileURL:(NSURL *) fileURL;
```

#### Return Value

An asset creation request.

#### Discussion

Call this method within a photo library change block to create a new asset. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

To set metadata properties of the newly created asset, use the corresponding properties of the change request (listed in Modifying Assets). To reference the newly created asset later in the same change block or after the change block completes, use the [`placeholderForCreatedAsset`](./placeholderforcreatedasset.md) property to retrieve a placeholder object.

## Parameters

- `fileURL`: A URL for a video file.

## See Also

### Adding New Assets
- [class func creationRequestForAsset(from: UIImage) -> Self](./creationrequestforasset%28from%29.md)
  Creates a request for adding a new image asset to the Photos library.
- [class func creationRequestForAssetFromImage(atFileURL: URL) -> Self?](./creationrequestforassetfromimage%28atfileurl%29.md)
  Creates a request for adding a new image asset to the Photos library, using the image file at the specified URL.
- [var placeholderForCreatedAsset: PHObjectPlaceholder?](./placeholderforcreatedasset.md)
  A placeholder object for the asset that the change request creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetchangerequest/creationrequestforassetfromvideo(atfileurl:))*