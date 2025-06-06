# stateUpdateHandler

**Framework**: Network  
**Kind**: property

A handler that receives browser state updates.

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
final var stateUpdateHandler: ((NWBrowser.State) -> Void)? { get set }
```

## See Also

- [NWBrowser.State](nwbrowser/state-swift.enum.md)
  States indicating whether a browser is able to discover services.
- [var state: NWBrowser.State](nwbrowser/state-swift.property.md)
  The current state of the browser.
- [func cancel()](nwbrowser/cancel.md)
  Stops browsing for services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/stateupdatehandler)*