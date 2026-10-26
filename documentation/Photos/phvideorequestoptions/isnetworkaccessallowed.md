# isNetworkAccessAllowed

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether Photos can download the requested video from iCloud.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isNetworkAccessAllowed: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isNetworkAccessAllowed) BOOL networkAccessAllowed;
```

#### Discussion

If `true`, and the requested video is not stored on the local device, Photos downloads the video from iCloud. To be notified of the download’s progress, use the [`progressHandler`](./progresshandler.md) property to provide a block that Photos calls periodically while downloading the video. If `false` (the default), and the video is not on the local device, the [`PHImageResultIsInCloudKey`](../phimageresultisincloudkey.md) value in the result handler’s `info` dictionary indicates that the video is not available unless you enable network access.

## See Also

### Fetching Video Data from iCloud
- [var progressHandler: PHAssetVideoProgressHandler?](./progresshandler.md)
  A block Photos calls periodically while downloading the video.
- [typealias PHAssetVideoProgressHandler](../phassetvideoprogresshandler.md)
  The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [`progressHandler`](./progresshandler.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phvideorequestoptions/isnetworkaccessallowed)*