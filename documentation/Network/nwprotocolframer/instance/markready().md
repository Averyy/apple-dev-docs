# markReady()

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Indicates to a connection that your protocol’s handshake is complete.

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
final func markReady()
```

## See Also

### Related Documentation
- [NWProtocolFramer.StartResult.willMarkReady](../startresult/willmarkready.md)
  The protocol will perform a handshake, preventing the overall connection from becoming ready until [`markReady()`](./markready%28%29.md) is called.
### Managing Instance Lifetime
- [func markFailed(error: NWError?)](./markfailed%28error%29.md)
  Indicates to a connection that your protocol has encountered an error, or has gracefully closed.
- [func prependApplicationProtocol(options: NWProtocolOptions) throws](./prependapplicationprotocol%28options%29.md)
  Dynamically adds another protocol that will run above your protocol after your protocol calls [`markReady()`](./markready%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/instance/markready())*