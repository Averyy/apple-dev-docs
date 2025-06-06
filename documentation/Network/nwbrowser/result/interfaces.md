# interfaces

**Framework**: Network  
**Kind**: property

The list of interfaces on which the service was discovered.

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
let interfaces: [NWInterface]
```

## See Also

- [let endpoint: NWEndpoint](nwbrowser/result/endpoint.md)
  The discovered service endpoint.
- [let metadata: NWBrowser.Result.Metadata](nwbrowser/result/metadata-swift.property.md)
  The metadata associated with the discovered service, such as the TXT record.
- [NWBrowser.Result.Metadata](nwbrowser/result/metadata-swift.enum.md)
  Values associated with discovered services, such as TXT records.
- [struct NWTXTRecord](nwtxtrecord.md)
  A dictionary representing a TXT record in a DNS packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/result/interfaces)*