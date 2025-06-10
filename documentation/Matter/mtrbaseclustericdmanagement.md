# MTRBaseClusterICDManagement

**Framework**: Matter  
**Kind**: class

Cluster ICD Management

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
class MTRBaseClusterICDManagement
```

#### Overview

Allows servers to ensure that listed clients are notified when a server is available for communication.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclustericdmanagement/init(device:endpointid:queue:).md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeActiveModeDuration(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeactivemodeduration(completion:).md)
- [func readAttributeActiveModeThreshold(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeactivemodethreshold(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeattributelist(completion:).md)
- [func readAttributeClientsSupportedPerFabric(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeclientssupportedperfabric(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeclusterrevision(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeICDCounter(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeicdcounter(completion:).md)
- [func readAttributeIdleModeDuration(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeidlemodeduration(completion:).md)
- [func readAttributeMaximumCheckInBackOff(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributemaximumcheckinbackoff(completion:).md)
- [func readAttributeOperatingMode(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeoperatingmode(completion:).md)
- [func readAttributeRegisteredClients(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeregisteredclients(with:completion:).md)
- [func readAttributeUserActiveModeTriggerHint(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeuseractivemodetriggerhint(completion:).md)
- [func readAttributeUserActiveModeTriggerInstruction(completion: (String?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeuseractivemodetriggerinstruction(completion:).md)
- [func registerClient(with: MTRICDManagementClusterRegisterClientParams, completion: (MTRICDManagementClusterRegisterClientResponseParams?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/registerclient(with:completion:).md)
  Command RegisterClient
- [func stayActiveRequest(with: MTRICDManagementClusterStayActiveRequestParams, completion: (MTRICDManagementClusterStayActiveResponseParams?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/stayactiverequest(with:completion:).md)
  Command StayActiveRequest
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActiveModeDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributeactivemodeduration(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeActiveModeThreshold(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributeactivemodethreshold(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClientsSupportedPerFabric(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributeclientssupportedperfabric(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeICDCounter(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributeicdcounter(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeIdleModeDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributeidlemodeduration(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMaximumCheckInBackOff(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributemaximumcheckinbackoff(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOperatingMode(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributeoperatingmode(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRegisteredClients(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributeregisteredclients(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUserActiveModeTriggerHint(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributeuseractivemodetriggerhint(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUserActiveModeTriggerInstruction(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/subscribeattributeuseractivemodetriggerinstruction(with:subscriptionestablished:reporthandler:).md)
- [func unregisterClient(with: MTRICDManagementClusterUnregisterClientParams, completion: ((any Error)?) -> Void)](mtrbaseclustericdmanagement/unregisterclient(with:completion:).md)
  Command UnregisterClient
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeActiveModeDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeactivemodeduration(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeActiveModeThreshold(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeactivemodethreshold(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClientsSupportedPerFabric(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeclientssupportedperfabric(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeICDCounter(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeicdcounter(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeIdleModeDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeidlemodeduration(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMaximumCheckInBackOff(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributemaximumcheckinbackoff(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOperatingMode(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeoperatingmode(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeRegisteredClients(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeregisteredclients(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeUserActiveModeTriggerHint(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeuseractivemodetriggerhint(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeUserActiveModeTriggerInstruction(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclustericdmanagement/readattributeuseractivemodetriggerinstruction(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustericdmanagement)*