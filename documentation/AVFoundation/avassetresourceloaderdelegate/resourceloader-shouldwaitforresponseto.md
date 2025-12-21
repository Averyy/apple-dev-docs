# resourceLoader(_:shouldWaitForResponseTo:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that assistance is required of the application to respond to an authentication challenge.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForResponseTo authenticationChallenge: URLAuthenticationChallenge) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the resource loader should wait for a response to the authentication challenge; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Delegates receive this message when assistance is required of the application to respond to an authentication challenge.

Return [`true`](https://developer.apple.com/documentation/Swift/true) if you expect a response either subsequently or immediately to the authenticationChallenger object’s sender.

If you intend to respond to the authentication challenge after your handling of `resourceLoader:shouldWaitForResponseToAuthenticationChallenge:` returns, you must retain the authenticationChallenge until after your response has been made.

## Parameters

- `resourceLoader`: The resource loader.
- `authenticationChallenge`: The authentication challenge.

## See Also

- [func resourceLoader(AVAssetResourceLoader, didCancel: URLAuthenticationChallenge)](avassetresourceloaderdelegate/resourceloader(_:didcancel:)-1wqin.md)
  Informs the delegate that a prior authentication challenge has been cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:shouldwaitforresponseto:))*