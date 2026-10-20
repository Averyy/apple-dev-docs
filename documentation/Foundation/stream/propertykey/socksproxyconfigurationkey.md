# socksProxyConfigurationKey

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Value is an `NSDictionary` object containing SOCKS proxy configuration information.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let socksProxyConfigurationKey: Stream.PropertyKey
```

```c
extern NSStreamPropertyKey const NSStreamSOCKSProxyConfigurationKey;
```

#### Discussion

The dictionary returned from the System Configuration framework for SOCKS proxies usually suffices.

## See Also

### Type Properties
- [static let dataWrittenToMemoryStreamKey: Stream.PropertyKey](./datawrittentomemorystreamkey.md)
  Value is an `NSData` instance containing the data written to a memory stream.
- [static let fileCurrentOffsetKey: Stream.PropertyKey](./filecurrentoffsetkey.md)
  Value is an `NSNumber` object containing the current absolute offset of the stream.
- [static let networkServiceType: Stream.PropertyKey](./networkservicetype.md)
  The type of service for the stream. Providing the service type allows the system to properly handle certain attributes of the stream, including routing and suspension behavior. Most streams do not need to set this property. See `Stream Service Types` for a list of possible values.
- [static let socketSecurityLevelKey: Stream.PropertyKey](./socketsecuritylevelkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/propertykey/socksproxyconfigurationkey)*