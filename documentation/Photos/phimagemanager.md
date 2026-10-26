# PHImageManager

**Framework**: Photos  
**Kind**: class  
**Role**: Class

An object that facilitates retrieving or generating preview thumbnails and asset data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHImageManager
```

```objc
@interface PHImageManager : NSObject
```

## Mentions

- [Displaying Live Photos](../PhotoKit/displaying-live-photos.md)
- [Loading and Caching Assets and Thumbnails](../PhotoKit/loading-and-caching-assets-and-thumbnails.md)

#### Overview

Use these methods to fetch full-size photo assets or thumbnail images, or to retrieve AVFoundation objects for playing, exporting, and manipulating video assets.

To load image or video data:

1. Use the [`PHAsset`](./phasset.md) class to fetch the asset you’re interested in.
2. Call the [`default()`](./phimagemanager/default%28%29.md) method to retrieve the shared image manager object.
3. Use one of the methods listed in the Requesting groups below to load the asset’s image or video data.

The image manager caches the asset images and data it provides, so later requests for the same assets with similar parameters will return results more quickly.

If you need to load image data for many assets together, use the [`PHCachingImageManager`](./phcachingimagemanager.md) class to “preheat” the cache by loading images you expect to need soon. For example, when populating a collection view with photo asset thumbnails, you can cache images ahead of the current scroll position.

## Topics

### Getting the Image Manager
- [class func `default`() -> PHImageManager](./phimagemanager/default%28%29.md)
  Returns the shared image manager object.
### Requesting Images
- [func requestImage(for: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?, resultHandler: (UIImage?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./phimagemanager/requestimage%28for,targetsize,contentmode,options,resulthandler%29.md)
  Requests an image representation for the specified asset.
- [func requestImageDataAndOrientation(for: PHAsset, options: PHImageRequestOptions?, resultHandler: (Data?, String?, CGImagePropertyOrientation, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./phimagemanager/requestimagedataandorientation%28for,options,resulthandler%29.md)
  Requests the largest represented image as data bytes and Exif orientation for the specified asset.
- [let PHImageManagerMaximumSize: CGSize](./phimagemanagermaximumsize.md)
  A special value for requesting original image data or the largest rendered image available. .
- [- requestImageDataForAsset:options:resultHandler:](./phimagemanager/requestimagedataforasset_options_resulthandler_.md)
  Requests full-sized image data for the specified asset.
### Requesting Video Objects
- [func requestPlayerItem(forVideo: PHAsset, options: PHVideoRequestOptions?, resultHandler: (AVPlayerItem?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./phimagemanager/requestplayeritem%28forvideo,options,resulthandler%29.md)
  Requests a representation of the video asset for playback, to be loaded asynchronously.
- [func requestExportSession(forVideo: PHAsset, options: PHVideoRequestOptions?, exportPreset: String, resultHandler: (AVAssetExportSession?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./phimagemanager/requestexportsession%28forvideo,options,exportpreset,resulthandler%29.md)
  Requests an export session for writing the video asset’s data to a file, to be loaded asynchronously.
- [func requestAVAsset(forVideo: PHAsset, options: PHVideoRequestOptions?, resultHandler: (AVAsset?, AVAudioMix?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./phimagemanager/requestavasset%28forvideo,options,resulthandler%29.md)
  Requests AVFoundation objects representing the video asset’s content and state, to be loaded asynchronously.
### Requesting Live Photos
- [func requestLivePhoto(for: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHLivePhotoRequestOptions?, resultHandler: (PHLivePhoto?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID](./phimagemanager/requestlivephoto%28for,targetsize,contentmode,options,resulthandler%29.md)
  Requests a Live Photo representation for the specified asset.
### Canceling a Request
- [func cancelImageRequest(PHImageRequestID)](./phimagemanager/cancelimagerequest%28_%29.md)
  Cancels an asynchronous request
- [typealias PHImageRequestID](./phimagerequestid.md)
  A numeric identifier for an asynchronous image request.
- [var PHInvalidImageRequestID: PHImageRequestID](./phinvalidimagerequestid.md)
  A special value provided for asynchronous image requests that cannot be canceled.
### Constants
- [enum PHImageContentMode](./phimagecontentmode.md)
  Options for fitting an image’s aspect ratio to a requested size, used by the [`requestImage(for:targetSize:contentMode:options:resultHandler:)`](./phimagemanager/requestimage%28for,targetsize,contentmode,options,resulthandler%29.md) method.
- [Image Result Info Keys](../PhotoKit/image-result-info-keys.md)
  Keys identifying information about an image loading result, used in the `resultHandler` block with image request methods.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [PHCachingImageManager](./phcachingimagemanager.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Asset loading
- [Loading and Caching Assets and Thumbnails](../PhotoKit/loading-and-caching-assets-and-thumbnails.md)
  Request image, video, or Live Photos content, and cache for quick reuse.
- [class PHCachingImageManager](./phcachingimagemanager.md)
  An object that facilitates retrieving or generating preview thumbnails, optimized for batch preloading large numbers of assets.
- [class PHImageRequestOptions](./phimagerequestoptions.md)
  A set of options affecting the delivery of still image representations of Photos assets you request from an image manager.
- [class PHVideoRequestOptions](./phvideorequestoptions.md)
  A set of options affecting the delivery of video asset data that you request from an image manager.
- [class PHLivePhotoRequestOptions](./phlivephotorequestoptions.md)
  A set of options affecting the delivery of Live Photo assets you request from an image manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagemanager)*