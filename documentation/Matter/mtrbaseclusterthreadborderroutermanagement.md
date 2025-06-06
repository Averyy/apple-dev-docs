# MTRBaseClusterThreadBorderRouterManagement

**Framework**: Matter  
**Kind**: class

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

#### Overview

Manage the Thread network of Thread Border Router

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterthreadborderroutermanagement/init(device:endpointid:queue:).md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func getActiveDatasetRequest(completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/getactivedatasetrequest(completion:).md)
- [func getActiveDatasetRequest(with: MTRThreadBorderRouterManagementClusterGetActiveDatasetRequestParams?, completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/getactivedatasetrequest(with:completion:).md)
  Command GetActiveDatasetRequest
- [func getPendingDatasetRequest(completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/getpendingdatasetrequest(completion:).md)
- [func getPendingDatasetRequest(with: MTRThreadBorderRouterManagementClusterGetPendingDatasetRequestParams?, completion: (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/getpendingdatasetrequest(with:completion:).md)
  Command GetPendingDatasetRequest
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeActiveDatasetTimestamp(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeactivedatasettimestamp(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeattributelist(completion:).md)
- [func readAttributeBorderAgentID(completion: (Data?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeborderagentid(completion:).md)
- [func readAttributeBorderRouterName(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeborderroutername(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeclusterrevision(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeInterfaceEnabled(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeinterfaceenabled(completion:).md)
- [func readAttributePendingDatasetTimestamp(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributependingdatasettimestamp(completion:).md)
- [func readAttributeThreadVersion(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributethreadversion(completion:).md)
- [func setActiveDatasetRequestWith(MTRThreadBorderRouterManagementClusterSetActiveDatasetRequestParams, completion: MTRStatusCompletion)](mtrbaseclusterthreadborderroutermanagement/setactivedatasetrequestwith(_:completion:).md)
  Command SetActiveDatasetRequest
- [func setPendingDatasetRequestWith(MTRThreadBorderRouterManagementClusterSetPendingDatasetRequestParams, completion: MTRStatusCompletion)](mtrbaseclusterthreadborderroutermanagement/setpendingdatasetrequestwith(_:completion:).md)
  Command SetPendingDatasetRequest
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActiveDatasetTimestamp(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/subscribeattributeactivedatasettimestamp(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBorderAgentID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (Data?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/subscribeattributeborderagentid(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeBorderRouterName(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/subscribeattributeborderroutername(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeInterfaceEnabled(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/subscribeattributeinterfaceenabled(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePendingDatasetTimestamp(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/subscribeattributependingdatasettimestamp(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeThreadVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/subscribeattributethreadversion(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeActiveDatasetTimestamp(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeactivedatasettimestamp(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBorderAgentID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (Data?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeborderagentid(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeBorderRouterName(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeborderroutername(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeInterfaceEnabled(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributeinterfaceenabled(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePendingDatasetTimestamp(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributependingdatasettimestamp(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeThreadVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterthreadborderroutermanagement/readattributethreadversion(withclusterstatecache:endpoint:queue:completion:).md)

## Relationships

### Inherits From
- [MTRGenericBaseCluster](mtrgenericbasecluster.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadborderroutermanagement)*