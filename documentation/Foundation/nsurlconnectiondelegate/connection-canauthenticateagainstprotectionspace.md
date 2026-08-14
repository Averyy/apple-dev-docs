# connection(_:canAuthenticateAgainstProtectionSpace:)

**Framework**: Foundation  
**Kind**: method

Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func connection(_ connection: NSURLConnection, canAuthenticateAgainstProtectionSpace protectionSpace: URLProtectionSpace) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the delegate if able to respond to a protection space’s form of authentication, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method is called before [`connection(_:didReceive:)`](nsurlconnectiondelegate/connection(_:didreceive:).md), allowing the delegate to inspect a protection space before attempting to authenticate against it. By returning [`true`](https://developer.apple.com/documentation/swift/true), the delegate indicates that it can handle the form of authentication, which it does in the subsequent call to [`connection(_:didReceive:)`](nsurlconnectiondelegate/connection(_:didreceive:).md). If the delegate returns [`false`](https://developer.apple.com/documentation/swift/false), the system attempts to use the user’s keychain to authenticate. If your delegate does not implement this method and the protection space uses client certificate authentication or server trust authentication, the system behaves as if you returned [`false`](https://developer.apple.com/documentation/swift/false). The system behaves as if you returned [`true`](https://developer.apple.com/documentation/swift/true) for all other authentication methods.

> **Note**:  This method is not called if the delegate implements the [`connection(_:willSendRequestFor:)`](nsurlconnectiondelegate/connection(_:willsendrequestfor:).md) method.

## Parameters

- `connection`: The connection sending the message.
- `protectionSpace`: The protection space that generates an authentication challenge.

## See Also

- [func connection(NSURLConnection, willSendRequestFor: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:willsendrequestfor:).md)
  Tells the delegate that the connection will send a request for an authentication challenge.
- [func connection(NSURLConnection, didCancel: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:didcancel:).md)
  Sent when a connection cancels an authentication challenge.
- [func connection(NSURLConnection, didReceive: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:didreceive:).md)
  Sent when a connection must authenticate a challenge in order to download its request.
- [func connectionShouldUseCredentialStorage(NSURLConnection) -> Bool](nsurlconnectiondelegate/connectionshouldusecredentialstorage(_:).md)
  Sent to determine whether the URL loader should use the credential storage for authenticating the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connection(_:canauthenticateagainstprotectionspace:))*