# fileCurrentOffsetKey

**Framework**: Foundation  
**Kind**: property

Value is an `NSNumber` object containing the current absolute offset of the stream.

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
static let fileCurrentOffsetKey: Stream.PropertyKey
```

## See Also

- [static let dataWrittenToMemoryStreamKey: Stream.PropertyKey](stream/propertykey/datawrittentomemorystreamkey.md)
  Value is an `NSData` instance containing the data written to a memory stream.
- [static let networkServiceType: Stream.PropertyKey](stream/propertykey/networkservicetype.md)
  The type of service for the stream. Providing the service type allows the system to properly handle certain attributes of the stream, including routing and suspension behavior. Most streams do not need to set this property. See `Stream Service Types` for a list of possible values.
- [static let socketSecurityLevelKey: Stream.PropertyKey](stream/propertykey/socketsecuritylevelkey.md)
- [static let socksProxyConfigurationKey: Stream.PropertyKey](stream/propertykey/socksproxyconfigurationkey.md)
  Value is an `NSDictionary` object containing SOCKS proxy configuration information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/propertykey/filecurrentoffsetkey)*