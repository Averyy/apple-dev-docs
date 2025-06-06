# delegate

**Framework**: AVFoundation  
**Kind**: property

The delegate object to use when handling resource requests.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any AVAssetResourceLoaderDelegate)? { get }
```

#### Discussion

The delegate object is responsible for indicating whether or not it is able to handle a resource request. And for those requests it does handle, the delegate object must initiate the loading of the requested resource.

## See Also

- [func setDelegate((any AVAssetResourceLoaderDelegate)?, queue: dispatch_queue_t?)](avassetresourceloader/setdelegate(_:queue:).md)
  Sets the delegate and dispatch queue to use with the resource loader.
- [protocol AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md)
  Methods you can implement to handle resource-loading requests coming from a URL asset.
- [var delegateQueue: dispatch_queue_t?](avassetresourceloader/delegatequeue.md)
  The dispatch queue to use when handling resource requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/delegate)*