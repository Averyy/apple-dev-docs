# init(for:using:)

**Framework**: Network  
**Kind**: init

Initializes a browser with a type of service to discover.

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
init(for descriptor: NWBrowser.Descriptor, using parameters: NWParameters)
```

## See Also

- [NWBrowser.Descriptor](nwbrowser/descriptor-swift.enum.md)
  A service description used to discover Bonjour services.
- [func start(queue: DispatchQueue)](nwbrowser/start(queue:).md)
  Starts browsing for services, and sets the queue on which all browser events will be delivered.
- [var browseResultsChangedHandler: ((Set<NWBrowser.Result>, Set<NWBrowser.Result.Change>) -> Void)?](nwbrowser/browseresultschangedhandler.md)
  A handler that delivers updates about discovered services.
- [NWBrowser.Result](nwbrowser/result.md)
  A set of discovered services and changes from the last result.
- [var browseResults: Set<NWBrowser.Result>](nwbrowser/browseresults.md)
  The list of discovered services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/init(for:using:))*