# dataWrittenToMemoryStreamKey

**Framework**: Foundation  
**Kind**: property

Value is an `NSData` instance containing the data written to a memory stream.

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
static let dataWrittenToMemoryStreamKey: Stream.PropertyKey
```

#### Discussion

Use this property when you have an output-stream object instantiated to collect written data in memory. The value of this property is read-only.

## See Also

- [static let fileCurrentOffsetKey: Stream.PropertyKey](stream/propertykey/filecurrentoffsetkey.md)
  Value is an `NSNumber` object containing the current absolute offset of the stream.
- [static let networkServiceType: Stream.PropertyKey](stream/propertykey/networkservicetype.md)
  The type of service for the stream. Providing the service type allows the system to properly handle certain attributes of the stream, including routing and suspension behavior. Most streams do not need to set this property. See `Stream Service Types` for a list of possible values.
- [static let socketSecurityLevelKey: Stream.PropertyKey](stream/propertykey/socketsecuritylevelkey.md)
- [static let socksProxyConfigurationKey: Stream.PropertyKey](stream/propertykey/socksproxyconfigurationkey.md)
  Value is an `NSDictionary` object containing SOCKS proxy configuration information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/propertykey/datawrittentomemorystreamkey)*