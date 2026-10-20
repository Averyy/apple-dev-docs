# NWProtocolFramer.StartResult.willMarkReady

**Framework**: Network  
**Kind**: case  
**Role**: Case

The protocol will perform a handshake, preventing the overall connection from becoming ready until [`markReady()`](../instance/markready%28%29.md) is called.

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
case willMarkReady
```

## See Also

### Related Documentation
- [func markReady()](../instance/markready%28%29.md)
  Indicates to a connection that your protocol’s handshake is complete.
### Start Results
- [NWProtocolFramer.StartResult.ready](./ready.md)
  The protocol is immediately ready to send and receive data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolframer/startresult/willmarkready)*