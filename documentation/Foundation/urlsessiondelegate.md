# URLSessionDelegate

**Framework**: Foundation  
**Kind**: protocol

A protocol that defines methods that URL session instances call on their delegates to handle session-level events, like session life cycle changes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol URLSessionDelegate : NSObjectProtocol, Sendable
```

## Mentions

- [Fetching website data into memory](fetching-website-data-into-memory.md)
- [Performing manual server trust authentication](performing-manual-server-trust-authentication.md)
- [Uploading data to a website](uploading-data-to-a-website.md)
- [Downloading files in the background](downloading-files-in-the-background.md)

#### Overview

In addition to the methods defined in this protocol, most delegates should also implement some or all of the methods in the [`URLSessionTaskDelegate`](urlsessiontaskdelegate.md), [`URLSessionDataDelegate`](urlsessiondatadelegate.md), and [`URLSessionDownloadDelegate`](urlsessiondownloaddelegate.md) protocols to handle task-level events. These include events like the beginning and end of individual tasks, and periodic progress updates from data or download tasks.

> **Note**:  Your [`URLSession`](urlsession.md) object doesn’t need to have a delegate. If no delegate is assigned, a system-provided delegate is used, and you must provide a completion callback to obtain the data.

## Topics

### Handling session life cycle changes
- [func urlSession(URLSession, didBecomeInvalidWithError: (any Error)?)](urlsessiondelegate/urlsession(_:didbecomeinvalidwitherror:).md)
  Tells the URL session that the session has been invalidated.
- [func urlSessionDidFinishEvents(forBackgroundURLSession: URLSession)](urlsessiondelegate/urlsessiondidfinishevents(forbackgroundurlsession:).md)
  Tells the delegate that all messages enqueued for a session have been delivered.
### Handling authentication challenges
- [func urlSession(URLSession, didReceive: URLAuthenticationChallenge, completionHandler: (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)](urlsessiondelegate/urlsession(_:didreceive:completionhandler:).md)
  Requests credentials from the delegate in response to a session-level authentication request from the remote server.
- [URLSession.AuthChallengeDisposition](urlsession/authchallengedisposition.md)
  Constants passed by session or task delegates to the provided continuation block in response to an authentication challenge.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
### Inherited By
- [URLSessionDataDelegate](urlsessiondatadelegate.md)
- [URLSessionDownloadDelegate](urlsessiondownloaddelegate.md)
- [URLSessionStreamDelegate](urlsessionstreamdelegate.md)
- [URLSessionTaskDelegate](urlsessiontaskdelegate.md)
- [URLSessionWebSocketDelegate](urlsessionwebsocketdelegate.md)

## See Also

- [var delegate: (any URLSessionDelegate)?](urlsession/delegate.md)
  The delegate assigned when this object was created.
- [protocol URLSessionTaskDelegate](urlsessiontaskdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events.
- [var delegateQueue: OperationQueue](urlsession/delegatequeue.md)
  The operation queue provided when this object was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/urlsessiondelegate)*