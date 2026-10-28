# networkInterface

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The network interface, if any, used by this flow.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var networkInterface: nw_interface_t? { get set }
```

```objc
@property (copy, nullable) nw_interface_t networkInterface;
```

## Discussion

To transport the flow’s data over a different interface, set this property to that interface.

## See Also

### Accessing flow information
- [var metaData: NEFlowMetaData](./metadata.md)
  A metadata object containing information about the source app of the flow.
- [func setMetadata(nw_parameters_t)](./setmetadata%28_%29.md)
  Sets the flow’s metadata for use by proxy providers.
- [typealias nw_parameters_t](../../Network/nw_parameters_t.md)
  An object that stores the protocols to use for connections, options for sending data, and network path constraints.
- [var isBound: Bool](./isbound.md)
  A Boolean value that indicates whether the flow has a binding to a specific interface.
- [struct nw_interface_type_t](../../Network/nw_interface_type_t.md)
  Types of network interfaces, based on their link layer media types.
- [var remoteHostname: String?](./remotehostname.md)
  The remote host name for flows created from a hostname.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflow/networkinterface)*