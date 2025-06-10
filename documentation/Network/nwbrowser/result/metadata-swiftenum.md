# NWBrowser.Result.Metadata

**Framework**: Network  
**Kind**: enum

Values associated with discovered services, such as TXT records.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum Metadata
```

## Topics

### Metadata Types
- [NWBrowser.Result.Metadata.bonjour(_:)](nwbrowser/result/metadata-swift.enum/bonjour(_:).md)
  A TXT record associated with a discovered service.
- [NWBrowser.Result.Metadata.none](nwbrowser/result/metadata-swift.enum/none.md)
  A value indicating that no associated data was discovered on a service.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let endpoint: NWEndpoint](nwbrowser/result/endpoint.md)
  The discovered service endpoint.
- [let interfaces: [NWInterface]](nwbrowser/result/interfaces.md)
  The list of interfaces on which the service was discovered.
- [let metadata: NWBrowser.Result.Metadata](nwbrowser/result/metadata-swift.property.md)
  The metadata associated with the discovered service, such as the TXT record.
- [struct NWTXTRecord](nwtxtrecord.md)
  A dictionary representing a TXT record in a DNS packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/result/metadata-swift.enum)*