# PHVideoRequestOptions

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A set of options affecting the delivery of video asset data that you request from an image manager.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHVideoRequestOptions
```

```objc
@interface PHVideoRequestOptions : NSObject
```

## Topics

### Specifying Video Request Options
- [var version: PHVideoRequestOptionsVersion](./phvideorequestoptions/version.md)
  The version of the video to request.
- [enum PHVideoRequestOptionsVersion](./phvideorequestoptionsversion.md)
  Options for requesting a video asset with or without adjustments, used by the [`version`](./phvideorequestoptions/version.md) property.
- [var deliveryMode: PHVideoRequestOptionsDeliveryMode](./phvideorequestoptions/deliverymode.md)
  A mode specifying the requested video quality and delivery priority.
- [enum PHVideoRequestOptionsDeliveryMode](./phvideorequestoptionsdeliverymode.md)
  Options for delivering requested video data, used by the [`deliveryMode`](./phvideorequestoptions/deliverymode.md) property.
### Fetching Video Data from iCloud
- [var isNetworkAccessAllowed: Bool](./phvideorequestoptions/isnetworkaccessallowed.md)
  A Boolean value that specifies whether Photos can download the requested video from iCloud.
- [var progressHandler: PHAssetVideoProgressHandler?](./phvideorequestoptions/progresshandler.md)
  A block Photos calls periodically while downloading the video.
- [typealias PHAssetVideoProgressHandler](./phassetvideoprogresshandler.md)
  The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [`progressHandler`](./phvideorequestoptions/progresshandler.md) property.

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
- [class PHImageRequestOptions](./phimagerequestoptions.md)
  A set of options affecting the delivery of still image representations of Photos assets you request from an image manager.
- [class PHLivePhotoRequestOptions](./phlivephotorequestoptions.md)
  A set of options affecting the delivery of Live Photo assets you request from an image manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phvideorequestoptions)*