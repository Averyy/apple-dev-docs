# NWBrowser.Result

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

A set of discovered services and changes from the last result.

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
struct Result
```

## Topics

### Evaluating Browser Results
- [let endpoint: NWEndpoint](./result/endpoint.md)
  The discovered service endpoint.
- [let interfaces: [NWInterface]](./result/interfaces.md)
  The list of interfaces on which the service was discovered.
- [let metadata: NWBrowser.Result.Metadata](./result/metadata-swift.property.md)
  The metadata associated with the discovered service, such as the TXT record.
- [NWBrowser.Result.Metadata](./result/metadata-swift.enum.md)
  Values associated with discovered services, such as TXT records.
- [struct NWTXTRecord](../nwtxtrecord.md)
  A dictionary representing a TXT record in a DNS packet.
### Comparing Results
- [NWBrowser.Result.Change](./result/change.md)
  Ways in which discovered services can change between specific results.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Browsing for Services
- [init(for: NWBrowser.Descriptor, using: NWParameters)](./init%28for,using%29.md)
  Initializes a browser with a type of service to discover.
- [NWBrowser.Descriptor](./descriptor-swift.enum.md)
  A service description used to discover Bonjour services.
- [func start(queue: DispatchQueue)](./start%28queue%29.md)
  Starts browsing for services, and sets the queue on which all browser events will be delivered.
- [var browseResultsChangedHandler: ((Set<NWBrowser.Result>, Set<NWBrowser.Result.Change>) -> Void)?](./browseresultschangedhandler.md)
  A handler that delivers updates about discovered services.
- [var browseResults: Set<NWBrowser.Result>](./browseresults.md)
  The list of discovered services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/result)*