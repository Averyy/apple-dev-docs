# start(queue:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Starts browsing for services, and sets the queue on which all browser events will be delivered.

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
final func start(queue: DispatchQueue)
```

## See Also

### Browsing for Services
- [init(for: NWBrowser.Descriptor, using: NWParameters)](./init%28for,using%29.md)
  Initializes a browser with a type of service to discover.
- [NWBrowser.Descriptor](./descriptor-swift.enum.md)
  A service description used to discover Bonjour services.
- [var browseResultsChangedHandler: ((Set<NWBrowser.Result>, Set<NWBrowser.Result.Change>) -> Void)?](./browseresultschangedhandler.md)
  A handler that delivers updates about discovered services.
- [NWBrowser.Result](./result.md)
  A set of discovered services and changes from the last result.
- [var browseResults: Set<NWBrowser.Result>](./browseresults.md)
  The list of discovered services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/start(queue:))*