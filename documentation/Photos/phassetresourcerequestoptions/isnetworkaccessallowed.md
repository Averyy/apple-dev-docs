# isNetworkAccessAllowed

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether Photos can download the requested asset resource data from iCloud.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
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

If `true`, and the requested resource data is not stored on the local device, Photos downloads that data from iCloud. To be notified of the download’s progress, use the [`progressHandler`](./progresshandler.md) property to provide a block that Photos calls periodically while downloading the resource data. If `false` (the default), and the resource data is not on the local device, Photos calls the `completionHandler` block you provided in your request, with an `NSError` object indicating that the resource requires network access.

## See Also

### Fetching Resource Data from iCloud
- [var progressHandler: PHAssetResourceProgressHandler?](./progresshandler.md)
  A block that Photos calls periodically while downloading the asset resource data.
- [typealias PHAssetResourceProgressHandler](../phassetresourceprogresshandler.md)
  The signature for a block that Photos calls while downloading asset resource data from iCloud. Used by the [`progressHandler`](./progresshandler.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcerequestoptions/isnetworkaccessallowed)*