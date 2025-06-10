# connection(_:didReceive:)

**Framework**: Foundation  
**Kind**: method

Sent when a connection must authenticate a challenge in order to download its request.

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
optional func connection(_ connection: NSURLConnection, didReceive challenge: URLAuthenticationChallenge)
```

#### Discussion

This method gives the delegate the opportunity to determine the course of action taken for the challenge: provide credentials, continue without providing credentials, or cancel the authentication challenge and the download.

> **Note**:  This method is not called if the delegate implements the [`connection(_:willSendRequestFor:)`](nsurlconnectiondelegate/connection(_:willsendrequestfor:).md) method.

The delegate can determine the number of previous authentication challenges by sending the message [`previousFailureCount`](urlauthenticationchallenge/previousfailurecount.md) to `challenge`.

If the previous failure count is 0 and the value returned by [`proposedCredential`](urlauthenticationchallenge/proposedcredential.md) is `nil`, the delegate can create a new NSURLCredential object, providing information specific to the type of credential, and send a [`use(_:for:)`](urlauthenticationchallengesender/use(_:for:).md) message to `[challenge sender]`, passing the credential and `challenge` as parameters. If [`proposedCredential`](urlauthenticationchallenge/proposedcredential.md) is not `nil`, the value is a credential from the URL or the shared credential storage that can be provided to the user as feedback.

The delegate may decide to abandon further attempts at authentication at any time by sending `[challenge sender]` a [`continueWithoutCredential(for:)`](urlauthenticationchallengesender/continuewithoutcredential(for:).md) or a [`cancel(_:)`](urlauthenticationchallengesender/cancel(_:).md) message. The specific action is implementation dependent.

If the delegate implements this method, the download will suspend until `[challenge sender]` is sent one of the following messages: [`use(_:for:)`](urlauthenticationchallengesender/use(_:for:).md), [`continueWithoutCredential(for:)`](urlauthenticationchallengesender/continuewithoutcredential(for:).md) or [`cancel(_:)`](urlauthenticationchallengesender/cancel(_:).md).

If the delegate does not implement this method the default implementation is used. If a valid credential for the request is provided as part of the URL, or is available from the NSURLCredentialStorage the `[challenge sender]` is sent a [`use(_:for:)`](urlauthenticationchallengesender/use(_:for:).md) with the credential. If the challenge has no credential or the credentials fail to authorize access, then [`continueWithoutCredential(for:)`](urlauthenticationchallengesender/continuewithoutcredential(for:).md) is sent to `[challenge sender]` instead.

## Parameters

- `connection`: The connection sending the message.
- `challenge`: The challenge that   must authenticate in order to download its request.

## See Also

- [func use(URLCredential, for: URLAuthenticationChallenge)](urlauthenticationchallengesender/use(_:for:).md)
  Attempt to use a given credential for a given authentication challenge.
- [func continueWithoutCredential(for: URLAuthenticationChallenge)](urlauthenticationchallengesender/continuewithoutcredential(for:).md)
  Attempt to continue downloading a request without providing a credential for a given challenge.
- [func cancel(URLAuthenticationChallenge)](urlauthenticationchallengesender/cancel(_:).md)
  Cancels a given authentication challenge.
- [func connection(NSURLConnection, willSendRequestFor: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:willsendrequestfor:).md)
  Tells the delegate that the connection will send a request for an authentication challenge.
- [func connection(NSURLConnection, canAuthenticateAgainstProtectionSpace: URLProtectionSpace) -> Bool](nsurlconnectiondelegate/connection(_:canauthenticateagainstprotectionspace:).md)
  Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [func connection(NSURLConnection, didCancel: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:didcancel:).md)
  Sent when a connection cancels an authentication challenge.
- [func connectionShouldUseCredentialStorage(NSURLConnection) -> Bool](nsurlconnectiondelegate/connectionshouldusecredentialstorage(_:).md)
  Sent to determine whether the URL loader should use the credential storage for authenticating the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connection(_:didreceive:))*