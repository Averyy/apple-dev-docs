# metaData

**Framework**: Network Extension  
**Kind**: property

A metadata object containing information about the source app of the flow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var metaData: NEFlowMetaData { get }
```

## See Also

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
- [var remoteHostname: String?](neappproxyflow/remotehostname.md)
  The remote host name for flows created from a hostname.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflow/metadata)*