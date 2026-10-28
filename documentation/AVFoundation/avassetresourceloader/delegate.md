# delegate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, weak, readonly, nullable) id<AVAssetResourceLoaderDelegate> delegate;
```

## Discussion

The delegate object is responsible for indicating whether or not it is able to handle a resource request. And for those requests it does handle, the delegate object must initiate the loading of the requested resource.

## See Also

### Accessing the delegate
- [func setDelegate((any AVAssetResourceLoaderDelegate)?, queue: dispatch_queue_t?)](./setdelegate%28_,queue%29.md)
  Sets the delegate and dispatch queue to use with the resource loader.
- [protocol AVAssetResourceLoaderDelegate](../avassetresourceloaderdelegate.md)
  Methods you can implement to handle resource-loading requests coming from a URL asset.
- [var delegateQueue: dispatch_queue_t?](./delegatequeue.md)
  The dispatch queue to use when handling resource requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/delegate)*