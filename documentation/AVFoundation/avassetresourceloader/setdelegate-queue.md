# setDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method

Sets the delegate and dispatch queue to use with the resource loader.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setDelegate(_ delegate: (any AVAssetResourceLoaderDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

#### Discussion

You use this method to specify the object to use when handling resource requests and the dispatch queue on which to process those requests. Resource requests are processed synchronously on the dispatch queue you provide.

## Parameters

- `delegate`: The delegate object to query when handling resource requests. You may specify   if you want to clear the delegate object. The resource loader does not store a strong reference to the delegate object.
- `delegateQueue`: The resource loader maintains a strong reference to the dispatch queue you specify.

## See Also

- [var delegate: (any AVAssetResourceLoaderDelegate)?](avassetresourceloader/delegate.md)
  The delegate object to use when handling resource requests.
- [protocol AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md)
  Methods you can implement to handle resource-loading requests coming from a URL asset.
- [var delegateQueue: dispatch_queue_t?](avassetresourceloader/delegatequeue.md)
  The dispatch queue to use when handling resource requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloader/setdelegate(_:queue:))*