# start(queue:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Starts the process of registering the channel, and sets the queue on which all channel events are delivered.

**Availability**:
- macOS 10.15+

## Declaration

```swift
final func start(queue: DispatchQueue)
```

## See Also

### Managing Ethernet Channels
- [init(on: NWInterface, etherType: UInt16)](./init%28on,ethertype%29.md)
  Initializes an Ethernet channel on a specific interface with a custom Ethernet type.
- [func cancel()](./cancel%28%29.md)
  Unregisters the channel from the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/start(queue:))*