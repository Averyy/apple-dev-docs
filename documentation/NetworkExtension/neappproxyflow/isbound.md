# isBound

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the flow has a binding to a specific interface.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- macOS 11.1+
- visionOS 1.0+

## Declaration

```swift
var isBound: Bool { get }
```

```objc
@property (readonly) BOOL isBound;
```

#### Discussion

When a binding exists, this value is [`true`](../../Swift/true.md), and the [`networkInterface`](./networkinterface.md) property indicates the bound interface. If the flow isn’t bound to an interface, this value is [`false`](../../Swift/false.md).

## See Also

### Accessing flow information
- [var metaData: NEFlowMetaData](./metadata.md)
  A metadata object containing information about the source app of the flow.
- [func setMetadata(nw_parameters_t)](./setmetadata%28_%29.md)
  Sets the flow’s metadata for use by proxy providers.
- [typealias nw_parameters_t](../../Network/nw_parameters_t.md)
  An object that stores the protocols to use for connections, options for sending data, and network path constraints.
- [var networkInterface: nw_interface_t?](./networkinterface.md)
  The network interface, if any, used by this flow.
- [struct nw_interface_type_t](../../Network/nw_interface_type_t.md)
  Types of network interfaces, based on their link layer media types.
- [var remoteHostname: String?](./remotehostname.md)
  The remote host name for flows created from a hostname.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyflow/isbound)*