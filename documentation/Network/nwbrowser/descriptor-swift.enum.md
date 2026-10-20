# NWBrowser.Descriptor

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

A service description used to discover Bonjour services.

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
enum Descriptor
```

## Topics

### Descriptor Types
- [case bonjour(type: String, domain: String?)](./descriptor-swift.enum/bonjour%28type,domain%29.md)
  A service descriptor used to discover a Bonjour service.
- [case bonjourWithTXTRecord(type: String, domain: String?)](./descriptor-swift.enum/bonjourwithtxtrecord%28type,domain%29.md)
  A service descriptor used to discover a Bonjour service with associated TXT records.
### Enumeration Cases
- [NWBrowser.Descriptor.applicationService(name:)](./descriptor-swift.enum/applicationservice%28name%29.md)
  Returns a browser descriptor for application services.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Browsing for Services
- [init(for: NWBrowser.Descriptor, using: NWParameters)](./init%28for,using%29.md)
  Initializes a browser with a type of service to discover.
- [func start(queue: DispatchQueue)](./start%28queue%29.md)
  Starts browsing for services, and sets the queue on which all browser events will be delivered.
- [var browseResultsChangedHandler: ((Set<NWBrowser.Result>, Set<NWBrowser.Result.Change>) -> Void)?](./browseresultschangedhandler.md)
  A handler that delivers updates about discovered services.
- [NWBrowser.Result](./result.md)
  A set of discovered services and changes from the last result.
- [var browseResults: Set<NWBrowser.Result>](./browseresults.md)
  The list of discovered services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/descriptor-swift.enum)*