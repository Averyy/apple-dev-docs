# PHAssetVideoProgressHandler

**Framework**: Photos  
**Kind**: typealias  
**Role**: Type Alias

The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [`progressHandler`](./phvideorequestoptions/progresshandler.md) property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
typealias PHAssetVideoProgressHandler = (Double, (any Error)?, UnsafeMutablePointer<ObjCBool>, [AnyHashable : Any]?) -> Void
```

```c
typedef void (^)(double, NSError *, _Bool *, NSDictionary *) PHAssetVideoProgressHandler;
```

#### Discussion

If you request a video asset whose data is not on the local device, and you have enabled downloading with the [`isNetworkAccessAllowed`](./phvideorequestoptions/isnetworkaccessallowed.md) property, Photos calls your block periodically to report progress and allow canceling the download.

> **Note**:  Because Photos calls this block in an arbitrary serial queue, it may not execute on the main thread.

The block takes the following parameters:

- **progress**: A floating-point value indicating the progress of the download. A value of `0.0` indicates the download has just started, and a value of `1.0` indicates the download is complete.
- **error**: An `NSError` object describing an error that occurred when attempting to download the video, or `nil` if no errors have occurred.
- **stop**: A pointer to a Boolean value. To cancel the download, set `*stop` to `true` inside the block.
- **info**: A dictionary providing additional information about the status of the video request. See Image Result Info Keys for possible keys and values.

## See Also

### Fetching Video Data from iCloud
- [var isNetworkAccessAllowed: Bool](./phvideorequestoptions/isnetworkaccessallowed.md)
  A Boolean value that specifies whether Photos can download the requested video from iCloud.
- [var progressHandler: PHAssetVideoProgressHandler?](./phvideorequestoptions/progresshandler.md)
  A block Photos calls periodically while downloading the video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetvideoprogresshandler)*