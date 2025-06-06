# URLAuthenticationChallengeSender

**Framework**: Foundation  
**Kind**: protocol

The `URLAuthenticationChallengeSender` protocol represents the interface that the sender of an authentication challenge must implement.

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
protocol URLAuthenticationChallengeSender : NSObjectProtocol, Sendable
```

#### Overview

The methods in the protocol are generally sent by a delegate in response to receiving a [`connection(_:didReceive:)`](nsurlconnectiondelegate/connection(_:didreceive:).md): or [`download(_:didReceive:)`](nsurldownloaddelegate/download(_:didreceive:)-1pc0v.md):. The different methods provide different ways of responding to authentication challenges.

> ❗ **Important**:  This protocol is  for use with the legacy [`NSURLConnection`](nsurlconnection.md) and [`NSURLDownload`](nsurldownload.md) classes. It should not be used with [`URLSession`](urlsession.md)-based code, for which you respond to authentication challenges by passing [`URLSession.AuthChallengeDisposition`](urlsession/authchallengedisposition.md) constants to the provided completion handler blocks.

 This protocol is  for use with the legacy [`NSURLConnection`](nsurlconnection.md) and [`NSURLDownload`](nsurldownload.md) classes. It should not be used with [`URLSession`](urlsession.md)-based code, for which you respond to authentication challenges by passing [`URLSession.AuthChallengeDisposition`](urlsession/authchallengedisposition.md) constants to the provided completion handler blocks.

## Topics

### Protocol Methods
- [func cancel(URLAuthenticationChallenge)](urlauthenticationchallengesender/cancel(_:).md)
  Cancels a given authentication challenge.
- [func continueWithoutCredential(for: URLAuthenticationChallenge)](urlauthenticationchallengesender/continuewithoutcredential(for:).md)
  Attempt to continue downloading a request without providing a credential for a given challenge.
- [func use(URLCredential, for: URLAuthenticationChallenge)](urlauthenticationchallengesender/use(_:for:).md)
  Attempt to use a given credential for a given authentication challenge.
- [func performDefaultHandling(for: URLAuthenticationChallenge)](urlauthenticationchallengesender/performdefaulthandling(for:).md)
  Causes the system-provided default behavior to be used.
- [func rejectProtectionSpaceAndContinue(with: URLAuthenticationChallenge)](urlauthenticationchallengesender/rejectprotectionspaceandcontinue(with:).md)
  Rejects the currently supplied protection space.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender)*