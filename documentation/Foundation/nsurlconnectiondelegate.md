# NSURLConnectionDelegate

**Framework**: Foundation  
**Kind**: protocol

A protocol that delegates of a URL connection implement to receive status about and provide feedback to the connection object.

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
protocol NSURLConnectionDelegate : NSObjectProtocol
```

#### Overview

Delegates of [`NSURLConnection`](nsurlconnection.md) objects should implement either the [`NSURLConnectionDataDelegate`](nsurlconnectiondatadelegate.md) or [`NSURLConnectionDownloadDelegate`](nsurlconnectiondownloaddelegate.md) protocol in addition to the [`NSURLConnectionDelegate`](nsurlconnectiondelegate.md) protocol. Specifically:

- If you are using [`NSURLConnection`](nsurlconnection.md) in conjunction with Newsstand Kit’s `download(with:)` method, the delegate class should implement the [`NSURLConnectionDownloadDelegate`](nsurlconnectiondownloaddelegate.md) protocol.
- Otherwise, the delegate class should implement the [`NSURLConnectionDataDelegate`](nsurlconnectiondatadelegate.md) protocol.

Delegates that wish to perform custom authentication handling should implement the [`connection(_:willSendRequestFor:)`](nsurlconnectiondelegate/connection(_:willsendrequestfor:).md) method, which is the preferred mechanism for responding to authentication challenges. (See [`URLAuthenticationChallenge`](urlauthenticationchallenge.md) for more information on authentication challenges.) If [`connection(_:willSendRequestFor:)`](nsurlconnectiondelegate/connection(_:willsendrequestfor:).md) is not implemented, the older, deprecated methods [`connection(_:canAuthenticateAgainstProtectionSpace:)`](nsurlconnectiondelegate/connection(_:canauthenticateagainstprotectionspace:).md), [`connection(_:didReceive:)`](nsurlconnectiondelegate/connection(_:didreceive:).md), and [`connection(_:didCancel:)`](nsurlconnectiondelegate/connection(_:didcancel:).md) are called instead.

The [`connection(_:didFailWithError:)`](nsurlconnectiondelegate/connection(_:didfailwitherror:).md) method is called at most once if an error occurs during the loading of a resource. The [`connectionShouldUseCredentialStorage(_:)`](nsurlconnectiondelegate/connectionshouldusecredentialstorage(_:).md) method is called once, just before the loading of a resource begins.

## Topics

### Connection Authentication
- [func connection(NSURLConnection, willSendRequestFor: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:willsendrequestfor:).md)
  Tells the delegate that the connection will send a request for an authentication challenge.
- [func connection(NSURLConnection, canAuthenticateAgainstProtectionSpace: URLProtectionSpace) -> Bool](nsurlconnectiondelegate/connection(_:canauthenticateagainstprotectionspace:).md)
  Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [func connection(NSURLConnection, didCancel: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:didcancel:).md)
  Sent when a connection cancels an authentication challenge.
- [func connection(NSURLConnection, didReceive: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:didreceive:).md)
  Sent when a connection must authenticate a challenge in order to download its request.
- [func connectionShouldUseCredentialStorage(NSURLConnection) -> Bool](nsurlconnectiondelegate/connectionshouldusecredentialstorage(_:).md)
  Sent to determine whether the URL loader should use the credential storage for authenticating the connection.
### Connection Completion
- [func connection(NSURLConnection, didFailWithError: any Error)](nsurlconnectiondelegate/connection(_:didfailwitherror:).md)
  Sent when a connection fails to load its request successfully.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [NSURLConnectionDataDelegate](nsurlconnectiondatadelegate.md)
- [NSURLConnectionDownloadDelegate](nsurlconnectiondownloaddelegate.md)

## See Also

- [class NSURLConnection](nsurlconnection.md)
  An object that enables you to start and stop URL requests.
- [protocol NSURLConnectionDataDelegate](nsurlconnectiondatadelegate.md)
  A protocol that most delegates of a URL connection implement to receive data associated with the connection.
- [protocol NSURLConnectionDownloadDelegate](nsurlconnectiondownloaddelegate.md)
  A protocol that delegates of a URL connection created with Newsstand Kit implement to receive data associated with a download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate)*