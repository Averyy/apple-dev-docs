# priority

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A property that gives you a hint about how to send a given data instance over the network.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var priority: ARSession.CollaborationData.Priority { get }
```

```objc
@property (nonatomic, readonly) ARCollaborationDataPriority priority;
```

## Discussion

If you have reliability options in the network protocol you choose to transport [`ARSession.CollaborationData`](../collaborationdata.md) among peers, the [`priority`](./priority-swift.property.md) property gives you a hint about which reliability option to choose for a given collaboration data instance. For example, if you use MultipeerConnectivity to send collaboration data over the network, choose [`MCSessionSendDataMode.reliable`](../../../MultipeerConnectivity/mcsessionsenddatamode/reliable.md) when calling [`send(_:toPeers:with:)`](../../../MultipeerConnectivity/mcsession/send%28_,topeers,with%29.md) after ARKit gives you a collaboration data instance with priority [`ARSession.CollaborationData.Priority.critical`](./priority-swift.enum/critical.md).

## See Also

### Observing Priority
- [ARSession.CollaborationData.Priority](./priority-swift.enum.md)
  Options that help you choose the appropriate network protocol or settings for a given data instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/collaborationdata/priority-swift.property)*