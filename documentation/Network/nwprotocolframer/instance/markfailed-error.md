# markFailed(error:)

**Framework**: Network  
**Kind**: method

Indicates to a connection that your protocol has encountered an error, or has gracefully closed.

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
final func markFailed(error: NWError?)
```

## See Also

- [func markReady()](nwprotocolframer/instance/markready.md)
  Indicates to a connection that your protocol’s handshake is complete.
- [func prependApplicationProtocol(options: NWProtocolOptions) throws](nwprotocolframer/instance/prependapplicationprotocol(options:).md)
  Dynamically adds another protocol that will run above your protocol after your protocol calls [`markReady()`](nwprotocolframer/instance/markready().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/markfailed(error:))*