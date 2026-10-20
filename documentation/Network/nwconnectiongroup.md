# NWConnectionGroup

**Framework**: Network  
**Kind**: class  
**Role**: Class

An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
final class NWConnectionGroup
```

## Topics

### Establishing Group Connectivity
- [init(with: any NWGroupDescriptor, using: NWParameters)](./nwconnectiongroup/init%28with,using%29.md)
  Initializes a new connection group with a group identifier.
- [class NWMulticastGroup](./nwmulticastgroup.md)
  A descriptor for a group you use to join an IP multicast group on a local network.
- [protocol NWGroupDescriptor](./nwgroupdescriptor.md)
  A protocol that defines a group of endpoints with which you can communicate, such as a multicast group.
- [func start(queue: DispatchQueue)](./nwconnectiongroup/start%28queue%29.md)
  Joins the group, registers to receive messages, and sets the queue on you handle group events.
### Sending and Receiving Group Messages
- [func setReceiveHandler(maximumMessageSize: Int, rejectOversizedMessages: Bool, handler: ((NWConnectionGroup.Message, Data?, Bool) -> Void)?)](./nwconnectiongroup/setreceivehandler%28maximummessagesize,rejectoversizedmessages,handler%29.md)
  Sets a handler that receives inbound messages from members of the group.
- [func send(content: Data?, to: NWEndpoint?, message: NWConnectionGroup.Message, completion: (NWError?) -> Void)](./nwconnectiongroup/send%28content,to,message,completion%29.md)
  Sends data to the entire group, or to a specific member of the group.
- [NWConnectionGroup.Message](./nwconnectiongroup/message.md)
  An object that represents a message that you send or receive within a group, and that contains protocol metadata and send properties.
### Managing Groups
- [var stateUpdateHandler: ((NWConnectionGroup.State) -> Void)?](./nwconnectiongroup/stateupdatehandler.md)
  A handler that receives connection group state updates.
- [NWConnectionGroup.State](./nwconnectiongroup/state-swift.enum.md)
  States that indicate whether you can use a connection group to send and receive messages.
- [var state: NWConnectionGroup.State](./nwconnectiongroup/state-swift.property.md)
  The current state of the connection group.
- [func cancel()](./nwconnectiongroup/cancel%28%29.md)
  Cancels the connection group object and leaves the network group.
### Inspecting Groups
- [let descriptor: any NWGroupDescriptor](./nwconnectiongroup/descriptor.md)
  The descriptor of the group you use to initialize the connection group.
- [let parameters: NWParameters](./nwconnectiongroup/parameters.md)
  The parameters with which you initialize the connection group.
- [var queue: DispatchQueue?](./nwconnectiongroup/queue.md)
  The queue on which you handle group events.
### Instance Properties
- [var newConnectionHandler: ((NWConnection) -> Void)?](./nwconnectiongroup/newconnectionhandler.md)
### Instance Methods
- [func extract(connectionTo: NWEndpoint?, using: NWProtocolOptions?) -> NWConnection?](./nwconnectiongroup/extract%28connectionto,using%29.md)
- [func metadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?](./nwconnectiongroup/metadata%28definition%29.md)
- [func reinsert(connection: NWConnection) -> Bool](./nwconnectiongroup/reinsert%28connection%29.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Connections and Listeners
- [class NWConnection](./nwconnection.md)
  A bidirectional data connection between a local endpoint and a remote endpoint.
- [class NWListener](./nwlistener.md)
  An object you use to listen for incoming network connections.
- [class NWBrowser](./nwbrowser.md)
  An object you use to browse for available network services.
- [class NWEthernetChannel](./nwethernetchannel.md)
  An object you use to send and receive custom Ethernet frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnectiongroup)*