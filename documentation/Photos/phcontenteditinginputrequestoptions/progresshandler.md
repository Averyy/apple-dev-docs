# progressHandler

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A block Photos calls periodically while downloading the asset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var progressHandler: ((Double, UnsafeMutablePointer<ObjCBool>) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^progressHandler)(double progress, BOOL *stop);
```

## Discussion

If you request an asset whose data is not on the local device, and have enabled downloading with the [`isNetworkAccessAllowed`](./isnetworkaccessallowed.md) property, Photos calls your block periodically to report progress and allow canceling the download.

The block takes the following parameters:

- **progress**: A floating-point value indicating the progress of the download. A value of `0.0` indicates the download has just started, and a value of `1.0` indicates the download is complete.
- **stop**: A pointer to a Boolean value. Set `*stop` to `true` inside the block to cancel the download.

## See Also

### Fetching Asset Data from iCloud
- [var isNetworkAccessAllowed: Bool](./isnetworkaccessallowed.md)
  A Boolean value that specifies whether Photos can download the asset from iCloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginputrequestoptions/progresshandler)*