# init(on:etherType:)

**Framework**: Network  
**Kind**: init  
**Role**: Initializer

Initializes an Ethernet channel on a specific interface with a custom Ethernet type.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(on interface: NWInterface, etherType: UInt16)
```

## Parameters

- `interface`: The interface on which to send and receive Ethernet frames.
- `etherType`: The custom Ethernet frame type to register for this channel, in host-byte order.

## See Also

### Managing Ethernet Channels
- [func start(queue: DispatchQueue)](./start%28queue%29.md)
  Starts the process of registering the channel, and sets the queue on which all channel events are delivered.
- [func cancel()](./cancel%28%29.md)
  Unregisters the channel from the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/init(on:ethertype:))*