# NEAppProxyFlow

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

An abstract base class shared by NEAppProxyTCPFlow and NEAppProxyUDPFlow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class NEAppProxyFlow
```

```objc
@interface NEAppProxyFlow : NSObject
```

## Mentions

- [Handling Flow Copying](./handling-flow-copying.md)

#### Overview

App Proxy Providers receive network connections to be proxied in the form of `NEAppProxyFlow` objects, which are passed to the App Proxy Provider via the [`handleNewFlow(_:)`](./neappproxyprovider/handlenewflow%28_%29.md) method.

`NEAppProxyFlow` objects are initially in an unopened state. Before they can be used to transmit network data, they must be opened using the [`open(withLocalEndpoint:completionHandler:)`](./neappproxyflow/open%28withlocalendpoint,completionhandler%29.md) method. When you are finished with a flow, you should call [`closeReadWithError(_:)`](./neappproxyflow/closereadwitherror%28_%29.md) and [`closeWriteWithError(_:)`](./neappproxyflow/closewritewitherror%28_%29.md), and then release the `NEAppProxyFlow` object.

## Topics

### Managing the flow life cycle
- [func open(withLocalEndpoint: NWHostEndpoint?, completionHandler: ((any Error)?) -> Void)](./neappproxyflow/open%28withlocalendpoint,completionhandler%29.md)
  Opens the flow, indicating to the system that the caller is ready to start receiving and sending data.
- [func closeReadWithError((any Error)?)](./neappproxyflow/closereadwitherror%28_%29.md)
  Close the flow for further read operations.
- [func closeWriteWithError((any Error)?)](./neappproxyflow/closewritewitherror%28_%29.md)
  Close the flow for further write operations.
### Accessing flow information
- [var metaData: NEFlowMetaData](./neappproxyflow/metadata.md)
  A metadata object containing information about the source app of the flow.
- [func setMetadata(nw_parameters_t)](./neappproxyflow/setmetadata%28_%29.md)
  Sets the flow’s metadata for use by proxy providers.
- [typealias nw_parameters_t](../Network/nw_parameters_t.md)
  An object that stores the protocols to use for connections, options for sending data, and network path constraints.
- [var isBound: Bool](./neappproxyflow/isbound.md)
  A Boolean value that indicates whether the flow has a binding to a specific interface.
- [var networkInterface: nw_interface_t?](./neappproxyflow/networkinterface.md)
  The network interface, if any, used by this flow.
- [struct nw_interface_type_t](../Network/nw_interface_type_t.md)
  Types of network interfaces, based on their link layer media types.
- [var remoteHostname: String?](./neappproxyflow/remotehostname.md)
  The remote host name for flows created from a hostname.
### Errors
- [struct NEAppProxyFlowError](./neappproxyflowerror-swift.struct.md)
  An error that the app proxy flow encounters.
- [let NEAppProxyErrorDomain: String](./neappproxyerrordomain.md)
  The domain used for app proxy errors.
- [NEAppProxyFlowError.Code](./neappproxyflowerror-swift.struct/code.md)
  Error codes that the app proxy flow API declares.
- [struct NEAppProxyFlowError](./neappproxyflowerror-swift.struct.md)
  An error that the app proxy flow encounters.
### Instance Properties
- [var interface: NWInterface?](./neappproxyflow/interface.md)
### Instance Methods
- [func open(withLocalFlowEndpoint: NWEndpoint?) async throws](./neappproxyflow/open%28withlocalflowendpoint%29.md)
- [func open(withLocalFlowEndpoint: NWEndpoint?, completionHandler: ((any Error)?) -> Void)](./neappproxyflow/open%28withlocalflowendpoint,completionhandler%29.md)
- [func setMetadata(on: NWParameters)](./neappproxyflow/setmetadata%28on%29.md)
- [- openWithLocalFlowEndpoint:completionHandler:](./neappproxyflow/openwithlocalflowendpoint_completionhandler_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NEAppProxyTCPFlow](./neappproxytcpflow.md)
- [NEAppProxyUDPFlow](./neappproxyudpflow.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Flow handling
- [class NEAppProxyTCPFlow](./neappproxytcpflow.md)
  An object for reading and writing data to and from a TCP connection being proxied by the provider.
- [class NEAppProxyUDPFlow](./neappproxyudpflow.md)
  An object for reading and writing data to and from a UDP conversation being proxied by the provider.
- [class NEFlowMetaData](./neflowmetadata.md)
  Additional information about data flowing through a per-app VPN provider.
- [In-Provider Networking](./in-provider-networking.md)
  Network APIs for use by all types of NetworkExtension providers and by hotspot helpers.
- [Handling Flow Copying](./handling-flow-copying.md)
  Exchange data streams by using proxy-provider classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflow)*