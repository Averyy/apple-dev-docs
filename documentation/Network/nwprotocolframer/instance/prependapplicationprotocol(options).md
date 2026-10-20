# prependApplicationProtocol(options:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Dynamically adds another protocol that will run above your protocol after your protocol calls [`markReady()`](./markready%28%29.md).

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

### Managing Instance Lifetime
- [func markReady()](./markready%28%29.md)
  Indicates to a connection that your protocol’s handshake is complete.
- [func markFailed(error: NWError?)](./markfailed%28error%29.md)
  Indicates to a connection that your protocol has encountered an error, or has gracefully closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/prependapplicationprotocol(options:))*