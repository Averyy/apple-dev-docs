# priority

**Framework**: ARKit  
**Kind**: property

A property that gives you a hint about how to send a given data instance over the network.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var priority: ARSession.CollaborationData.Priority { get }
```

#### Discussion

If you have reliability options in the network protocol you choose to transport [`ARSession.CollaborationData`](arsession/collaborationdata.md) among peers, the [`priority`](arsession/collaborationdata/priority-swift.property.md) property gives you a hint about which reliability option to choose for a given collaboration data instance. For example, if you use MultipeerConnectivity to send collaboration data over the network, choose [`MCSessionSendDataMode.reliable`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSessionSendDataMode/reliable) when calling [`send(_:toPeers:with:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/send(_:toPeers:with:)) after ARKit gives you a collaboration data instance with priority [`ARSession.CollaborationData.Priority.critical`](arsession/collaborationdata/priority-swift.enum/critical.md).

## See Also

- [ARSession.CollaborationData.Priority](arsession/collaborationdata/priority-swift.enum.md)
  Options that help you choose the appropriate network protocol or settings for a given data instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/collaborationdata/priority-swift.property)*