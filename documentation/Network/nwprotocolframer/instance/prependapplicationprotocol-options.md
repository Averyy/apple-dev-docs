# prependApplicationProtocol(options:)

**Framework**: Network  
**Kind**: method

Dynamically adds another protocol that will run above your protocol after your protocol calls [`markReady()`](nwprotocolframer/instance/markready().md).

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
final func prependApplicationProtocol(options: NWProtocolOptions) throws
```

## See Also

- [func markReady()](nwprotocolframer/instance/markready.md)
  Indicates to a connection that your protocol’s handshake is complete.
- [func markFailed(error: NWError?)](nwprotocolframer/instance/markfailed(error:).md)
  Indicates to a connection that your protocol has encountered an error, or has gracefully closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/prependapplicationprotocol(options:))*