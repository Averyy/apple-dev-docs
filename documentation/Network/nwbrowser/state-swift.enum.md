# NWBrowser.State

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
- [NWBrowser.State.setup](./state-swift.enum/setup.md)
  The browser has been initialized but not started.
- [NWBrowser.State.ready](./state-swift.enum/ready.md)
  The browser is registered for discovering services.
- [NWBrowser.State.failed(_:)](./state-swift.enum/failed%28_%29.md)
  The browser has encountered a fatal error.
- [NWBrowser.State.cancelled](./state-swift.enum/cancelled.md)
  The browser has been canceled.
### Enumeration Cases
- [NWBrowser.State.waiting(_:)](./state-swift.enum/waiting%28_%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Browsers
- [var stateUpdateHandler: ((NWBrowser.State) -> Void)?](./stateupdatehandler.md)
  A handler that receives browser state updates.
- [var state: NWBrowser.State](./state-swift.property.md)
  The current state of the browser.
- [func cancel()](./cancel%28%29.md)
  Stops browsing for services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/state-swift.enum)*