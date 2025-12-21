# NetworkBrowser.State.failed(_:)

**Framework**: Network  
**Kind**: case

The browser has irrecoverably failed. Do not call `start()` on the browser to restart it. Instead, `cancel()` the browser and create a new browser.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
case failed(NWError)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkbrowser/state/failed(_:))*