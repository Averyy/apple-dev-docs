# start(queue:)

**Framework**: Network  
**Kind**: method

Starts the process of registering the channel, and sets the queue on which all channel events are delivered.

**Availability**:
- macOS 10.15+

## Declaration

```swift
final func start(queue: DispatchQueue)
```

## See Also

- [init(on: NWInterface, etherType: UInt16)](nwethernetchannel/init(on:ethertype:).md)
  Initializes an Ethernet channel on a specific interface with a custom Ethernet type.
- [func cancel()](nwethernetchannel/cancel.md)
  Unregisters the channel from the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/start(queue:))*