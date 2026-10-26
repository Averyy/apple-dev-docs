# isNetworkAccessAllowed

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether Photos can download the requested Live Photo data from iCloud.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
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

If `true`, and the requested Live Photo data is not stored on the local device, Photos downloads that data from iCloud. To be notified of the download’s progress, use the [`progressHandler`](./progresshandler.md) property to provide a block that Photos calls periodically while downloading. If `false` (the default), and the Live Photo data is not on the local device, the [`PHImageResultIsInCloudKey`](../phimageresultisincloudkey.md) value in the result handler’s `info` dictionary indicates that the data is not available unless you enable network access.

## See Also

### Fetching Image Data from iCloud
- [var progressHandler: PHAssetImageProgressHandler?](./progresshandler.md)
  A block that Photos calls periodically while downloading the Live Photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotorequestoptions/isnetworkaccessallowed)*