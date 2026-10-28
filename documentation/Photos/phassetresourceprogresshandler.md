# PHAssetResourceProgressHandler

**Framework**: Photos  
**Kind**: typealias  
**Role**: Type Alias

The signature for a block that Photos calls while downloading asset resource data from iCloud. Used by the [`progressHandler`](./phassetresourcerequestoptions/progresshandler.md) property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
typealias PHAssetResourceProgressHandler = (Double) -> Void
```

```c
typedef void (^)(double) PHAssetResourceProgressHandler;
```

## Discussion

If you request an asset resource whose data is not on the local device, and you have enabled downloading with the [`isNetworkAccessAllowed`](./phassetresourcerequestoptions/isnetworkaccessallowed.md) property, Photos calls your block periodically to report progress.

The block takes a single parameter:

- **progress**: A floating-point value indicating the progress of the download. A value of `0.0` indicates that the download has just started, and a value of `1.0` indicates the download is complete.

## See Also

### Fetching Resource Data from iCloud
- [var isNetworkAccessAllowed: Bool](./phassetresourcerequestoptions/isnetworkaccessallowed.md)
  A Boolean value that specifies whether Photos can download the requested asset resource data from iCloud.
- [var progressHandler: PHAssetResourceProgressHandler?](./phassetresourcerequestoptions/progresshandler.md)
  A block that Photos calls periodically while downloading the asset resource data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceprogresshandler)*