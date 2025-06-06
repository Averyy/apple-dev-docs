# NWBrowser.Descriptor

**Framework**: Network  
**Kind**: enum

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
- [case bonjour(type: String, domain: String?)](nwbrowser/descriptor-swift.enum/bonjour(type:domain:).md)
  A service descriptor used to discover a Bonjour service.
- [case bonjourWithTXTRecord(type: String, domain: String?)](nwbrowser/descriptor-swift.enum/bonjourwithtxtrecord(type:domain:).md)
  A service descriptor used to discover a Bonjour service with associated TXT records.
### Enumeration Cases
- [NWBrowser.Descriptor.applicationService(name:)](nwbrowser/descriptor-swift.enum/applicationservice(name:).md)
  Returns a browser descriptor for application services.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(for: NWBrowser.Descriptor, using: NWParameters)](nwbrowser/init(for:using:).md)
  Initializes a browser with a type of service to discover.
- [func start(queue: DispatchQueue)](nwbrowser/start(queue:).md)
  Starts browsing for services, and sets the queue on which all browser events will be delivered.
- [var browseResultsChangedHandler: ((Set<NWBrowser.Result>, Set<NWBrowser.Result.Change>) -> Void)?](nwbrowser/browseresultschangedhandler.md)
  A handler that delivers updates about discovered services.
- [NWBrowser.Result](nwbrowser/result.md)
  A set of discovered services and changes from the last result.
- [var browseResults: Set<NWBrowser.Result>](nwbrowser/browseresults.md)
  The list of discovered services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/descriptor-swift.enum)*