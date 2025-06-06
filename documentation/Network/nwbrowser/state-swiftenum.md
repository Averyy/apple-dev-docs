# NWBrowser.State

**Framework**: Network  
**Kind**: enum

States indicating whether a browser is able to discover services.

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
enum State
```

## Topics

### States
- [NWBrowser.State.setup](nwbrowser/state-swift.enum/setup.md)
  The browser has been initialized but not started.
- [NWBrowser.State.ready](nwbrowser/state-swift.enum/ready.md)
  The browser is registered for discovering services.
- [NWBrowser.State.failed(_:)](nwbrowser/state-swift.enum/failed(_:).md)
  The browser has encountered a fatal error.
- [NWBrowser.State.cancelled](nwbrowser/state-swift.enum/cancelled.md)
  The browser has been canceled.
### Enumeration Cases
- [NWBrowser.State.waiting(_:)](nwbrowser/state-swift.enum/waiting(_:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var stateUpdateHandler: ((NWBrowser.State) -> Void)?](nwbrowser/stateupdatehandler.md)
  A handler that receives browser state updates.
- [var state: NWBrowser.State](nwbrowser/state-swift.property.md)
  The current state of the browser.
- [func cancel()](nwbrowser/cancel.md)
  Stops browsing for services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/state-swift.enum)*