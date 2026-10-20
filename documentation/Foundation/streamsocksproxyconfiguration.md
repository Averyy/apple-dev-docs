# StreamSOCKSProxyConfiguration

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
struct StreamSOCKSProxyConfiguration
```

```c
typedef NSString * NSStreamSOCKSProxyConfiguration;
```

## Topics

### Type Properties
- [static let hostKey: StreamSOCKSProxyConfiguration](./streamsocksproxyconfiguration/hostkey.md)
  Value is an `NSString` object that represents the SOCKS proxy host.
- [static let passwordKey: StreamSOCKSProxyConfiguration](./streamsocksproxyconfiguration/passwordkey.md)
  Value is an `NSString` object containing the user’s password.
- [static let portKey: StreamSOCKSProxyConfiguration](./streamsocksproxyconfiguration/portkey.md)
  Value is an `NSNumber` object containing an integer that represents the port on which the proxy listens.
- [static let userKey: StreamSOCKSProxyConfiguration](./streamsocksproxyconfiguration/userkey.md)
  Value is an `NSString` object containing the user’s name.
- [static let versionKey: StreamSOCKSProxyConfiguration](./streamsocksproxyconfiguration/versionkey.md)
  Value is either `NSStreamSOCKSProxyVersion4` or `NSStreamSOCKSProxyVersion5`.
### Initializers
- [init(rawValue: String)](./streamsocksproxyconfiguration/init%28rawvalue%29.md)

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
- [struct StreamNetworkServiceTypeValue](./streamnetworkservicetypevalue.md)
  `NSStream` defines these string constants for specifying the service type of a stream.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/streamsocksproxyconfiguration)*