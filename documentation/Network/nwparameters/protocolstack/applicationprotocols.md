# applicationProtocols

**Framework**: Network  
**Kind**: property

The array of application protocol options used by connections and listeners.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var applicationProtocols: [NWProtocolOptions] { get set }
```

#### Discussion

The array of application protocols is ordered with the closest to the application first, and the closest to the transport protocol last. For example, if you want to run the WebSocket protocol over TLS, the WebSocket protocol should come first, and the TLS protocol should come second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/protocolstack/applicationprotocols)*