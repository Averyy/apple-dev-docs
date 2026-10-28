# URLAuthenticationChallengeSender

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol NSURLAuthenticationChallengeSender <NSObject>
```

## Overview

The methods in the protocol are generally sent by a delegate in response to receiving a [`connection(_:didReceive:)`](./nsurlconnectiondelegate/connection%28_,didreceive%29.md): or [`download(_:didReceive:)`](./nsurldownloaddelegate/download%28_,didreceive%29-1pc0v.md):. The different methods provide different ways of responding to authentication challenges.

> ❗ **Important**:  This protocol is *only* for use with the legacy [`NSURLConnection`](./nsurlconnection.md) and [`NSURLDownload`](./nsurldownload.md) classes. It should not be used with [`URLSession`](./urlsession.md)-based code, for which you respond to authentication challenges by passing [`URLSession.AuthChallengeDisposition`](./urlsession/authchallengedisposition.md) constants to the provided completion handler blocks.

## Topics

### Protocol Methods
- [func cancel(URLAuthenticationChallenge)](./urlauthenticationchallengesender/cancel%28_%29.md)
  Cancels a given authentication challenge.
- [func continueWithoutCredential(for: URLAuthenticationChallenge)](./urlauthenticationchallengesender/continuewithoutcredential%28for%29.md)
  Attempt to continue downloading a request without providing a credential for a given challenge.
- [func use(URLCredential, for: URLAuthenticationChallenge)](./urlauthenticationchallengesender/use%28_,for%29.md)
  Attempt to use a given credential for a given authentication challenge.
- [func performDefaultHandling(for: URLAuthenticationChallenge)](./urlauthenticationchallengesender/performdefaulthandling%28for%29.md)
  Causes the system-provided default behavior to be used.
- [func rejectProtectionSpaceAndContinue(with: URLAuthenticationChallenge)](./urlauthenticationchallengesender/rejectprotectionspaceandcontinue%28with%29.md)
  Rejects the currently supplied protection space.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender)*