# placeholderForCreatedAsset

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A placeholder object for the asset that the change request creates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var placeholderForCreatedAsset: PHObjectPlaceholder? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) PHObjectPlaceholder * placeholderForCreatedAsset;
```

#### Discussion

Use this property if you need to reference the asset created by a change request within the same change block. For example, the following code, when included in a photo library change block, creates an asset and then adds it to a collection.

**Swift**:

```swift
let createAssetRequest = PHAssetChangeRequest.creationRequestForAsset(from: image)
let assetPlaceholder = createAssetRequest.placeholderForCreatedAsset!
let albumChangeRequest = PHAssetCollectionChangeRequest(for: album)
albumChangeRequest!.addAssets([assetPlaceholder] as NSFastEnumeration)
```

**Objective-C**:

```objc
PHAssetChangeRequest *createAssetRequest = [PHAssetChangeRequest creationRequestForAssetFromImage:image];
PHObjectPlaceholder *assetPlaceholder = createAssetRequest.placeholderForCreatedAsset;
PHAssetCollectionChangeRequest *albumChangeRequest =
    [PHAssetCollectionChangeRequest changeRequestForAssetCollection:album];
[albumChangeRequest addAssets:@[ assetPlaceholder ]];
```

For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

## See Also

### Adding New Assets
- [class func creationRequestForAsset(from: UIImage) -> Self](./creationrequestforasset%28from%29.md)
  Creates a request for adding a new image asset to the Photos library.
- [class func creationRequestForAssetFromImage(atFileURL: URL) -> Self?](./creationrequestforassetfromimage%28atfileurl%29.md)
  Creates a request for adding a new image asset to the Photos library, using the image file at the specified URL.
- [class func creationRequestForAssetFromVideo(atFileURL: URL) -> Self?](./creationrequestforassetfromvideo%28atfileurl%29.md)
  Creates a request for adding a new video asset to the Photos library, using the video file at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetchangerequest/placeholderforcreatedasset)*