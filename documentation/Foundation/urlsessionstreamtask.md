# URLSessionStreamTask

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSURLSessionStreamTask : NSURLSessionTask
```

## Overview

[`URLSessionStreamTask`](./urlsessionstreamtask.md) is a concrete subclass of [`URLSessionTask`](./urlsessiontask.md). Many of the methods in the [`URLSessionStreamTask`](./urlsessionstreamtask.md) class are documented in [`URLSessionTask`](./urlsessiontask.md).

The [`URLSessionStreamTask`](./urlsessionstreamtask.md) class provides an interface a TCP/IP connection created via [`URLSession`](./urlsession.md). Tasks may be created from an [`URLSession`](./urlsession.md) using the [`streamTask(withHostName:port:)`](./urlsession/streamtask%28withhostname,port%29.md) and [`streamTask(with:)`](./urlsession/streamtask%28with%29.md) methods. They may also be created as a result of an [`URLSessionDataTask`](./urlsessiondatatask.md) being upgraded via the HTTP `Upgrade:` response header and appropriate use of the [`httpShouldUsePipelining`](./urlsessionconfiguration/httpshouldusepipelining.md) option of [`URLSessionConfiguration`](./urlsessionconfiguration.md).

> **Note**:  See [RFC 2817](https://tools.ietf.org/html/rfc2817) and [RFC 6455](https://tools.ietf.org/html/rfc6455) for information about the `Upgrade:` header.

A [`URLSessionStreamTask`](./urlsessionstreamtask.md) object performs asynchronous reads and writes, which are enqueued and executed serially, calling a handler upon completion being on the session delegate queue. If the task is canceled, all enqueued reads and writes will call their completion handlers with an appropriate error.

When working with APIs that accept [`Stream`](./stream.md) objects, you can create [`InputStream`](./inputstream.md) and [`OutputStream`](./outputstream.md) objects from an [`URLSessionStreamTask`](./urlsessionstreamtask.md) object by calling the [`captureStreams()`](./urlsessionstreamtask/capturestreams%28%29.md) method.

> **Note**:  watchOS supports [`URLSessionStreamTask`](./urlsessionstreamtask.md) for specific use cases. For more details, see [TN3135: Low-level networking on watchOS](../Technotes/tn3135-low-level-networking-on-watchos.md).

## Topics

### Reading and writing data
- [func readData(ofMinLength: Int, maxLength: Int, timeout: TimeInterval, completionHandler: (Data?, Bool, (any Error)?) -> Void)](./urlsessionstreamtask/readdata%28ofminlength,maxlength,timeout,completionhandler%29.md)
  Asynchronously reads a number of bytes from the stream, and calls a handler upon completion.
- [func write(Data, timeout: TimeInterval, completionHandler: ((any Error)?) -> Void)](./urlsessionstreamtask/write%28_,timeout,completionhandler%29.md)
  Asynchronously writes the specified data to the stream, and calls a handler upon completion.
### Capturing streams
- [func captureStreams()](./urlsessionstreamtask/capturestreams%28%29.md)
  Completes any already enqueued reads and writes, and then invokes the [`urlSession(_:streamTask:didBecome:outputStream:)`](./urlsessionstreamdelegate/urlsession%28_,streamtask,didbecome,outputstream%29.md) delegate message.
### Closing read and write sockets
- [func closeRead()](./urlsessionstreamtask/closeread%28%29.md)
  Completes any enqueued reads and writes, and then closes the read side of the underlying socket.
- [func closeWrite()](./urlsessionstreamtask/closewrite%28%29.md)
  Completes any enqueued reads and writes, and then closes the write side of the underlying socket.
### Starting and stopping secure connections
- [func startSecureConnection()](./urlsessionstreamtask/startsecureconnection%28%29.md)
  Completes any enqueued reads and writes, and establishes a secure connection.
- [func stopSecureConnection()](./urlsessionstreamtask/stopsecureconnection%28%29.md)
  Completes any enqueued reads and writes, and closes the secure connection.
### Initializers
- [init()](./urlsessionstreamtask/init%28%29.md)
### Type Methods
- [class func new() -> Self](./urlsessionstreamtask/new%28%29.md)

## Relationships

### Inherits From
- [URLSessionTask](./urlsessiontask.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [ProgressReporting](./progressreporting.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Adding stream tasks to a session
- [func streamTask(withHostName: String, port: Int) -> URLSessionStreamTask](./urlsession/streamtask%28withhostname,port%29.md)
  Creates a task that establishes a bidirectional TCP/IP connection to a specified hostname and port.
- [func streamTask(with: NetService) -> URLSessionStreamTask](./urlsession/streamtask%28with%29.md)
  Creates a task that establishes a bidirectional TCP/IP connection using a specified network service.
- [protocol URLSessionStreamDelegate](./urlsessionstreamdelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to stream tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionstreamtask)*