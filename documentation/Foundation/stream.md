# Stream

**Framework**: Foundation  
**Kind**: class

An abstract class representing a stream.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class Stream
```

## Mentions

- [Uploading streams of data](uploading-streams-of-data.md)

#### Overview

This class’s interface is common to all Cocoa stream classes, including its concrete subclasses [`InputStream`](inputstream.md) and [`OutputStream`](outputstream.md).

[`Stream`](stream.md) objects provide an easy way to read and write data to and from a variety of media in a device-independent way. You can create stream objects for data located in memory, in a file, or on a network (using sockets), and you can use stream objects without loading all of the data into memory at once.

By default, [`Stream`](stream.md) instances that aren’t file-based are non-seekable, one-way streams (although custom seekable subclasses are possible). After you provide or consume data, you can’t retrieve the data from the stream.

##### Subclassing Notes

[`Stream`](stream.md) is an abstract class, incapable of instantiation and intended for you to subclass it. It publishes a programmatic interface that all subclasses must adopt and provide implementations for. The two Apple-provided concrete subclasses of [`Stream`](stream.md), [`InputStream`](inputstream.md) and [`OutputStream`](outputstream.md), are suitable for most purposes. However, there might be situations when you want a peer subclass to [`InputStream`](inputstream.md) and [`OutputStream`](outputstream.md). For example, you might want a class that implements a full-duplex (two-way) stream, or a class whose instances are capable of seeking through a stream.

###### Methods to Override

All subclasses must fully implement the following methods:

- [`open()`](stream/open().md) and [`close()`](stream/close().md)

Implement [`open()`](stream/open().md) to open the stream for reading or writing and make the stream available to the client directly or, if the stream object is scheduled on a run loop, to the delegate. Implement [`close()`](stream/close().md) to close the stream and remove the stream object from the run loop, if necessary. A closed stream should still be able to accept new properties and report its current properties. Once you close a stream, you can’t reopen it.

- [`delegate`](stream/delegate.md)

Return and set the delegate. By a default, a stream object must be its own delegate; so a [`delegate`](stream/delegate.md) message with an argument of `nil` should restore this delegate. Don’t retain the delegate to prevent retain cycles.

To learn about delegates and delegation, read “Delegation” in Cocoa Fundamentals Guide.

- [`schedule(in:forMode:)`](stream/schedule(in:formode:).md) and [`remove(from:forMode:)`](stream/remove(from:formode:).md)

Implement [`schedule(in:forMode:)`](stream/schedule(in:formode:).md) to schedule the stream object on the specified run loop for the specified mode. Implement [`remove(from:forMode:)`](stream/remove(from:formode:).md) to remove the object from the run loop. See the documentation of the [`RunLoop`](runloop.md) class for details. Once the stream object for an open stream is scheduled on a run loop, it is the responsibility of the subclass as it processes stream data to send [`stream(_:handle:)`](streamdelegate/stream(_:handle:).md) messages to its delegate.

- [`property(forKey:)`](stream/property(forkey:).md) and [`setProperty(_:forKey:)`](stream/setproperty(_:forkey:).md)

Implement these methods to return and set, respectively, the property value for the specified key. You may add custom properties, but be sure to handle all properties defined by [`Stream`](stream.md) as well.

- [`streamStatus`](stream/streamstatus.md) and [`streamError`](stream/streamerror.md)

Implement [`streamStatus`](stream/streamstatus.md) to return the current status of the stream as a [`Stream.Status`](stream/status.md) constant; you may define new [`Stream.Status`](stream/status.md) constants, but be sure to handle the system defined constants properly. Implement [`streamError`](stream/streamerror.md) to return an [`NSError`](nserror.md) object representing the current error. You might decide to return a custom [`NSError`](nserror.md) object that can provide complete and localized information about the error.

## Topics

### Creating Streams
- [class func getStreamsTo(Host, port: Int, inputStream: AutoreleasingUnsafeMutablePointer<InputStream?>?, outputStream: AutoreleasingUnsafeMutablePointer<OutputStream?>?)](stream/getstreamsto(_:port:inputstream:outputstream:).md)
  Creates and returns by reference an `NSInputStream` object and `NSOutputStream` object for a socket connection with a given host on a given port.
### Configuring Streams
- [func property(forKey: Stream.PropertyKey) -> Any?](stream/property(forkey:).md)
  Returns the receiver’s property for a given key.
- [func setProperty(Any?, forKey: Stream.PropertyKey) -> Bool](stream/setproperty(_:forkey:).md)
  Attempts to set the value of a given property of the receiver and returns a Boolean value that indicates whether the value is accepted by the receiver.
- [var delegate: (any StreamDelegate)?](stream/delegate.md)
  Sets the receiver’s delegate.
### Using Streams
- [func open()](stream/open.md)
  Opens the receiving stream.
- [func close()](stream/close.md)
  Closes the receiver.
### Managing Run Loops
- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](stream/schedule(in:formode:).md)
  Schedules the receiver on a given run loop in a given mode.
- [func remove(from: RunLoop, forMode: RunLoop.Mode)](stream/remove(from:formode:).md)
  Removes the receiver from a given run loop running in a given mode.
### Getting Stream Information
- [var streamStatus: Stream.Status](stream/streamstatus.md)
  Returns the receiver’s status.
- [var streamError: (any Error)?](stream/streamerror.md)
  Returns an `NSError` object representing the stream error.
### Constants
- [Stream.Status](stream/status.md)
  The type declared for the constants listed in doc:stream/stream_status_constants.
- [Stream Status Constants](stream_status_constants.md)
  These constants indicate the current status of a stream. They are returned by [`streamStatus`](stream/streamstatus.md).
- [Stream.Event](stream/event.md)
  Describes the constants that may be sent to the delegate as a bit field in the second parameter of [`stream(_:handle:)`](streamdelegate/stream(_:handle:).md) to specify the kind of stream event.
- [struct StreamNetworkServiceTypeValue](streamnetworkservicetypevalue.md)
  `NSStream` defines these string constants for specifying the service type of a stream.
- [struct StreamSOCKSProxyConfiguration](streamsocksproxyconfiguration.md)
- [struct StreamSOCKSProxyVersion](streamsocksproxyversion.md)
- [struct StreamSocketSecurityLevel](streamsocketsecuritylevel.md)
  `NSStream` defines these string constants for specifying the secure-socket layer (SSL) security level.
- [Stream.PropertyKey](stream/propertykey.md)
  `NSStream` defines these string constants as keys for accessing stream properties using [`property(forKey:)`](stream/property(forkey:).md) and setting properties with [`setProperty(_:forKey:)`](stream/setproperty(_:forkey:).md):
- [let NSStreamSocketSSLErrorDomain: String](nsstreamsocketsslerrordomain.md)
  The error domain used by `NSError` when reporting SSL errors.
- [let NSStreamSOCKSErrorDomain: String](nsstreamsockserrordomain.md)
  The error domain used by `NSError` when reporting SOCKS errors.
### Type Methods
- [class func getBoundStreams(withBufferSize: Int, inputStream: AutoreleasingUnsafeMutablePointer<InputStream?>?, outputStream: AutoreleasingUnsafeMutablePointer<OutputStream?>?)](stream/getboundstreams(withbuffersize:inputstream:outputstream:).md)
  Creates and returns by reference a bound pair of input and output streams.
- [class func getStreamsToHost(withName: String, port: Int, inputStream: AutoreleasingUnsafeMutablePointer<InputStream?>?, outputStream: AutoreleasingUnsafeMutablePointer<OutputStream?>?)](stream/getstreamstohost(withname:port:inputstream:outputstream:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [InputStream](inputstream.md)
- [OutputStream](outputstream.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class InputStream](inputstream.md)
  A stream that provides read-only stream functionality.
- [class OutputStream](outputstream.md)
  A stream that provides write-only stream functionality.
- [protocol StreamDelegate](streamdelegate.md)
  An interface that delegates of a stream instance use to handle events on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream)*