# Handling Flow Copying

**Framework**: Network Extension

Exchange data streams by using proxy-provider classes.

#### Overview

In the context of a Network Extension provider, a  is a bidirectional stream of data. A TCP flow represents a TCP connection. A UDP flow represents a sequence of incoming and outgoing datagrams you can identify based on a local IP address and port and a remote IP address and port.

 has two components: inbound and outbound data. Think of handling inbound data as reading from the remote side of the connection and writing to the local flow. Likewise, handling outbound data is comparable to reading from the local flow and writing to the remote side of the connection.

Some proxy providers may only want to flow copy for a specific set of traffic, such as only Safari flows. Starting with macOS 11,  [`NETransparentProxyProvider`](netransparentproxyprovider.md) gives the provider the option to handle the flow or let the system do it. This is the only provider you can use to do this. The only other way to limit flows claimed by the provider is to alter the `NETunnelNetworkSettings`.

When implementing a [`NEAppProxyProvider`](neappproxyprovider.md) or [`NEDNSProxyProvider`](nednsproxyprovider.md), you must deal with flows. The system calls the [`handleNewFlow(_:)`](neappproxyprovider/handlenewflow(_:).md) method for a flow that the proxy provider claims, based on network settings configured in the provider. A flow enters this method in a closed state, so returning `false` in this method indicates the flow remains closed and the system discards it.

> **Note**:  Starting with macOS 11, you can use [`NETransparentProxyProvider`](netransparentproxyprovider.md) to flow copy specific data streams.

 Starting with macOS 11, you can use [`NETransparentProxyProvider`](netransparentproxyprovider.md) to flow copy specific data streams.

##### Decide How to Handle a Flow

`NETransparentProxyProvider` gives the proxy provider the option to handle the flow or let the system do it. This means you can choose the best approach for your situation. For example, when the flow enters `handleNewFlow`, the provider logic handles the flow based on the application from which the traffic originated or the destination IP of the flow.

- To handle a desired flow, return `true` from `handleNewFlow`.
- To let the operating system handle the flow, return `false` for `NETransparentProxyProvider`.
- All other proxy providers must handle the flow if returning `true` in `handleNewFlow.`
- Returning `false` for `NEAppProxyProvider` or `NEDNSProxyProvider`, results in the flow being discarded by the system.

##### Open the Connection

Once you’ve decided how you want to handle the flow, the next step is to set up the remote side of the connection. You can decide how the provider handles the remote side of the connection, but this article assumes usage of an API such as [`NWConnection`](https://developer.apple.com/documentation/Network/NWConnection) or [`nw_connection_t`](https://developer.apple.com/documentation/Network/nw_connection_t). The steps to open the connection are:

1. Cast the original [`NEAppProxyFlow`](neappproxyflow.md) object provided from `handleNewFlow` into the transport protocol object that represents the flow the provider is going to copy. For example, if the provider flow copies TCP, use [`NEAppProxyTCPFlow`](neappproxytcpflow.md), and for UDP, use [`NEAppProxyUDPFlow`](neappproxyudpflow.md). The new `NEAppProxyTCPFlow` provides the `remoteEndpoint` object with which you set up the remote connection.
2. Open the remote connection and wait until it transitions to the [`NWConnection.State.ready`](https://developer.apple.com/documentation/Network/NWConnection/State-swift.enum/ready).
3. After the remote connection is ready, open the local flow using the `NWHostEndpoint` object to represent a local Endpoint.

##### Handle Inbound Data

When both sides of the connection move into the [`NWConnection.State.ready`](https://developer.apple.com/documentation/Network/NWConnection/State-swift.enum/ready), your next step is to define flow copying methods to read and write inbound data to both sides of the connection. Using `NWConnection` and `NEAppProxyTCPFlow` as an example, you use the following APIs, as shown in the code below:

- (Remote side) [`receive(minimumIncompleteLength:maximumLength:completion:)`](https://developer.apple.com/documentation/Network/NWConnection/receive(minimumIncompleteLength:maximumLength:completion:))
- (Flow side) [`write(_:withCompletionHandler:)`](neappproxytcpflow/write(_:withcompletionhandler:).md)

```swift
let flow: NEAppProxyTCPFlow
let connection: NWConnection

// Read from the remote connection and write to the flow.
func inboundCopier() {

    connection.receive(minimumIncompleteLength: 1, 
                       maximumLength: 2048) { (data, _, isComplete, error) in

        switch (data, isComplete, error) {
            case (let data?, _, _):
                flow.write(data) { writeError in
                    if writeError == nil {
                        // Set up another read on the remote connection if no error is present.
                        self.inboundCopier()
                    }
                }
            case (_, true, _):
                // The connection is finished; cancel the remote connection and mark flow as closed.
                connection.stateUpdateHandler = nil
                connection.cancel()
                flow.closeReadWithError(error)
                flow.closeWriteWithError(error)
            case (_, _, let error?):
                // Handle any error.
            default:
                // Handle default case.   
        }
    }
}
```

##### Handle Outbound Data

Handle outbound data as you do inbound data, by creating an outbound copier that reads from the local flow and writes to the remote connection. Using `NWConnection` and `NEAppProxyTCPFlow` once again as examples, the methods are listed here and the code is below:

- (Flow side) [`readData(completionHandler:)`](neappproxytcpflow/readdata(completionhandler:).md)
- (Remote side) `send(content:contentContext:isComplete:completion:)`

```swift
let flow: NEAppProxyTCPFlow
let connection: NWConnection

// Reads from the flow and writes to the remote connection.
func outboundCopier() {

    flow.readData { (data, error) in
        if error == nil, let readData = data, !readData.isEmpty {
            connection.send(content: readData, 
                            completion: .contentProcessed( { connectionError in
                // Handle completion success or error.
                // Set up another read if there is no error.
                if connectionError == nil {
                    self.outboundCopier()
                }
            }))
        } else {
            // Handle error case or the read that contains empty data.
        }
    }
}
```

##### Implement Flow Control

Flow control is important because it keeps the Network Extension from allocating unbounded amounts of memory that can lead to slow performance or even a , where the system frees memory by terminating applications. Such conditions can occur when a device experiences poor network conditions or large volumes of data pass through the provider. For more on a , see [`Identifying high-memory use with jetsam event reports`](https://developer.apple.com/documentation/Xcode/identifying-high-memory-use-with-jetsam-event-reports).

You can implement flow control by using an implicit technique, where all data is written before any more is read.  This prevents buffering too much data at any one time.  Buffering larger amounts of data can lead to memory problems. If the provider must buffer data, set an upper bound on the buffer and don’t read until the buffer has space to hold more data.

##### Close the Connections

When the system marks the connection as complete, the flow copying process is finished. Once finished, the flow copying process calls [`cancel()`](https://developer.apple.com/documentation/Network/NWConnection/cancel()) on the remote side of the connection, and calls [`closeReadWithError(_:)`](neappproxyflow/closereadwitherror(_:).md) and [`closeWriteWithError(_:)`](neappproxyflow/closewritewitherror(_:).md)  on the flow. Note that you need to apply the same cancellation and close process when an error takes place on either side of the connection.

## See Also

- [class NEAppProxyTCPFlow](neappproxytcpflow.md)
  An object for reading and writing data to and from a TCP connection being proxied by the provider.
- [class NEAppProxyUDPFlow](neappproxyudpflow.md)
  An object for reading and writing data to and from a UDP conversation being proxied by the provider.
- [class NEAppProxyFlow](neappproxyflow.md)
  An abstract base class shared by NEAppProxyTCPFlow and NEAppProxyUDPFlow.
- [class NEFlowMetaData](neflowmetadata.md)
  Additional information about data flowing through a per-app VPN provider.
- [In-Provider Networking](in-provider-networking.md)
  Network APIs for use by all types of NetworkExtension providers and by hotspot helpers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/handling-flow-copying)*