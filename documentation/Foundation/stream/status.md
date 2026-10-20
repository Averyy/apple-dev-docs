# Stream.Status

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSStreamStatus : NSUInteger;
```

## Topics

### Enumeration Cases
- [Stream.Status.atEnd](./status/atend.md)
  There is no more data to read, or no more data can be written to the stream. When this status is returned, the stream is in a “non-blocking” mode and no data are available.
- [Stream.Status.closed](./status/closed.md)
  The stream is closed ([`close()`](./close%28%29.md) has been called on it).
- [Stream.Status.error](./status/error.md)
  The remote end of the connection can’t be contacted, or the connection has been severed for some other reason.
- [Stream.Status.notOpen](./status/notopen.md)
  The stream is not open for reading or writing. This status is returned before the underlying call to open a stream but after it’s been created.
- [Stream.Status.open](./status/open.md)
  The stream is open, but no reading or writing is occurring.
- [Stream.Status.opening](./status/opening.md)
  The stream is in the process of being opened for reading or for writing. For network streams, this status might include the time after the stream was opened, but while network DNS resolution is happening.
- [Stream.Status.reading](./status/reading.md)
  Data is being read from the stream. This status would be returned if code on another thread were to call [`streamStatus`](./streamstatus.md) on the stream while a [`read(_:maxLength:)`](../inputstream/read%28_,maxlength%29.md) call ([`InputStream`](../inputstream.md)) was in progress.
- [Stream.Status.writing](./status/writing.md)
  Data is being written to the stream. This status would be returned if code on another thread were to call [`streamStatus`](./streamstatus.md) on the stream while a [`write(_:maxLength:)`](../outputstream/write%28_,maxlength%29.md) call ([`OutputStream`](../outputstream.md)) was in progress.
### Initializers
- [init?(rawValue: UInt)](./status/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [Stream Status Constants](../stream_status_constants.md)
  These constants indicate the current status of a stream. They are returned by [`streamStatus`](./streamstatus.md).
- [Stream.Event](./event.md)
  Describes the constants that may be sent to the delegate as a bit field in the second parameter of [`stream(_:handle:)`](../streamdelegate/stream%28_,handle%29.md) to specify the kind of stream event.
- [struct StreamNetworkServiceTypeValue](../streamnetworkservicetypevalue.md)
  `NSStream` defines these string constants for specifying the service type of a stream.
- [struct StreamSOCKSProxyConfiguration](../streamsocksproxyconfiguration.md)
- [struct StreamSOCKSProxyVersion](../streamsocksproxyversion.md)
- [struct StreamSocketSecurityLevel](../streamsocketsecuritylevel.md)
  `NSStream` defines these string constants for specifying the secure-socket layer (SSL) security level.
- [Stream.PropertyKey](./propertykey.md)
  `NSStream` defines these string constants as keys for accessing stream properties using [`property(forKey:)`](./property%28forkey%29.md) and setting properties with [`setProperty(_:forKey:)`](./setproperty%28_,forkey%29.md):
- [let NSStreamSocketSSLErrorDomain: String](../nsstreamsocketsslerrordomain.md)
  The error domain used by `NSError` when reporting SSL errors.
- [let NSStreamSOCKSErrorDomain: String](../nsstreamsockserrordomain.md)
  The error domain used by `NSError` when reporting SOCKS errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/status)*