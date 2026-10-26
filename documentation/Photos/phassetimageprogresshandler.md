# PHAssetImageProgressHandler

**Framework**: Photos  
**Kind**: typealias  
**Role**: Type Alias

The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [`progressHandler`](./phimagerequestoptions/progresshandler.md) property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
typealias PHAssetImageProgressHandler = (Double, (any Error)?, UnsafeMutablePointer<ObjCBool>, [AnyHashable : Any]?) -> Void
```

```c
typedef void (^)(double, NSError *, _Bool *, NSDictionary *) PHAssetImageProgressHandler;
```

#### Discussion

If you request an image whose data is not on the local device, and you have enabled downloading with the [`isNetworkAccessAllowed`](./phimagerequestoptions/isnetworkaccessallowed.md) property, Photos calls your block periodically to report progress and to allow you to cancel the download.

> **Note**:  Photos calls this block in an arbitrary serial queue. Dispatch to the main thread if your handler needs to update the user interface.

The block takes the following parameters:

- **progress**: A floating-point value indicating the progress of the download. A value of `0.0` indicates that the download has just started, and a value of `1.0` indicates the download is complete.
- **error**: An `NSError` object describing an error that occurred when attempting to download the image, or `nil` if no errors have occurred.
- **stop**: A pointer to a Boolean value. To cancel the download, set `*stop` to `true` inside the block.
- **info**: A dictionary providing additional information about the status of the image request. See Image Result Info Keys for possible keys and values. For example, a `true` value for the key [`PHImageResultIsDegradedKey`](./phimageresultisdegradedkey.md) indicates that Photos may send the full-quality version of the image later, depending on the value of the image request’s [`deliveryMode`](./phimagerequestoptions/deliverymode.md) property.

## See Also

### Fetching Image Data from iCloud
- [var isNetworkAccessAllowed: Bool](./phimagerequestoptions/isnetworkaccessallowed.md)
  A Boolean value that specifies whether Photos can download the requested image from iCloud.
- [var progressHandler: PHAssetImageProgressHandler?](./phimagerequestoptions/progresshandler.md)
  A block that Photos calls periodically while downloading the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetimageprogresshandler)*