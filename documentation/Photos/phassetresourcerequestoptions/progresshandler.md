# progressHandler

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A block that Photos calls periodically while downloading the asset resource data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var progressHandler: PHAssetResourceProgressHandler? { get set }
```

```objc
@property (nonatomic, copy, nullable) PHAssetResourceProgressHandler progressHandler;
```

## Discussion

If you request an asset resource whose data is not on the local device, and you have enabled downloading with the [`isNetworkAccessAllowed`](./isnetworkaccessallowed.md) property, Photos calls your block periodically to report progress.

## See Also

### Fetching Resource Data from iCloud
- [var isNetworkAccessAllowed: Bool](./isnetworkaccessallowed.md)
  A Boolean value that specifies whether Photos can download the requested asset resource data from iCloud.
- [typealias PHAssetResourceProgressHandler](../phassetresourceprogresshandler.md)
  The signature for a block that Photos calls while downloading asset resource data from iCloud. Used by the [`progressHandler`](./progresshandler.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcerequestoptions/progresshandler)*