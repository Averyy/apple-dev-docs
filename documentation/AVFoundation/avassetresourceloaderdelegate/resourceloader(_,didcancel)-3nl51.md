# resourceLoader(_:didCancel:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Informs the delegate that a prior loading request has been cancelled.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancel loadingRequest: AVAssetResourceLoadingRequest)
```

```objc
- (void) resourceLoader:(AVAssetResourceLoader *) resourceLoader didCancelLoadingRequest:(AVAssetResourceLoadingRequest *) loadingRequest;
```

## Discussion

Previously issued loading requests can be cancelled when data from the resource is no longer required or when a loading request is superseded by new requests for data from the same resource.

For example, if to complete a seek operation it becomes necessary to load a range of bytes that’s different from a range previously requested, the prior request may be cancelled while the delegate is still handling it.

## Parameters

- `resourceLoader`: The resource loader.
- `loadingRequest`: The loading request that has been cancelled.

## See Also

### Processing resource requests
- [func resourceLoader(AVAssetResourceLoader, shouldWaitForLoadingOfRequestedResource: AVAssetResourceLoadingRequest) -> Bool](./resourceloader%28_,shouldwaitforloadingofrequestedresource%29.md)
  Asks the delegate if it wants to load the requested resource.
- [func resourceLoader(AVAssetResourceLoader, shouldWaitForRenewalOfRequestedResource: AVAssetResourceRenewalRequest) -> Bool](./resourceloader%28_,shouldwaitforrenewalofrequestedresource%29.md)
  Tells the delegate when assistance is required of the application to renew a resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:didcancel:)-3nl51)*