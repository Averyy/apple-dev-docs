# networkServiceType

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The type of service for the stream. Providing the service type allows the system to properly handle certain attributes of the stream, including routing and suspension behavior. Most streams do not need to set this property. See `Stream Service Types` for a list of possible values.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let networkServiceType: Stream.PropertyKey
```

```c
extern NSStreamPropertyKey const NSStreamNetworkServiceType;
```

## See Also

### Type Properties
- [static let dataWrittenToMemoryStreamKey: Stream.PropertyKey](./datawrittentomemorystreamkey.md)
  Value is an `NSData` instance containing the data written to a memory stream.
- [static let fileCurrentOffsetKey: Stream.PropertyKey](./filecurrentoffsetkey.md)
  Value is an `NSNumber` object containing the current absolute offset of the stream.
- [static let socketSecurityLevelKey: Stream.PropertyKey](./socketsecuritylevelkey.md)
- [static let socksProxyConfigurationKey: Stream.PropertyKey](./socksproxyconfigurationkey.md)
  Value is an `NSDictionary` object containing SOCKS proxy configuration information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/propertykey/networkservicetype)*