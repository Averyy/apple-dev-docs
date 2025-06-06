# MTRClusterCommissionerControl

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustercommissionercontrol/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func commissionNode(with: MTRCommissionerControlClusterCommissionNodeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRCommissionerControlClusterReverseOpenCommissioningWindowParams?, (any Error)?) -> Void)](mtrclustercommissionercontrol/commissionnode(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustercommissionercontrol/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustercommissionercontrol/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustercommissionercontrol/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustercommissionercontrol/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustercommissionercontrol/readattributegeneratedcommandlist(with:).md)
- [func readAttributeSupportedDeviceCategories(with: MTRReadParams?) -> [String : Any]?](mtrclustercommissionercontrol/readattributesupporteddevicecategories(with:).md)
- [func requestCommissioningApproval(with: MTRCommissionerControlClusterRequestCommissioningApprovalParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustercommissionercontrol/requestcommissioningapproval(with:expectedvalues:expectedvalueinterval:completion:).md)

## Relationships

### Inherits From
- [MTRGenericCluster](mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustercommissionercontrol)*