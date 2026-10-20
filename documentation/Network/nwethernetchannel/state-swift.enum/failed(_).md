# NWEthernetChannel.State.failed(_:)

**Framework**: Network  
**Kind**: case  
**Role**: Case

The channel has encountered a fatal error.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case failed(NWError)
```

## See Also

### States
- [NWEthernetChannel.State.setup](./setup.md)
  The channel has been initialized but not started.
- [NWEthernetChannel.State.waiting(_:)](./waiting%28_%29.md)
  The channel is waiting for its interface to become available.
- [NWEthernetChannel.State.preparing](./preparing.md)
  The channel is registering with the interface.
- [NWEthernetChannel.State.ready](./ready.md)
  The channel is able to send and receive Ethernet frames.
- [NWEthernetChannel.State.cancelled](./cancelled.md)
  The channel has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/state-swift.enum/failed(_:))*