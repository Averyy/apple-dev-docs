# connectionShouldUseCredentialStorage(_:)

**Framework**: Foundation  
**Kind**: method

Sent to determine whether the URL loader should use the credential storage for authenticating the connection.

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
optional func connectionShouldUseCredentialStorage(_ connection: NSURLConnection) -> Bool
```

#### Discussion

This method is called before any attempt to authenticate is made.

If you return [`false`](https://developer.apple.com/documentation/swift/false), the connection does not consult the credential storage automatically, and does not store credentials. However, in your connection:didReceiveAuthenticationChallenge: method, you can consult the credential storage yourself and store credentials yourself, as needed.

Not implementing this method is the same as returning [`true`](https://developer.apple.com/documentation/swift/true).

> ❗ **Important**:  Prior to iOS 7 and OS X v10.9, the `connectionShouldUseCredentialStorage:` method is never called on delegates that implement the [`connection(_:willSendRequestFor:)`](nsurlconnectiondelegate/connection(_:willsendrequestfor:).md) method. In later operating systems, if the delegate implements the [`connection(_:willSendRequestFor:)`](nsurlconnectiondelegate/connection(_:willsendrequestfor:).md) method, the `connectionShouldUseCredentialStorage:` method is called  if the app’s deployment target is at least iOS 7 or OS X v10.9.

## Parameters

- `connection`: The connection sending the message.

## See Also

- [func connection(NSURLConnection, willSendRequestFor: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:willsendrequestfor:).md)
  Tells the delegate that the connection will send a request for an authentication challenge.
- [func connection(NSURLConnection, canAuthenticateAgainstProtectionSpace: URLProtectionSpace) -> Bool](nsurlconnectiondelegate/connection(_:canauthenticateagainstprotectionspace:).md)
  Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [func connection(NSURLConnection, didCancel: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:didcancel:).md)
  Sent when a connection cancels an authentication challenge.
- [func connection(NSURLConnection, didReceive: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:didreceive:).md)
  Sent when a connection must authenticate a challenge in order to download its request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connectionshouldusecredentialstorage(_:))*