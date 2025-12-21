# setMetadata(_:)

**Framework**: Network Extension  
**Kind**: method

Sets the flow’s metadata for use by proxy providers.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
func setMetadata(_ parameters: nw_parameters_t)
```

#### Discussion

Use an [`nw_parameters_t`](https://developer.apple.com/documentation/Network/nw_parameters_t) object to create a connection that transparently proxies the flow’s data. This also provides accurate source app information to any subsequent [`NEAppProxyProvider`](neappproxyprovider.md) instances that transparently proxy the flow.

## Parameters

- `parameters`: A nw_parameters_t object that contains the flow metadata.

## See Also

- [var metaData: NEFlowMetaData](neappproxyflow/metadata.md)
  A metadata object containing information about the source app of the flow.
- [typealias nw_parameters_t](../Network/nw_parameters_t.md)
  An object that stores the protocols to use for connections, options for sending data, and network path constraints.
- [var isBound: Bool](neappproxyflow/isbound.md)
  A Boolean value that indicates whether the flow has a binding to a specific interface.
- [var networkInterface: nw_interface_t?](neappproxyflow/networkinterface.md)
  The network interface, if any, used by this flow.
- [struct nw_interface_type_t](../Network/nw_interface_type_t.md)
  Types of network interfaces, based on their link layer media types.
- [var remoteHostname: String?](neappproxyflow/remotehostname.md)
  The remote host name for flows created from a hostname.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflow/setmetadata(_:))*