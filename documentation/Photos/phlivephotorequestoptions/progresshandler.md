# progressHandler

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A block that Photos calls periodically while downloading the Live Photo.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.15+
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

If you request a Live Photo whose data is not on the local device, and you have enabled downloading with the [`PHLivePhotoRequestOptions`](../phlivephotorequestoptions.md) property, Photos calls your block periodically to report progress and to allow you to cancel the download.

## See Also

### Fetching Image Data from iCloud
- [var isNetworkAccessAllowed: Bool](./isnetworkaccessallowed.md)
  A Boolean value that specifies whether Photos can download the requested Live Photo data from iCloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotorequestoptions/progresshandler)*