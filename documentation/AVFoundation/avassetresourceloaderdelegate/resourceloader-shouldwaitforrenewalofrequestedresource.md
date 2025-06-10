# resourceLoader(_:shouldWaitForRenewalOfRequestedResource:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate when assistance is required of the application to renew a resource.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForRenewalOfRequestedResource renewalRequest: AVAssetResourceRenewalRequest) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the delegate can renew the resource; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Delegates receive this message when assistance is required to renew a resource previously loaded by [`resourceLoader(_:shouldWaitForLoadingOfRequestedResource:)`](avassetresourceloaderdelegate/resourceloader(_:shouldwaitforloadingofrequestedresource:).md). For example, this method is invoked to for decryption keys that require renewal, as indicated in a response to a prior invocation of [`resourceLoader(_:shouldWaitForLoadingOfRequestedResource:)`](avassetresourceloaderdelegate/resourceloader(_:shouldwaitforloadingofrequestedresource:).md).

If the result is [`true`](https://developer.apple.com/documentation/swift/true), the resource loader expects invocation, either subsequently or immediately, of either the `AVAssetResourceRenewalRequest` method `finishLoading` or `finishLoadingWithError:`. If you intend to finish loading the resource after your handling of this message returns, you must retain the `renewalRequest` until after loading is finished.

If the result is [`false`](https://developer.apple.com/documentation/swift/false), the resource loader treats the loading of the resource as having failed.

> **Note**:  If the delegate’s implementation of -[`resourceLoader(_:shouldWaitForLoadingOfRequestedResource:)`](avassetresourceloaderdelegate/resourceloader(_:shouldwaitforloadingofrequestedresource:).md) returns [`true`](https://developer.apple.com/documentation/swift/true) without finishing the loading request immediately, it may be invoked again with another loading request before the prior request is finished; therefore in such cases the delegate should be prepared to manage multiple loading requests.

## Parameters

- `resourceLoader`: The resource loader.
- `renewalRequest`: An instance of   that provides information about the requested resource.

## See Also

- [func resourceLoader(AVAssetResourceLoader, shouldWaitForLoadingOfRequestedResource: AVAssetResourceLoadingRequest) -> Bool](avassetresourceloaderdelegate/resourceloader(_:shouldwaitforloadingofrequestedresource:).md)
  Asks the delegate if it wants to load the requested resource.
- [func resourceLoader(AVAssetResourceLoader, didCancel: AVAssetResourceLoadingRequest)](avassetresourceloaderdelegate/resourceloader(_:didcancel:)-3nl51.md)
  Informs the delegate that a prior loading request has been cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:shouldwaitforrenewalofrequestedresource:))*