# PHLivePhotoRequestOptions

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A set of options affecting the delivery of Live Photo assets you request from an image manager.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHLivePhotoRequestOptions
```

```objc
@interface PHLivePhotoRequestOptions : NSObject
```

#### Overview

A Live Photo is a picture that includes movement and sound from the moments just before and after its capture.

## Topics

### Specifying Image Request Options
- [var version: PHImageRequestOptionsVersion](./phlivephotorequestoptions/version.md)
  The version of the Live Photo to be requested.
- [var deliveryMode: PHImageRequestOptionsDeliveryMode](./phlivephotorequestoptions/deliverymode.md)
  The requested Live Photo quality and delivery priority.
### Fetching Image Data from iCloud
- [var isNetworkAccessAllowed: Bool](./phlivephotorequestoptions/isnetworkaccessallowed.md)
  A Boolean value that specifies whether Photos can download the requested Live Photo data from iCloud.
- [var progressHandler: PHAssetImageProgressHandler?](./phlivephotorequestoptions/progresshandler.md)
  A block that Photos calls periodically while downloading the Live Photo.
### Instance Properties
- [var preferHDR: Bool](./phlivephotorequestoptions/preferhdr.md)
  Request HDR image data if available (such as PQ/HLG formats).

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
- [class PHVideoRequestOptions](./phvideorequestoptions.md)
  A set of options affecting the delivery of video asset data that you request from an image manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotorequestoptions)*