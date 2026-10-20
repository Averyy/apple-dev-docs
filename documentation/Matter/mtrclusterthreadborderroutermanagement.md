# MTRClusterThreadBorderRouterManagement

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterThreadBorderRouterManagement : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterthreadborderroutermanagement/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func getActiveDatasetRequest(with: MTRThreadBorderRouterManagementClusterGetActiveDatasetRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](./mtrclusterthreadborderroutermanagement/getactivedatasetrequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getActiveDatasetRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](./mtrclusterthreadborderroutermanagement/getactivedatasetrequest%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func getPendingDatasetRequest(with: MTRThreadBorderRouterManagementClusterGetPendingDatasetRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](./mtrclusterthreadborderroutermanagement/getpendingdatasetrequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getPendingDatasetRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](./mtrclusterthreadborderroutermanagement/getpendingdatasetrequest%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadborderroutermanagement/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeActiveDatasetTimestamp(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadborderroutermanagement/readattributeactivedatasettimestamp%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadborderroutermanagement/readattributeattributelist%28with%29.md)
- [func readAttributeBorderAgentID(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadborderroutermanagement/readattributeborderagentid%28with%29.md)
- [func readAttributeBorderRouterName(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadborderroutermanagement/readattributeborderroutername%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadborderroutermanagement/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadborderroutermanagement/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadborderroutermanagement/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeInterfaceEnabled(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadborderroutermanagement/readattributeinterfaceenabled%28with%29.md)
- [func readAttributePendingDatasetTimestamp(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadborderroutermanagement/readattributependingdatasettimestamp%28with%29.md)
- [func readAttributeThreadVersion(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadborderroutermanagement/readattributethreadversion%28with%29.md)
- [func setActiveDatasetRequestWith(MTRThreadBorderRouterManagementClusterSetActiveDatasetRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterthreadborderroutermanagement/setactivedatasetrequestwith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setPendingDatasetRequestWith(MTRThreadBorderRouterManagementClusterSetPendingDatasetRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterthreadborderroutermanagement/setpendingdatasetrequestwith%28_,expectedvalues,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterthreadborderroutermanagement)*