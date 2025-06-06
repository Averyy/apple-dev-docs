# URLSessionStreamTask

**Framework**: Foundation  
**Kind**: class

A URL session task that is stream-based.

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
class URLSessionStreamTask
```

#### Overview

[`URLSessionStreamTask`](urlsessionstreamtask.md) is a concrete subclass of [`URLSessionTask`](urlsessiontask.md). Many of the methods in the [`URLSessionStreamTask`](urlsessionstreamtask.md) class are documented in [`URLSessionTask`](urlsessiontask.md).

The [`URLSessionStreamTask`](urlsessionstreamtask.md) class provides an interface a TCP/IP connection created via [`URLSession`](urlsession.md). Tasks may be created from an [`URLSession`](urlsession.md) using the [`streamTask(withHostName:port:)`](urlsession/streamtask(withhostname:port:).md) and [`streamTask(with:)`](urlsession/streamtask(with:).md) methods. They may also be created as a result of an [`URLSessionDataTask`](urlsessiondatatask.md) being upgraded via the HTTP `Upgrade:` response header and appropriate use of the [`httpShouldUsePipelining`](urlsessionconfiguration/httpshouldusepipelining.md) option of [`URLSessionConfiguration`](urlsessionconfiguration.md).

> **Note**:  See [`RFC 2817`](https://developer.apple.comhttps://tools.ietf.org/html/rfc2817) and [`RFC 6455`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6455) for information about the `Upgrade:` header.

A [`URLSessionStreamTask`](urlsessionstreamtask.md) object performs asynchronous reads and writes, which are enqueued and executed serially, calling a handler upon completion being on the session delegate queue. If the task is canceled, all enqueued reads and writes will call their completion handlers with an appropriate error.

When working with APIs that accept [`Stream`](stream.md) objects, you can create [`InputStream`](inputstream.md) and [`OutputStream`](outputstream.md) objects from an [`URLSessionStreamTask`](urlsessionstreamtask.md) object by calling the [`captureStreams()`](urlsessionstreamtask/capturestreams().md) method.

> **Note**:  watchOS supports [`URLSessionStreamTask`](urlsessionstreamtask.md) for specific use cases. For more details, see [`TN3135: Low-level networking on watchOS`](https://developer.apple.com/documentation/Technotes/tn3135-low-level-networking-on-watchOS).

## Topics

### Reading and writing data
- [func readData(ofMinLength: Int, maxLength: Int, timeout: TimeInterval, completionHandler: (Data?, Bool, (any Error)?) -> Void)](urlsessionstreamtask/readdata(ofminlength:maxlength:timeout:completionhandler:).md)
  Asynchronously reads a number of bytes from the stream, and calls a handler upon completion.
- [func write(Data, timeout: TimeInterval, completionHandler: ((any Error)?) -> Void)](urlsessionstreamtask/write(_:timeout:completionhandler:).md)
  Asynchronously writes the specified data to the stream, and calls a handler upon completion.
### Capturing streams
- [func captureStreams()](urlsessionstreamtask/capturestreams.md)
  Completes any already enqueued reads and writes, and then invokes the [`urlSession(_:streamTask:didBecome:outputStream:)`](urlsessionstreamdelegate/urlsession(_:streamtask:didbecome:outputstream:).md) delegate message.
### Closing read and write sockets
- [func closeRead()](urlsessionstreamtask/closeread.md)
  Completes any enqueued reads and writes, and then closes the read side of the underlying socket.
- [func closeWrite()](urlsessionstreamtask/closewrite.md)
  Completes any enqueued reads and writes, and then closes the write side of the underlying socket.
### Starting and stopping secure connections
- [func startSecureConnection()](urlsessionstreamtask/startsecureconnection.md)
  Completes any enqueued reads and writes, and establishes a secure connection.
- [func stopSecureConnection()](urlsessionstreamtask/stopsecureconnection.md)
  Completes any enqueued reads and writes, and closes the secure connection.
### Initializers
- [init()](urlsessionstreamtask/init.md)
### Type Methods
- [class func new() -> Self](urlsessionstreamtask/new.md)

## Relationships

### Inherits From
- [URLSessionTask](urlsessiontask.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [ProgressReporting](progressreporting.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func streamTask(withHostName: String, port: Int) -> URLSessionStreamTask](urlsession/streamtask(withhostname:port:).md)
  Creates a task that establishes a bidirectional TCP/IP connection to a specified hostname and port.
- [func streamTask(with: NetService) -> URLSessionStreamTask](urlsession/streamtask(with:).md)
  Creates a task that establishes a bidirectional TCP/IP connection using a specified network service.
- [protocol URLSessionStreamDelegate](urlsessionstreamdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to stream tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/urlsessionstreamtask)*