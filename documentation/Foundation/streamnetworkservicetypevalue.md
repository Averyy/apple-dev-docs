# StreamNetworkServiceTypeValue

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

`NSStream` defines these string constants for specifying the service type of a stream.

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
struct StreamNetworkServiceTypeValue
```

```c
typedef NSString * NSStreamNetworkServiceTypeValue;
```

## Topics

### Type Properties
- [static let background: StreamNetworkServiceTypeValue](./streamnetworkservicetypevalue/background.md)
  Specifies that the stream is providing a background service.
- [static let video: StreamNetworkServiceTypeValue](./streamnetworkservicetypevalue/video.md)
  Specifies that the stream is providing video service.
- [static let voice: StreamNetworkServiceTypeValue](./streamnetworkservicetypevalue/voice.md)
  Specifies that the stream is providing voice service.
- [static let voIP: StreamNetworkServiceTypeValue](./streamnetworkservicetypevalue/voip.md)
  Specifies that the stream is providing VoIP service.
- [static let callSignaling: StreamNetworkServiceTypeValue](./streamnetworkservicetypevalue/callsignaling.md)
### Initializers
- [init(rawValue: String)](./streamnetworkservicetypevalue/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [Stream.Status](./stream/status.md)
  The type declared for the constants listed in doc:stream/stream_status_constants.
- [Stream Status Constants](./stream_status_constants.md)
  These constants indicate the current status of a stream. They are returned by [`streamStatus`](./stream/streamstatus.md).
- [Stream.Event](./stream/event.md)
  Describes the constants that may be sent to the delegate as a bit field in the second parameter of [`stream(_:handle:)`](./streamdelegate/stream%28_,handle%29.md) to specify the kind of stream event.
- [struct StreamSOCKSProxyConfiguration](./streamsocksproxyconfiguration.md)
- [struct StreamSOCKSProxyVersion](./streamsocksproxyversion.md)
- [struct StreamSocketSecurityLevel](./streamsocketsecuritylevel.md)
  `NSStream` defines these string constants for specifying the secure-socket layer (SSL) security level.
- [Stream.PropertyKey](./stream/propertykey.md)
  `NSStream` defines these string constants as keys for accessing stream properties using [`property(forKey:)`](./stream/property%28forkey%29.md) and setting properties with [`setProperty(_:forKey:)`](./stream/setproperty%28_,forkey%29.md):
- [let NSStreamSocketSSLErrorDomain: String](./nsstreamsocketsslerrordomain.md)
  The error domain used by `NSError` when reporting SSL errors.
- [let NSStreamSOCKSErrorDomain: String](./nsstreamsockserrordomain.md)
  The error domain used by `NSError` when reporting SOCKS errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/streamnetworkservicetypevalue)*