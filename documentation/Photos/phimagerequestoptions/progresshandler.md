# progressHandler

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A block that Photos calls periodically while downloading the image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var progressHandler: PHAssetImageProgressHandler? { get set }
```

```objc
@property (nonatomic, copy, nullable) PHAssetImageProgressHandler progressHandler;
```

#### Discussion

If you request an image whose data is not on the local device, and you have enabled downloading with the [`isNetworkAccessAllowed`](./isnetworkaccessallowed.md) property, Photos calls your block periodically to report progress and to allow you to cancel the download.

## See Also

### Fetching Image Data from iCloud
- [var isNetworkAccessAllowed: Bool](./isnetworkaccessallowed.md)
  A Boolean value that specifies whether Photos can download the requested image from iCloud.
- [typealias PHAssetImageProgressHandler](../phassetimageprogresshandler.md)
  The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [`progressHandler`](./progresshandler.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptions/progresshandler)*