# Stream.Event

**Framework**: Foundation  
**Kind**: struct

Describes the constants that may be sent to the delegate as a bit field in the second parameter of [`stream(_:handle:)`](streamdelegate/stream(_:handle:).md) to specify the kind of stream event.

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
struct Event
```

## Topics

### Constants
- [static var openCompleted: Stream.Event](stream/event/opencompleted.md)
  The open has completed successfully.
- [static var hasBytesAvailable: Stream.Event](stream/event/hasbytesavailable.md)
  The stream has bytes to be read.
- [static var hasSpaceAvailable: Stream.Event](stream/event/hasspaceavailable.md)
  The stream can accept bytes for writing.
- [static var errorOccurred: Stream.Event](stream/event/erroroccurred.md)
  An error has occurred on the stream.
- [static var endEncountered: Stream.Event](stream/event/endencountered.md)
  The end of the stream has been reached.
- [static var openCompleted: Stream.Event](stream/event/opencompleted.md)
  The open has completed successfully.
- [static var hasBytesAvailable: Stream.Event](stream/event/hasbytesavailable.md)
  The stream has bytes to be read.
- [static var hasSpaceAvailable: Stream.Event](stream/event/hasspaceavailable.md)
  The stream can accept bytes for writing.
- [static var errorOccurred: Stream.Event](stream/event/erroroccurred.md)
  An error has occurred on the stream.
- [static var endEncountered: Stream.Event](stream/event/endencountered.md)
  The end of the stream has been reached.
### Initializers
- [init(rawValue: UInt)](stream/event/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Stream.Status](stream/status.md)
  The type declared for the constants listed in doc:stream/stream_status_constants.
- [Stream Status Constants](stream_status_constants.md)
  These constants indicate the current status of a stream. They are returned by [`streamStatus`](stream/streamstatus.md).
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/event)*