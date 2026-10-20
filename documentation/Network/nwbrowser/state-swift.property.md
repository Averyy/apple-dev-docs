# state

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

The current state of the browser.

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
final var state: NWBrowser.State { get }
```

## See Also

### Managing Browsers
- [var stateUpdateHandler: ((NWBrowser.State) -> Void)?](./stateupdatehandler.md)
  A handler that receives browser state updates.
- [NWBrowser.State](./state-swift.enum.md)
  States indicating whether a browser is able to discover services.
- [func cancel()](./cancel%28%29.md)
  Stops browsing for services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/state-swift.property)*