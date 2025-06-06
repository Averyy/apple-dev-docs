# remoteHostname

**Framework**: Network Extension  
**Kind**: property

The remote host name for flows created from a hostname.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- Mac Catalyst 14.2+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var remoteHostname: String? { get }
```

#### Discussion

The flow populates this property when you create the flow from a connect-by-name API such as [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) or the [`Network`](https://developer.apple.com/documentation/Network) framework.

## See Also

- [var metaData: NEFlowMetaData](neappproxyflow/metadata.md)
  A metadata object containing information about the source app of the flow.
- [func setMetadata(nw_parameters_t)](neappproxyflow/setmetadata(_:).md)
  Sets the flow’s metadata for use by proxy providers.
- [typealias nw_parameters_t = any OS_nw_parameters](../Network/nw_parameters_t.md)
  An object that stores the protocols to use for connections, options for sending data, and network path constraints.
- [var isBound: Bool](neappproxyflow/isbound.md)
  A Boolean value that indicates whether the flow has a binding to a specific interface.
- [var networkInterface: nw_interface_t?](neappproxyflow/networkinterface.md)
  The network interface, if any, used by this flow.
- [struct nw_interface_type_t](../Network/nw_interface_type_t.md)
  Types of network interfaces, based on their link layer media types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflow/remotehostname)*