# NWEthernetChannel.State.setup

**Framework**: Network  
**Kind**: case

The channel has been initialized but not started.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case setup
```

## See Also

- [NWEthernetChannel.State.waiting(_:)](nwethernetchannel/state-swift.enum/waiting(_:).md)
  The channel is waiting for its interface to become available.
- [NWEthernetChannel.State.preparing](nwethernetchannel/state-swift.enum/preparing.md)
  The channel is registering with the interface.
- [NWEthernetChannel.State.ready](nwethernetchannel/state-swift.enum/ready.md)
  The channel is able to send and receive Ethernet frames.
- [NWEthernetChannel.State.failed(_:)](nwethernetchannel/state-swift.enum/failed(_:).md)
  The channel has encountered a fatal error.
- [NWEthernetChannel.State.cancelled](nwethernetchannel/state-swift.enum/cancelled.md)
  The channel has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/state-swift.enum/setup)*