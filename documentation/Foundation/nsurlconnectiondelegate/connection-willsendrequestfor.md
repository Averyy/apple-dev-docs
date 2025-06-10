# connection(_:willSendRequestFor:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the connection will send a request for an authentication challenge.

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
optional func connection(_ connection: NSURLConnection, willSendRequestFor challenge: URLAuthenticationChallenge)
```

#### Discussion

This method allows the delegate to make an informed decision about connection authentication at once. If the delegate implements this method, it has no need to implement [`connection(_:canAuthenticateAgainstProtectionSpace:)`](nsurlconnectiondelegate/connection(_:canauthenticateagainstprotectionspace:).md) or [`connection(_:didReceive:)`](nsurlconnectiondelegate/connection(_:didreceive:).md). In fact, those other methods are not invoked (except on older operating systems, where applicable).

In this method,you  invoke one of the challenge-responder methods ([`URLAuthenticationChallengeSender`](urlauthenticationchallengesender.md) protocol):

- [`use(_:for:)`](urlauthenticationchallengesender/use(_:for:).md)
- [`continueWithoutCredential(for:)`](urlauthenticationchallengesender/continuewithoutcredential(for:).md)
- [`cancel(_:)`](urlauthenticationchallengesender/cancel(_:).md)
- [`performDefaultHandling(for:)`](urlauthenticationchallengesender/performdefaulthandling(for:).md)
- [`rejectProtectionSpaceAndContinue(with:)`](urlauthenticationchallengesender/rejectprotectionspaceandcontinue(with:).md)

> ❗ **Important**:  Your delegate method is called on the thread where the connection is scheduled. Always call the methods above on that same thread.

You might also want to analyze `challenge` for the authentication scheme and the proposed credential before calling a [`URLAuthenticationChallengeSender`](urlauthenticationchallengesender.md) method. You should never assume that a proposed credential is present. You can either create your own credential and respond with that, or you can send the proposed credential back. (Because this object is immutable, if you want to change it you must copy it and then modify the copy.)

## Parameters

- `connection`: The connection sending the message.
- `challenge`: The authentication challenge for which a request is being sent.

## See Also

- [URL Loading System](url-loading-system.md)
  Interact with URLs and communicate with servers using standard Internet protocols.
- [func connection(NSURLConnection, canAuthenticateAgainstProtectionSpace: URLProtectionSpace) -> Bool](nsurlconnectiondelegate/connection(_:canauthenticateagainstprotectionspace:).md)
  Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [func connection(NSURLConnection, didCancel: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:didcancel:).md)
  Sent when a connection cancels an authentication challenge.
- [func connection(NSURLConnection, didReceive: URLAuthenticationChallenge)](nsurlconnectiondelegate/connection(_:didreceive:).md)
  Sent when a connection must authenticate a challenge in order to download its request.
- [func connectionShouldUseCredentialStorage(NSURLConnection) -> Bool](nsurlconnectiondelegate/connectionshouldusecredentialstorage(_:).md)
  Sent to determine whether the URL loader should use the credential storage for authenticating the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connection(_:willsendrequestfor:))*