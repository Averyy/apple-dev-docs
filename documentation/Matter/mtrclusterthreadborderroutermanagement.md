# MTRClusterThreadBorderRouterManagement

**Framework**: Matter  
**Kind**: class

Cluster Thread Border Router Management Manage the Thread network of Thread Border Router

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
class MTRClusterThreadBorderRouterManagement
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterthreadborderroutermanagement/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func getActiveDatasetRequest(with: MTRThreadBorderRouterManagementClusterGetActiveDatasetRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](mtrclusterthreadborderroutermanagement/getactivedatasetrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func getActiveDatasetRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](mtrclusterthreadborderroutermanagement/getactivedatasetrequest(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func getPendingDatasetRequest(with: MTRThreadBorderRouterManagementClusterGetPendingDatasetRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](mtrclusterthreadborderroutermanagement/getpendingdatasetrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func getPendingDatasetRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](mtrclusterthreadborderroutermanagement/getpendingdatasetrequest(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadborderroutermanagement/readattributeacceptedcommandlist(with:).md)
- [func readAttributeActiveDatasetTimestamp(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadborderroutermanagement/readattributeactivedatasettimestamp(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadborderroutermanagement/readattributeattributelist(with:).md)
- [func readAttributeBorderAgentID(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadborderroutermanagement/readattributeborderagentid(with:).md)
- [func readAttributeBorderRouterName(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadborderroutermanagement/readattributeborderroutername(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadborderroutermanagement/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadborderroutermanagement/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadborderroutermanagement/readattributegeneratedcommandlist(with:).md)
- [func readAttributeInterfaceEnabled(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadborderroutermanagement/readattributeinterfaceenabled(with:).md)
- [func readAttributePendingDatasetTimestamp(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadborderroutermanagement/readattributependingdatasettimestamp(with:).md)
- [func readAttributeThreadVersion(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadborderroutermanagement/readattributethreadversion(with:).md)
- [func setActiveDatasetRequestWith(MTRThreadBorderRouterManagementClusterSetActiveDatasetRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterthreadborderroutermanagement/setactivedatasetrequestwith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func setPendingDatasetRequestWith(MTRThreadBorderRouterManagementClusterSetPendingDatasetRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterthreadborderroutermanagement/setpendingdatasetrequestwith(_:expectedvalues:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterthreadborderroutermanagement)*