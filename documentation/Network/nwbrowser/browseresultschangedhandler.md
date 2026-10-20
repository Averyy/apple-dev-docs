# browseResultsChangedHandler

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A handler that delivers updates about discovered services.

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
@preconcurrency
final var browseResultsChangedHandler: (@Sendable (Set<NWBrowser.Result>, Set<NWBrowser.Result.Change>) -> Void)? { get set }
```

## See Also

### Browsing for Services
- [init(for: NWBrowser.Descriptor, using: NWParameters)](./init%28for,using%29.md)
  Initializes a browser with a type of service to discover.
- [NWBrowser.Descriptor](./descriptor-swift.enum.md)
  A service description used to discover Bonjour services.
- [func start(queue: DispatchQueue)](./start%28queue%29.md)
  Starts browsing for services, and sets the queue on which all browser events will be delivered.
- [NWBrowser.Result](./result.md)
  A set of discovered services and changes from the last result.
- [var browseResults: Set<NWBrowser.Result>](./browseresults.md)
  The list of discovered services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/browseresultschangedhandler)*