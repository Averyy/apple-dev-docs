# URLSessionStreamDelegate

**Framework**: Foundation  
**Kind**: protocol

A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to stream tasks.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol URLSessionStreamDelegate : URLSessionTaskDelegate
```

#### Overview

In addition to these methods, be sure to implement the methods in the [`URLSessionTaskDelegate`](urlsessiontaskdelegate.md) and [`URLSessionDelegate`](urlsessiondelegate.md) protocols to handle events common to all task types and session-level events, respectively.

> **Note**: A [`URLSession`](urlsession.md) object need not have a delegate. If no delegate is assigned, a system-provided delegate is used, and you must provide a completion callback to obtain the data.

A [`URLSession`](urlsession.md) object need not have a delegate. If no delegate is assigned, a system-provided delegate is used, and you must provide a completion callback to obtain the data.

## Topics

### Handling rerouting
- [func urlSession(URLSession, betterRouteDiscoveredFor: URLSessionStreamTask)](urlsessionstreamdelegate/urlsession(_:betterroutediscoveredfor:).md)
  Tells the delegate that a better route to the host has been detected for the stream.
### Completing stream capture
- [func urlSession(URLSession, streamTask: URLSessionStreamTask, didBecome: InputStream, outputStream: OutputStream)](urlsessionstreamdelegate/urlsession(_:streamtask:didbecome:outputstream:).md)
  Tells the delegate that the stream task has been completed as a result of the stream task calling the [`captureStreams()`](urlsessionstreamtask/capturestreams().md) method.
### Handling closing events
- [func urlSession(URLSession, readClosedFor: URLSessionStreamTask)](urlsessionstreamdelegate/urlsession(_:readclosedfor:).md)
  Tells the delegate that the read side of the underlying socket has been closed.
- [func urlSession(URLSession, writeClosedFor: URLSessionStreamTask)](urlsessionstreamdelegate/urlsession(_:writeclosedfor:).md)
  Tells the delegate that the write side of the underlying socket has been closed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [URLSessionDelegate](urlsessiondelegate.md)
- [URLSessionTaskDelegate](urlsessiontaskdelegate.md)

## See Also

- [func streamTask(withHostName: String, port: Int) -> URLSessionStreamTask](urlsession/streamtask(withhostname:port:).md)
  Creates a task that establishes a bidirectional TCP/IP connection to a specified hostname and port.
- [func streamTask(with: NetService) -> URLSessionStreamTask](urlsession/streamtask(with:).md)
  Creates a task that establishes a bidirectional TCP/IP connection using a specified network service.
- [class URLSessionStreamTask](urlsessionstreamtask.md)
  A URL session task that is stream-based.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate)*