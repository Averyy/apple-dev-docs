# MTRBaseClusterThreadBorderRouterManagement

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Thread Border Router Management

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
class MTRBaseClusterThreadBorderRouterManagement
```

```objc
@interface MTRBaseClusterThreadBorderRouterManagement : MTRGenericBaseCluster
```

#### Overview

Manage the Thread network of Thread Border Router

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterthreadborderroutermanagement/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func getActiveDatasetRequest(completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/getactivedatasetrequest%28completion%29.md)
- [func getActiveDatasetRequest(with: MTRThreadBorderRouterManagementClusterGetActiveDatasetRequestParams?, completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/getactivedatasetrequest%28with,completion%29.md)
  Command GetActiveDatasetRequest
- [func getPendingDatasetRequest(completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/getpendingdatasetrequest%28completion%29.md)
- [func getPendingDatasetRequest(with: MTRThreadBorderRouterManagementClusterGetPendingDatasetRequestParams?, completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/getpendingdatasetrequest%28with,completion%29.md)
  Command GetPendingDatasetRequest
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeActiveDatasetTimestamp(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeactivedatasettimestamp%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeattributelist%28completion%29.md)
- [func readAttributeBorderAgentID(completion: (Data?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeborderagentid%28completion%29.md)
- [func readAttributeBorderRouterName(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeborderroutername%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeclusterrevision%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeInterfaceEnabled(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeinterfaceenabled%28completion%29.md)
- [func readAttributePendingDatasetTimestamp(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributependingdatasettimestamp%28completion%29.md)
- [func readAttributeThreadVersion(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributethreadversion%28completion%29.md)
- [func setActiveDatasetRequestWith(MTRThreadBorderRouterManagementClusterSetActiveDatasetRequestParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/setactivedatasetrequestwith%28_,completion%29.md)
  Command SetActiveDatasetRequest
- [func setPendingDatasetRequestWith(MTRThreadBorderRouterManagementClusterSetPendingDatasetRequestParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/setpendingdatasetrequestwith%28_,completion%29.md)
  Command SetPendingDatasetRequest
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActiveDatasetTimestamp(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/subscribeattributeactivedatasettimestamp%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBorderAgentID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (Data?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/subscribeattributeborderagentid%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeBorderRouterName(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/subscribeattributeborderroutername%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeInterfaceEnabled(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/subscribeattributeinterfaceenabled%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePendingDatasetTimestamp(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/subscribeattributependingdatasettimestamp%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeThreadVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/subscribeattributethreadversion%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeActiveDatasetTimestamp(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeactivedatasettimestamp%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBorderAgentID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (Data?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeborderagentid%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeBorderRouterName(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeborderroutername%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeInterfaceEnabled(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributeinterfaceenabled%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePendingDatasetTimestamp(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributependingdatasettimestamp%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeThreadVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterthreadborderroutermanagement/readattributethreadversion%28withclusterstatecache,endpoint,queue,completion%29.md)

## Relationships

### Inherits From
- [MTRGenericBaseCluster](./mtrgenericbasecluster.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadborderroutermanagement)*