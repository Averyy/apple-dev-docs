# cancel()

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Unregisters the channel from the interface.

**Availability**:
- macOS 10.15+

## Declaration

```swift
final func cancel()
```

## See Also

### Managing Ethernet Channels
- [init(on: NWInterface, etherType: UInt16)](./init%28on,ethertype%29.md)
  Initializes an Ethernet channel on a specific interface with a custom Ethernet type.
- [func start(queue: DispatchQueue)](./start%28queue%29.md)
  Starts the process of registering the channel, and sets the queue on which all channel events are delivered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/cancel())*