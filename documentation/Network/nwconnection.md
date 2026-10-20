# NWConnection

**Framework**: Network  
**Kind**: class  
**Role**: Class

A bidirectional data connection between a local endpoint and a remote endpoint.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
final class NWConnection
```

## Mentions

- [Inspecting app activity data](./inspecting-app-activity-data.md)

## Topics

### Creating Connections
- [convenience init(host: NWEndpoint.Host, port: NWEndpoint.Port, using: NWParameters)](./nwconnection/init%28host,port,using%29.md)
  Initializes a new connection to a host and port.
- [init(to: NWEndpoint, using: NWParameters)](./nwconnection/init%28to,using%29.md)
  Initializes a new connection to a remote endpoint.
- [func start(queue: DispatchQueue)](./nwconnection/start%28queue%29.md)
  Starts establishing a connection, and sets the queue on which to deliver all connection events.
- [func restart()](./nwconnection/restart%28%29.md)
  Restarts a connection that is in the waiting state.
### Handling State Updates
- [var state: NWConnection.State](./nwconnection/state-swift.property.md)
  The current state of the connection.
- [NWConnection.State](./nwconnection/state-swift.enum.md)
  States indicating whether a connection can be used to send and receive data.
- [var stateUpdateHandler: ((NWConnection.State) -> Void)?](./nwconnection/stateupdatehandler.md)
  A handler that receives connection state updates.
### Sending and Receiving Data
- [func send(content: Data?, contentContext: NWConnection.ContentContext, isComplete: Bool, completion: NWConnection.SendCompletion)](./nwconnection/send%28content,contentcontext,iscomplete,completion%29-5ecuz.md)
  Sends data on a connection.
- [func send<Content>(content: Content?, contentContext: NWConnection.ContentContext, isComplete: Bool, completion: NWConnection.SendCompletion)](./nwconnection/send%28content,contentcontext,iscomplete,completion%29-3mfmt.md)
  Sends data on a connection using a custom Data type.
- [NWConnection.SendCompletion](./nwconnection/sendcompletion.md)
  A completion handler that indicates when the connection has finished processing sent content.
- [func receive(minimumIncompleteLength: Int, maximumLength: Int, completion: (Data?, NWConnection.ContentContext?, Bool, NWError?) -> Void)](./nwconnection/receive%28minimumincompletelength,maximumlength,completion%29.md)
  Schedules a single receive completion handler, with a range indicating how many bytes the handler can receive at one time.
- [func receiveMessage(completion: (Data?, NWConnection.ContentContext?, Bool, NWError?) -> Void)](./nwconnection/receivemessage%28completion%29.md)
  Schedules a single receive completion handler for a complete message, as opposed to a range of bytes.
- [func batch(() -> Void)](./nwconnection/batch%28_%29.md)
  Defines a block in which calls to send and receive are processed as a batch to improve performance.
- [NWConnection.ContentContext](./nwconnection/contentcontext.md)
  An object that represents a message to send or receive, containing protocol metadata and send properties.
- [var maximumDatagramSize: Int](./nwconnection/maximumdatagramsize.md)
  The maximum size of a datagram message that can be sent on a connection.
### Canceling Connections
- [func cancel()](./nwconnection/cancel%28%29.md)
  Cancels the connection and gracefully disconnects any established network protocols.
- [func forceCancel()](./nwconnection/forcecancel%28%29.md)
  Cancels the connection and immediately disconnects any established network protocols.
- [func cancelCurrentEndpoint()](./nwconnection/cancelcurrentendpoint%28%29.md)
  Causes the current endpoint to be rejected, allowing the connection to try another resolved address.
### Handling Path Updates
- [var currentPath: NWPath?](./nwconnection/currentpath.md)
  The network path the connection is using.
- [var pathUpdateHandler: ((NWPath) -> Void)?](./nwconnection/pathupdatehandler.md)
  A handler that receives network path updates.
- [var viabilityUpdateHandler: ((Bool) -> Void)?](./nwconnection/viabilityupdatehandler.md)
  A handler that receives updates when data can be sent and received.
- [var betterPathUpdateHandler: ((Bool) -> Void)?](./nwconnection/betterpathupdatehandler.md)
  A handler that receives updates when an alternative network path is preferred over the current path.
### Collecting Connection Metrics
- [Collecting Network Connection Metrics](./collecting-network-connection-metrics.md)
  Use reports to understand how DNS and protocol handshakes impact connection establishment.
- [func requestEstablishmentReport(queue: DispatchQueue, completion: (NWConnection.EstablishmentReport?) -> Void)](./nwconnection/requestestablishmentreport%28queue,completion%29.md)
  Requests a copy of the connection’s establishment report once the connection is in the ready state.
- [NWConnection.EstablishmentReport](./nwconnection/establishmentreport.md)
  A report that provides metrics about the establishment of a connection.
- [func startDataTransferReport() -> NWConnection.PendingDataTransferReport](./nwconnection/startdatatransferreport%28%29.md)
  Begins a new data transfer report, which can later be collected.
- [NWConnection.PendingDataTransferReport](./nwconnection/pendingdatatransferreport.md)
  An outstanding data transfer report that has yet to be collected.
- [NWConnection.DataTransferReport](./nwconnection/datatransferreport.md)
  A report that provides metrics about data being sent and received on a connection.
### Inspecting Connections
- [func metadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?](./nwconnection/metadata%28definition%29.md)
  Retrieves the connection-wide metadata for a specific protocol.
- [class NWProtocolMetadata](./nwprotocolmetadata.md)
  The abstract superclass for specifying metadata about a network protocol.
- [let endpoint: NWEndpoint](./nwconnection/endpoint.md)
  The remote endpoint with which the connection was initialized.
- [let parameters: NWParameters](./nwconnection/parameters.md)
  The parameters with which the connection was initialized.
- [var queue: DispatchQueue?](./nwconnection/queue.md)
  The queue on which connection events are delivered.
### Initializers
- [convenience init?(from: NWConnectionGroup, to: NWEndpoint?, using: NWProtocolOptions?)](./nwconnection/init%28from,to,using%29.md)
- [convenience init?(message: NWConnectionGroup.Message)](./nwconnection/init%28message%29.md)
### Instance Methods
- [func receiveDiscontiguous(minimumIncompleteLength: Int, maximumLength: Int, completion: (DispatchData?, NWConnection.ContentContext?, Bool, NWError?) -> Void)](./nwconnection/receivediscontiguous%28minimumincompletelength,maximumlength,completion%29.md)
- [func receiveMessageDiscontiguous(completion: (DispatchData?, NWConnection.ContentContext?, Bool, NWError?) -> Void)](./nwconnection/receivemessagediscontiguous%28completion%29.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Connections and Listeners
- [class NWListener](./nwlistener.md)
  An object you use to listen for incoming network connections.
- [class NWBrowser](./nwbrowser.md)
  An object you use to browse for available network services.
- [class NWConnectionGroup](./nwconnectiongroup.md)
  An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- [class NWEthernetChannel](./nwethernetchannel.md)
  An object you use to send and receive custom Ethernet frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection)*