# Stream.Event

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Describes the constants that may be sent to the delegate as a bit field in the second parameter of [`stream(_:handle:)`](../streamdelegate/stream%28_,handle%29.md) to specify the kind of stream event.

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

```c
enum NSStreamEvent : NSUInteger;
```

## Topics

### Constants
- [static var openCompleted: Stream.Event](./event/opencompleted.md)
  The open has completed successfully.
- [static var hasBytesAvailable: Stream.Event](./event/hasbytesavailable.md)
  The stream has bytes to be read.
- [static var hasSpaceAvailable: Stream.Event](./event/hasspaceavailable.md)
  The stream can accept bytes for writing.
- [static var errorOccurred: Stream.Event](./event/erroroccurred.md)
  An error has occurred on the stream.
- [static var endEncountered: Stream.Event](./event/endencountered.md)
  The end of the stream has been reached.
### Initializers
- [init(rawValue: UInt)](./event/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [Stream.Status](./status.md)
  The type declared for the constants listed in doc:stream/stream_status_constants.
- [Stream Status Constants](../stream_status_constants.md)
  These constants indicate the current status of a stream. They are returned by [`streamStatus`](./streamstatus.md).
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/event)*