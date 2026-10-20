# MTRClusterCommissionerControl

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Commissioner Control Supports the ability for clients to request the commissioning of themselves or other nodes onto a fabric which the cluster server can commission onto.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class MTRClusterCommissionerControl
```

```objc
@interface MTRClusterCommissionerControl : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustercommissionercontrol/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func commissionNode(with: MTRCommissionerControlClusterCommissionNodeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRCommissionerControlClusterReverseOpenCommissioningWindowParams?, (any Error)?) -> Void)](./mtrclustercommissionercontrol/commissionnode%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustercommissionercontrol/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustercommissionercontrol/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustercommissionercontrol/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustercommissionercontrol/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustercommissionercontrol/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeSupportedDeviceCategories(with: MTRReadParams?) -> [String : Any]?](./mtrclustercommissionercontrol/readattributesupporteddevicecategories%28with%29.md)
- [func requestCommissioningApproval(with: MTRCommissionerControlClusterRequestCommissioningApprovalParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercommissionercontrol/requestcommissioningapproval%28with,expectedvalues,expectedvalueinterval,completion%29.md)

## Relationships

### Inherits From
- [MTRGenericCluster](./mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustercommissionercontrol)*