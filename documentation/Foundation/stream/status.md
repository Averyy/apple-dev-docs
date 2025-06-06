# Stream.Status

**Framework**: Foundation  
**Kind**: enum

The type declared for the constants listed in doc:stream/stream_status_constants.

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
enum Status
```

## Topics

### Enumeration Cases
- [Stream.Status.atEnd](stream/status/atend.md)
  There is no more data to read, or no more data can be written to the stream. When this status is returned, the stream is in a “non-blocking” mode and no data are available.
- [Stream.Status.closed](stream/status/closed.md)
  The stream is closed ([`close()`](stream/close().md) has been called on it).
- [Stream.Status.error](stream/status/error.md)
  The remote end of the connection can’t be contacted, or the connection has been severed for some other reason.
- [Stream.Status.notOpen](stream/status/notopen.md)
  The stream is not open for reading or writing. This status is returned before the underlying call to open a stream but after it’s been created.
- [Stream.Status.open](stream/status/open.md)
  The stream is open, but no reading or writing is occurring.
- [Stream.Status.opening](stream/status/opening.md)
  The stream is in the process of being opened for reading or for writing. For network streams, this status might include the time after the stream was opened, but while network DNS resolution is happening.
- [Stream.Status.reading](stream/status/reading.md)
  Data is being read from the stream. This status would be returned if code on another thread were to call [`streamStatus`](stream/streamstatus.md) on the stream while a [`read(_:maxLength:)`](inputstream/read(_:maxlength:).md) call ([`InputStream`](inputstream.md)) was in progress.
- [Stream.Status.writing](stream/status/writing.md)
  Data is being written to the stream. This status would be returned if code on another thread were to call [`streamStatus`](stream/streamstatus.md) on the stream while a [`write(_:maxLength:)`](outputstream/write(_:maxlength:).md) call ([`OutputStream`](outputstream.md)) was in progress.
- [Stream.Status.atEnd](stream/status/atend.md)
  There is no more data to read, or no more data can be written to the stream. When this status is returned, the stream is in a “non-blocking” mode and no data are available.
- [Stream.Status.closed](stream/status/closed.md)
  The stream is closed ([`close()`](stream/close().md) has been called on it).
- [Stream.Status.error](stream/status/error.md)
  The remote end of the connection can’t be contacted, or the connection has been severed for some other reason.
- [Stream.Status.notOpen](stream/status/notopen.md)
  The stream is not open for reading or writing. This status is returned before the underlying call to open a stream but after it’s been created.
- [Stream.Status.open](stream/status/open.md)
  The stream is open, but no reading or writing is occurring.
- [Stream.Status.opening](stream/status/opening.md)
  The stream is in the process of being opened for reading or for writing. For network streams, this status might include the time after the stream was opened, but while network DNS resolution is happening.
- [Stream.Status.reading](stream/status/reading.md)
  Data is being read from the stream. This status would be returned if code on another thread were to call [`streamStatus`](stream/streamstatus.md) on the stream while a [`read(_:maxLength:)`](inputstream/read(_:maxlength:).md) call ([`InputStream`](inputstream.md)) was in progress.
- [Stream.Status.writing](stream/status/writing.md)
  Data is being written to the stream. This status would be returned if code on another thread were to call [`streamStatus`](stream/streamstatus.md) on the stream while a [`write(_:maxLength:)`](outputstream/write(_:maxlength:).md) call ([`OutputStream`](outputstream.md)) was in progress.
### Initializers
- [init?(rawValue: UInt)](stream/status/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/status)*