# NWBrowser.Result.Metadata

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
- [NWBrowser.Result.Metadata.bonjour(_:)](./metadata-swift.enum/bonjour%28_%29.md)
  A TXT record associated with a discovered service.
- [NWBrowser.Result.Metadata.none](./metadata-swift.enum/none.md)
  A value indicating that no associated data was discovered on a service.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Evaluating Browser Results
- [let endpoint: NWEndpoint](./endpoint.md)
  The discovered service endpoint.
- [let interfaces: [NWInterface]](./interfaces.md)
  The list of interfaces on which the service was discovered.
- [let metadata: NWBrowser.Result.Metadata](./metadata-swift.property.md)
  The metadata associated with the discovered service, such as the TXT record.
- [struct NWTXTRecord](../../nwtxtrecord.md)
  A dictionary representing a TXT record in a DNS packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/result/metadata-swift.enum)*