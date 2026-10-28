# connection(_:canAuthenticateAgainstProtectionSpace:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.6+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use -connection:willSendRequestForAuthenticationChallenge: instead.

## Declaration

```swift
optional func connection(_ connection: NSURLConnection, canAuthenticateAgainstProtectionSpace protectionSpace: URLProtectionSpace) -> Bool
```

```objc
- (BOOL) connection:(NSURLConnection *) connection canAuthenticateAgainstProtectionSpace:(NSURLProtectionSpace *) protectionSpace;
```

## Return Value

[`true`](../../Swift/true.md) if the delegate if able to respond to a protection space’s form of authentication, otherwise [`false`](../../Swift/false.md).

## Discussion

This method is called before [`connection(_:didReceive:)`](./connection%28_,didreceive%29.md), allowing the delegate to inspect a protection space before attempting to authenticate against it. By returning [`true`](../../Swift/true.md), the delegate indicates that it can handle the form of authentication, which it does in the subsequent call to [`connection(_:didReceive:)`](./connection%28_,didreceive%29.md). If the delegate returns [`false`](../../Swift/false.md), the system attempts to use the user’s keychain to authenticate. If your delegate does not implement this method and the protection space uses client certificate authentication or server trust authentication, the system behaves as if you returned [`false`](../../Swift/false.md). The system behaves as if you returned [`true`](../../Swift/true.md) for all other authentication methods.

> **Note**:  This method is not called if the delegate implements the [`connection(_:willSendRequestFor:)`](./connection%28_,willsendrequestfor%29.md) method.

## Parameters

- `connection`: The connection sending the message.
- `protectionSpace`: The protection space that generates an authentication challenge.

## See Also

### Connection Authentication
- [func connection(NSURLConnection, willSendRequestFor: URLAuthenticationChallenge)](./connection%28_,willsendrequestfor%29.md)
  Tells the delegate that the connection will send a request for an authentication challenge.
- [func connection(NSURLConnection, didCancel: URLAuthenticationChallenge)](./connection%28_,didcancel%29.md)
  Sent when a connection cancels an authentication challenge.
- [func connection(NSURLConnection, didReceive: URLAuthenticationChallenge)](./connection%28_,didreceive%29.md)
  Sent when a connection must authenticate a challenge in order to download its request.
- [func connectionShouldUseCredentialStorage(NSURLConnection) -> Bool](./connectionshouldusecredentialstorage%28_%29.md)
  Sent to determine whether the URL loader should use the credential storage for authenticating the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connection(_:canauthenticateagainstprotectionspace:))*