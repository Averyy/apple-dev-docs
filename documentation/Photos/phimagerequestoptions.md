# PHImageRequestOptions

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A set of options affecting the delivery of still image representations of Photos assets you request from an image manager.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHImageRequestOptions
```

```objc
@interface PHImageRequestOptions : NSObject
```

## Topics

### Scheduling an Image Request
- [var isSynchronous: Bool](./phimagerequestoptions/issynchronous.md)
  A Boolean value that determines whether Photos processes the image request synchronously.
### Specifying Image Request Options
- [var version: PHImageRequestOptionsVersion](./phimagerequestoptions/version.md)
  The version of the image to be requested.
- [enum PHImageRequestOptionsVersion](./phimagerequestoptionsversion.md)
  Options for requesting an image asset with or without adjustments, used by the [`version`](./phimagerequestoptions/version.md) property.
- [var deliveryMode: PHImageRequestOptionsDeliveryMode](./phimagerequestoptions/deliverymode.md)
  The requested image quality and delivery priority.
- [enum PHImageRequestOptionsDeliveryMode](./phimagerequestoptionsdeliverymode.md)
  Options for delivering requested image data, used by the [`deliveryMode`](./phimagerequestoptions/deliverymode.md) property.
- [var resizeMode: PHImageRequestOptionsResizeMode](./phimagerequestoptions/resizemode.md)
  A mode that specifies how to resize the requested image.
- [enum PHImageRequestOptionsResizeMode](./phimagerequestoptionsresizemode.md)
  Options for how to resize the requested image to fit a target size, used by the [`resizeMode`](./phimagerequestoptions/resizemode.md) property.
- [var normalizedCropRect: CGRect](./phimagerequestoptions/normalizedcroprect.md)
  A rectangle for requesting a cropped version of the original image.
### Fetching Image Data from iCloud
- [var isNetworkAccessAllowed: Bool](./phimagerequestoptions/isnetworkaccessallowed.md)
  A Boolean value that specifies whether Photos can download the requested image from iCloud.
- [var progressHandler: PHAssetImageProgressHandler?](./phimagerequestoptions/progresshandler.md)
  A block that Photos calls periodically while downloading the image.
- [typealias PHAssetImageProgressHandler](./phassetimageprogresshandler.md)
  The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [`progressHandler`](./phimagerequestoptions/progresshandler.md) property.
### Instance Properties
- [var allowSecondaryDegradedImage: Bool](./phimagerequestoptions/allowsecondarydegradedimage.md)
- [var preferHDR: Bool](./phimagerequestoptions/preferhdr.md)
  Request HDR image data if available (such as PQ/HLG formats).
- [var targetHDRHeadroom: CGFloat](./phimagerequestoptions/targethdrheadroom.md)
  Target HDR headroom for image rendering.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Asset loading
- [Loading and Caching Assets and Thumbnails](../PhotoKit/loading-and-caching-assets-and-thumbnails.md)
  Request image, video, or Live Photos content, and cache for quick reuse.
- [class PHImageManager](./phimagemanager.md)
  An object that facilitates retrieving or generating preview thumbnails and asset data.
- [class PHCachingImageManager](./phcachingimagemanager.md)
  An object that facilitates retrieving or generating preview thumbnails, optimized for batch preloading large numbers of assets.
- [class PHVideoRequestOptions](./phvideorequestoptions.md)
  A set of options affecting the delivery of video asset data that you request from an image manager.
- [class PHLivePhotoRequestOptions](./phlivephotorequestoptions.md)
  A set of options affecting the delivery of Live Photo assets you request from an image manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptions)*