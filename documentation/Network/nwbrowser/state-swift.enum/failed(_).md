# NWBrowser.State.failed(_:)

**Framework**: Network  
**Kind**: case  
**Role**: Case

The browser has encountered a fatal error.

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
case failed(NWError)
```

## See Also

### States
- [NWBrowser.State.setup](./setup.md)
  The browser has been initialized but not started.
- [NWBrowser.State.ready](./ready.md)
  The browser is registered for discovering services.
- [NWBrowser.State.cancelled](./cancelled.md)
  The browser has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/state-swift.enum/failed(_:))*