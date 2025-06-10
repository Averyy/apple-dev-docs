# NWEthernetChannel

**Framework**: Network  
**Kind**: class

An object you use to send and receive custom Ethernet frames.

**Availability**:
- macOS 10.15+

## Declaration

```swift
final class NWEthernetChannel
```

#### Overview

Use Ethernet channels to send and receive custom Ethernet frame types over an interface.

Creating Ethernet channels requires the `com.apple.developer.networking.custom-protocol` entitlement.

## Topics

### Managing Ethernet Channels
- [init(on: NWInterface, etherType: UInt16)](nwethernetchannel/init(on:ethertype:).md)
  Initializes an Ethernet channel on a specific interface with a custom Ethernet type.
- [func start(queue: DispatchQueue)](nwethernetchannel/start(queue:).md)
  Starts the process of registering the channel, and sets the queue on which all channel events are delivered.
- [func cancel()](nwethernetchannel/cancel.md)
  Unregisters the channel from the interface.
### Handling State Updates
- [var state: NWEthernetChannel.State](nwethernetchannel/state-swift.property.md)
  The current state of the channel.
- [NWEthernetChannel.State](nwethernetchannel/state-swift.enum.md)
  States indicating whether an Ethernet channel is able to send and receive frames.
- [var stateUpdateHandler: ((NWEthernetChannel.State) -> Void)?](nwethernetchannel/stateupdatehandler.md)
  A handler that delivers channel state updates.
### Sending and Receiving Ethernet Frames
- [func send(content: Data, to: NWEthernetChannel.EthernetAddress, vlanTag: UInt16, completion: (NWError?) -> Void)](nwethernetchannel/send(content:to:vlantag:completion:).md)
  Sends a single Ethernet frame over a channel to a specific Ethernet address.
- [var receiveHandler: ((Data, UInt16, NWEthernetChannel.EthernetAddress, NWEthernetChannel.EthernetAddress) -> Void)?](nwethernetchannel/receivehandler.md)
  A handler that delivers inbound Ethernet frames.
- [NWEthernetChannel.EthernetAddress](nwethernetchannel/ethernetaddress.md)
  A 48-bit Ethernet address.
### Inspecting Ethernet Channels
- [let etherType: UInt16](nwethernetchannel/ethertype.md)
  The custom Ethernet type with which the channel was initialized.
- [let interface: NWInterface](nwethernetchannel/interface.md)
  The interface with which the channel was initialized.
- [var queue: DispatchQueue?](nwethernetchannel/queue.md)
  The queue on which channel events will be delivered.
### Initializers
- [init(on: NWInterface, etherType: UInt16, parameters: NWParameters)](nwethernetchannel/init(on:ethertype:parameters:).md)
### Instance Properties
- [var maximumPayloadSize: Int](nwethernetchannel/maximumpayloadsize.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NWConnection](nwconnection.md)
  A bidirectional data connection between a local endpoint and a remote endpoint.
- [class NWListener](nwlistener.md)
  An object you use to listen for incoming network connections.
- [class NWBrowser](nwbrowser.md)
  An object you use to browse for available network services.
- [class NWConnectionGroup](nwconnectiongroup.md)
  An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel)*