# browseResults

**Framework**: Network  
**Kind**: property

The list of discovered services.

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
final var browseResults: Set<NWBrowser.Result> { get }
```

## See Also

- [init(for: NWBrowser.Descriptor, using: NWParameters)](nwbrowser/init(for:using:).md)
  Initializes a browser with a type of service to discover.
- [NWBrowser.Descriptor](nwbrowser/descriptor-swift.enum.md)
  A service description used to discover Bonjour services.
- [func start(queue: DispatchQueue)](nwbrowser/start(queue:).md)
  Starts browsing for services, and sets the queue on which all browser events will be delivered.
- [var browseResultsChangedHandler: ((Set<NWBrowser.Result>, Set<NWBrowser.Result.Change>) -> Void)?](nwbrowser/browseresultschangedhandler.md)
  A handler that delivers updates about discovered services.
- [NWBrowser.Result](nwbrowser/result.md)
  A set of discovered services and changes from the last result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/browseresults)*