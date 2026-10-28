# nw_ethernet_channel_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

An object you use to send and receive custom Ethernet frames.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias nw_ethernet_channel_t = any OS_nw_ethernet_channel
```

```c
typedef NSObject<OS_nw_ethernet_channel> * nw_ethernet_channel_t;
```

## Discussion

Use Ethernet channels to send and receive custom Ethernet frame types over an interface.

Creating Ethernet channels requires the `com.apple.developer.networking.custom-protocol` entitlement.

## Topics

### Managing Ethernet Channels
- [func nw_ethernet_channel_create(UInt16, nw_interface_t) -> nw_ethernet_channel_t](./nw_ethernet_channel_create%28_,_%29.md)
  Initializes an Ethernet channel on a specific interface with a custom Ethernet type.
- [func nw_ethernet_channel_set_queue(nw_ethernet_channel_t, dispatch_queue_t)](./nw_ethernet_channel_set_queue%28_,_%29.md)
  Sets the queue on which all channel events are delivered.
- [func nw_ethernet_channel_start(nw_ethernet_channel_t)](./nw_ethernet_channel_start%28_%29.md)
  Starts the process of registering the channel.
- [func nw_ethernet_channel_cancel(nw_ethernet_channel_t)](./nw_ethernet_channel_cancel%28_%29.md)
  Unregisters the channel from the interface.
### Handling State Updates
- [func nw_ethernet_channel_set_state_changed_handler(nw_ethernet_channel_t, nw_ethernet_channel_state_changed_handler_t?)](./nw_ethernet_channel_set_state_changed_handler%28_,_%29.md)
  Sets a handler to receive channel state updates.
- [typealias nw_ethernet_channel_state_changed_handler_t](./nw_ethernet_channel_state_changed_handler_t.md)
  A handler that delivers Ethernet channel state updates with associated errors.
- [struct nw_ethernet_channel_state_t](./nw_ethernet_channel_state_t.md)
  States indicating whether an Ethernet channel is able to send and receive frames.
### Sending and Receiving Ethernet Frames
- [func nw_ethernet_channel_send(nw_ethernet_channel_t, dispatch_data_t, UInt16, UnsafeMutablePointer<UInt8>, nw_ethernet_channel_send_completion_t)](./nw_ethernet_channel_send%28_,_,_,_,_%29.md)
  Sends a single Ethernet frame over a channel to a specific Ethernet address.
- [typealias nw_ethernet_channel_send_completion_t](./nw_ethernet_channel_send_completion_t.md)
  A handler that indicates when an Ethernet frame has been sent, or if an error was encountered.
- [func nw_ethernet_channel_set_receive_handler(nw_ethernet_channel_t, nw_ethernet_channel_receive_handler_t?)](./nw_ethernet_channel_set_receive_handler%28_,_%29.md)
  Sets a handler to receive inbound Ethernet frames.
- [typealias nw_ethernet_channel_receive_handler_t](./nw_ethernet_channel_receive_handler_t.md)
  A handler that delivers inbound Ethernet frames.
- [typealias nw_ethernet_address_t](./nw_ethernet_address_t.md)
  A 48-bit Ethernet address.

## See Also

### Connections and Listeners
- [Implementing netcat with Network Framework](./implementing-netcat-with-network-framework.md)
  Build a simple `netcat` tool that establishes network connections and transfers data.
- [nw_connection_t](./nw_connection_t.md)
  A bidirectional data connection between a local endpoint and a remote endpoint.
- [nw_listener_t](./nw_listener_t.md)
  An object you use to listen for incoming network connections.
- [nw_browser_t](./nw_browser_t.md)
  An object you use to browse for available network services.
- [nw_connection_group_t](./nw_connection_group_t.md)
  An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_ethernet_channel_t)*