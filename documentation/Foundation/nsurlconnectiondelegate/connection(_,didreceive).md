# connection(_:didReceive:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent when a connection must authenticate a challenge in order to download its request.

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
optional func connection(_ connection: NSURLConnection, didReceive challenge: URLAuthenticationChallenge)
```

```objc
- (void) connection:(NSURLConnection *) connection didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *) challenge;
```

## Discussion

This method gives the delegate the opportunity to determine the course of action taken for the challenge: provide credentials, continue without providing credentials, or cancel the authentication challenge and the download.

> **Note**:  This method is not called if the delegate implements the [`connection(_:willSendRequestFor:)`](./connection%28_,willsendrequestfor%29.md) method.

The delegate can determine the number of previous authentication challenges by sending the message [`previousFailureCount`](../urlauthenticationchallenge/previousfailurecount.md) to `challenge`.

If the previous failure count is 0 and the value returned by [`proposedCredential`](../urlauthenticationchallenge/proposedcredential.md) is `nil`, the delegate can create a new NSURLCredential object, providing information specific to the type of credential, and send a [`use(_:for:)`](../urlauthenticationchallengesender/use%28_,for%29.md) message to `[challenge sender]`, passing the credential and `challenge` as parameters. If [`proposedCredential`](../urlauthenticationchallenge/proposedcredential.md) is not `nil`, the value is a credential from the URL or the shared credential storage that can be provided to the user as feedback.

The delegate may decide to abandon further attempts at authentication at any time by sending `[challenge sender]` a [`continueWithoutCredential(for:)`](../urlauthenticationchallengesender/continuewithoutcredential%28for%29.md) or a [`cancel(_:)`](../urlauthenticationchallengesender/cancel%28_%29.md) message. The specific action is implementation dependent.

If the delegate implements this method, the download will suspend until `[challenge sender]` is sent one of the following messages: [`use(_:for:)`](../urlauthenticationchallengesender/use%28_,for%29.md), [`continueWithoutCredential(for:)`](../urlauthenticationchallengesender/continuewithoutcredential%28for%29.md) or [`cancel(_:)`](../urlauthenticationchallengesender/cancel%28_%29.md).

If the delegate does not implement this method the default implementation is used. If a valid credential for the request is provided as part of the URL, or is available from the NSURLCredentialStorage the `[challenge sender]` is sent a [`use(_:for:)`](../urlauthenticationchallengesender/use%28_,for%29.md) with the credential. If the challenge has no credential or the credentials fail to authorize access, then [`continueWithoutCredential(for:)`](../urlauthenticationchallengesender/continuewithoutcredential%28for%29.md) is sent to `[challenge sender]` instead.

## Parameters

- `connection`: The connection sending the message.
- `challenge`: The challenge that `connection` must authenticate in order to download its request.

## See Also

### Related Documentation
- [func use(URLCredential, for: URLAuthenticationChallenge)](../urlauthenticationchallengesender/use%28_,for%29.md)
  Attempt to use a given credential for a given authentication challenge.
- [func continueWithoutCredential(for: URLAuthenticationChallenge)](../urlauthenticationchallengesender/continuewithoutcredential%28for%29.md)
  Attempt to continue downloading a request without providing a credential for a given challenge.
- [func cancel(URLAuthenticationChallenge)](../urlauthenticationchallengesender/cancel%28_%29.md)
  Cancels a given authentication challenge.
### Connection Authentication
- [func connection(NSURLConnection, willSendRequestFor: URLAuthenticationChallenge)](./connection%28_,willsendrequestfor%29.md)
  Tells the delegate that the connection will send a request for an authentication challenge.
- [func connection(NSURLConnection, canAuthenticateAgainstProtectionSpace: URLProtectionSpace) -> Bool](./connection%28_,canauthenticateagainstprotectionspace%29.md)
  Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [func connection(NSURLConnection, didCancel: URLAuthenticationChallenge)](./connection%28_,didcancel%29.md)
  Sent when a connection cancels an authentication challenge.
- [func connectionShouldUseCredentialStorage(NSURLConnection) -> Bool](./connectionshouldusecredentialstorage%28_%29.md)
  Sent to determine whether the URL loader should use the credential storage for authenticating the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connection(_:didreceive:))*