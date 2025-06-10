# connection(_:didCancel:)

**Framework**: Foundation  
**Kind**: method

Sent when a connection cancels an authentication challenge.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func connection(_ connection: NSURLConnection, didCancel challenge: URLAuthenticationChallenge)
```

## Parameters

- `connection`: The connection sending the message.
- `challenge`: The challenge that was canceled.

## See Also

- [func connection(NSURLConnection, willSendRequestFor: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:willsendrequestfor:).md)
  Tells the delegate that the connection will send a request for an authentication challenge.
- [func connection(NSURLConnection, canAuthenticateAgainstProtectionSpace: URLProtectionSpace) -> Bool](nsurlconnectiondelegate/connection(_:canauthenticateagainstprotectionspace:).md)
  Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [func connection(NSURLConnection, didReceive: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:didreceive:).md)
  Sent when a connection must authenticate a challenge in order to download its request.
- [func connectionShouldUseCredentialStorage(NSURLConnection) -> Bool](nsurlconnectiondelegate/connectionshouldusecredentialstorage(_:).md)
  Sent to determine whether the URL loader should use the credential storage for authenticating the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connection(_:didcancel:))*