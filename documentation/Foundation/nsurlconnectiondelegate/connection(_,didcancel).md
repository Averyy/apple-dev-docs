# connection(_:didCancel:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent when a connection cancels an authentication challenge.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use -connection:willSendRequestForAuthenticationChallenge: instead.

## Declaration

```swift
optional func connection(_ connection: NSURLConnection, didCancel challenge: URLAuthenticationChallenge)
```

```objc
- (void) connection:(NSURLConnection *) connection didCancelAuthenticationChallenge:(NSURLAuthenticationChallenge *) challenge;
```

## Parameters

- `connection`: The connection sending the message.
- `challenge`: The challenge that was canceled.

## See Also

### Connection Authentication
- [func connection(NSURLConnection, willSendRequestFor: URLAuthenticationChallenge)](./connection%28_,willsendrequestfor%29.md)
  Tells the delegate that the connection will send a request for an authentication challenge.
- [func connection(NSURLConnection, canAuthenticateAgainstProtectionSpace: URLProtectionSpace) -> Bool](./connection%28_,canauthenticateagainstprotectionspace%29.md)
  Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [func connection(NSURLConnection, didReceive: URLAuthenticationChallenge)](./connection%28_,didreceive%29.md)
  Sent when a connection must authenticate a challenge in order to download its request.
- [func connectionShouldUseCredentialStorage(NSURLConnection) -> Bool](./connectionshouldusecredentialstorage%28_%29.md)
  Sent to determine whether the URL loader should use the credential storage for authenticating the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connection(_:didcancel:))*