# isNetworkAccessAllowed

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether Photos can download the requested image from iCloud.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
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

If `true`, and the requested image is not stored on the local device, Photos downloads the image from iCloud. To be notified of the download’s progress, use the [`progressHandler`](./progresshandler.md) property to provide a block that Photos calls periodically while downloading the image. If `false` (the default), and the image is not on the local device, the [`PHImageResultIsInCloudKey`](../phimageresultisincloudkey.md) value in the result handler’s `info` dictionary indicates that the image is not available unless you enable network access.

## See Also

### Fetching Image Data from iCloud
- [var progressHandler: PHAssetImageProgressHandler?](./progresshandler.md)
  A block that Photos calls periodically while downloading the image.
- [typealias PHAssetImageProgressHandler](../phassetimageprogresshandler.md)
  The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [`progressHandler`](./progresshandler.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptions/isnetworkaccessallowed)*