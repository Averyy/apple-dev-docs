# init(configuration:delegate:delegateQueue:)

**Framework**: Foundation  
**Kind**: init

Creates a session with the specified session configuration, delegate, and operation queue.

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
init(configuration: URLSessionConfiguration, delegate: (any URLSessionDelegate)?, delegateQueue queue: OperationQueue?)
```

## Mentions

- [Fetching website data into memory](fetching-website-data-into-memory.md)

## Parameters

- `configuration`: A configuration object that specifies certain behaviors, such as caching policies, timeouts, proxies, pipelining, TLS versions to support, cookie policies, and credential storage. See [`URLSessionConfiguration`](urlsessionconfiguration.md) for more information.
- `delegate`: A session delegate object that handles requests for authentication and other session-related events. This delegate object is responsible for handling authentication challenges, for making caching decisions, and for handling other session-related events. If `nil`, the class should be used only with methods that take completion handlers. > ❗ **Important**:  The session object keeps a strong reference to the delegate until your app exits or explicitly invalidates the session. If you do not invalidate the session by calling the [`invalidateAndCancel()`](urlsession/invalidateandcancel().md) or [`finishTasksAndInvalidate()`](urlsession/finishtasksandinvalidate().md) method, your app leaks memory until it exits.
- `queue`: An operation queue for scheduling the delegate calls and completion handlers. The queue should be a serial queue, in order to ensure the correct ordering of callbacks. If `nil`, the session creates a serial operation queue for performing all delegate method calls and completion handler calls.

## See Also

- [init(configuration: URLSessionConfiguration)](urlsession/init(configuration:).md)
  Creates a session with the specified session configuration.
- [class URLSessionConfiguration](urlsessionconfiguration.md)
  A configuration object that defines behavior and policies for a URL session.
- [var configuration: URLSessionConfiguration](urlsession/configuration.md)
  A copy of the configuration object for this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/init(configuration:delegate:delegatequeue:))*