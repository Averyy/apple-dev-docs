# Stream.PropertyKey

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

`NSStream` defines these string constants as keys for accessing stream properties using [`property(forKey:)`](./property%28forkey%29.md) and setting properties with [`setProperty(_:forKey:)`](./setproperty%28_,forkey%29.md):

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
struct PropertyKey
```

```c
typedef NSString * NSStreamPropertyKey;
```

## Topics

### Type Properties
- [static let dataWrittenToMemoryStreamKey: Stream.PropertyKey](./propertykey/datawrittentomemorystreamkey.md)
  Value is an `NSData` instance containing the data written to a memory stream.
- [static let fileCurrentOffsetKey: Stream.PropertyKey](./propertykey/filecurrentoffsetkey.md)
  Value is an `NSNumber` object containing the current absolute offset of the stream.
- [static let networkServiceType: Stream.PropertyKey](./propertykey/networkservicetype.md)
  The type of service for the stream. Providing the service type allows the system to properly handle certain attributes of the stream, including routing and suspension behavior. Most streams do not need to set this property. See `Stream Service Types` for a list of possible values.
- [static let socketSecurityLevelKey: Stream.PropertyKey](./propertykey/socketsecuritylevelkey.md)
- [static let socksProxyConfigurationKey: Stream.PropertyKey](./propertykey/socksproxyconfigurationkey.md)
  Value is an `NSDictionary` object containing SOCKS proxy configuration information.
### Initializers
- [init(String)](./propertykey/init%28_%29.md)
- [init(rawValue: String)](./propertykey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [Stream.Status](./status.md)
  The type declared for the constants listed in doc:stream/stream_status_constants.
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
- [let NSStreamSocketSSLErrorDomain: String](../nsstreamsocketsslerrordomain.md)
  The error domain used by `NSError` when reporting SSL errors.
- [let NSStreamSOCKSErrorDomain: String](../nsstreamsockserrordomain.md)
  The error domain used by `NSError` when reporting SOCKS errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/propertykey)*