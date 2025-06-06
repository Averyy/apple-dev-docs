# resourceLoader(_:didCancel:)

**Framework**: AVFoundation  
**Kind**: method

Informs the delegate that a prior authentication challenge has been cancelled.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancel authenticationChallenge: URLAuthenticationChallenge)
```

## Parameters

- `resourceLoader`: The resource loader.
- `authenticationChallenge`: The authentication challenge that has been cancelled.

## See Also

- [func resourceLoader(AVAssetResourceLoader, shouldWaitForResponseTo: URLAuthenticationChallenge) -> Bool](avassetresourceloaderdelegate/resourceloader(_:shouldwaitforresponseto:).md)
  Tells the delegate that assistance is required of the application to respond to an authentication challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:didcancel:)-1wqin)*