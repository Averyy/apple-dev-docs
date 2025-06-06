# StreamSocketSecurityLevel

**Framework**: Foundation  
**Kind**: struct

`NSStream` defines these string constants for specifying the secure-socket layer (SSL) security level.

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
struct StreamSocketSecurityLevel
```

#### Discussion

You access and set these values using the `NSStreamSocketSecurityLevelKey` property key.

## Topics

### Type Properties
- [static let negotiatedSSL: StreamSocketSecurityLevel](streamsocketsecuritylevel/negotiatedssl.md)
  Specifies that the highest level security protocol that can be negotiated be set as the security protocol for a socket stream.
- [static let none: StreamSocketSecurityLevel](streamsocketsecuritylevel/none.md)
  Specifies that no security level be set for a socket stream.
- [static let ssLv2: StreamSocketSecurityLevel](streamsocketsecuritylevel/sslv2.md)
  Specifies that SSL version 2 be set as the security protocol for a socket stream.
- [static let ssLv3: StreamSocketSecurityLevel](streamsocketsecuritylevel/sslv3.md)
  Specifies that SSL version 3 be set as the security protocol for a socket stream.
- [static let tlSv1: StreamSocketSecurityLevel](streamsocketsecuritylevel/tlsv1.md)
  Specifies that TLS version 1 be set as the security protocol for a socket stream.
### Initializers
- [init(rawValue: String)](streamsocketsecuritylevel/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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
- [Stream.PropertyKey](stream/propertykey.md)
  `NSStream` defines these string constants as keys for accessing stream properties using [`property(forKey:)`](stream/property(forkey:).md) and setting properties with [`setProperty(_:forKey:)`](stream/setproperty(_:forkey:).md):
- [let NSStreamSocketSSLErrorDomain: String](nsstreamsocketsslerrordomain.md)
  The error domain used by `NSError` when reporting SSL errors.
- [let NSStreamSOCKSErrorDomain: String](nsstreamsockserrordomain.md)
  The error domain used by `NSError` when reporting SOCKS errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/streamsocketsecuritylevel)*