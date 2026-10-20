# delegateQueue

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The dispatch queue to use when handling resource requests.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var delegateQueue: dispatch_queue_t? { get }
```

```objc
@property (nonatomic, readonly, nullable) dispatch_queue_t delegateQueue;
```

#### Discussion

Resource requests are processed synchronously on the specified dispatch queue.

## See Also

### Accessing the delegate
- [func setDelegate((any AVAssetResourceLoaderDelegate)?, queue: dispatch_queue_t?)](./setdelegate%28_,queue%29.md)
  Sets the delegate and dispatch queue to use with the resource loader.
- [var delegate: (any AVAssetResourceLoaderDelegate)?](./delegate.md)
  The delegate object to use when handling resource requests.
- [protocol AVAssetResourceLoaderDelegate](../avassetresourceloaderdelegate.md)
  Methods you can implement to handle resource-loading requests coming from a URL asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/delegatequeue)*