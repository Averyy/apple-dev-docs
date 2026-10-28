# MTRBaseClusterICDManagement

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRBaseClusterICDManagement : MTRGenericBaseCluster
```

## Overview

Allows servers to ensure that listed clients are notified when a server is available for communication.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclustericdmanagement/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeActiveModeDuration(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeactivemodeduration%28completion%29.md)
- [func readAttributeActiveModeThreshold(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeactivemodethreshold%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeattributelist%28completion%29.md)
- [func readAttributeClientsSupportedPerFabric(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeclientssupportedperfabric%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeclusterrevision%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeICDCounter(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeicdcounter%28completion%29.md)
- [func readAttributeIdleModeDuration(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeidlemodeduration%28completion%29.md)
- [func readAttributeMaximumCheckInBackOff(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributemaximumcheckinbackoff%28completion%29.md)
- [func readAttributeOperatingMode(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeoperatingmode%28completion%29.md)
- [func readAttributeRegisteredClients(with: MTRReadParams?, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeregisteredclients%28with,completion%29.md)
- [func readAttributeUserActiveModeTriggerHint(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeuseractivemodetriggerhint%28completion%29.md)
- [func readAttributeUserActiveModeTriggerInstruction(completion: (String?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeuseractivemodetriggerinstruction%28completion%29.md)
- [func registerClient(with: MTRICDManagementClusterRegisterClientParams, completion: (MTRICDManagementClusterRegisterClientResponseParams?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/registerclient%28with,completion%29.md)
  Command RegisterClient
- [func stayActiveRequest(with: MTRICDManagementClusterStayActiveRequestParams, completion: (MTRICDManagementClusterStayActiveResponseParams?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/stayactiverequest%28with,completion%29.md)
  Command StayActiveRequest
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActiveModeDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributeactivemodeduration%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeActiveModeThreshold(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributeactivemodethreshold%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClientsSupportedPerFabric(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributeclientssupportedperfabric%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeICDCounter(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributeicdcounter%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeIdleModeDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributeidlemodeduration%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMaximumCheckInBackOff(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributemaximumcheckinbackoff%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeOperatingMode(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributeoperatingmode%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeRegisteredClients(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributeregisteredclients%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUserActiveModeTriggerHint(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributeuseractivemodetriggerhint%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUserActiveModeTriggerInstruction(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/subscribeattributeuseractivemodetriggerinstruction%28with,subscriptionestablished,reporthandler%29.md)
- [func unregisterClient(with: MTRICDManagementClusterUnregisterClientParams, completion: ((any Error)?) -> Void)](./mtrbaseclustericdmanagement/unregisterclient%28with,completion%29.md)
  Command UnregisterClient
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeActiveModeDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeactivemodeduration%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeActiveModeThreshold(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeactivemodethreshold%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClientsSupportedPerFabric(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeclientssupportedperfabric%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeICDCounter(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeicdcounter%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeIdleModeDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeidlemodeduration%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMaximumCheckInBackOff(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributemaximumcheckinbackoff%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeOperatingMode(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeoperatingmode%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeRegisteredClients(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeregisteredclients%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeUserActiveModeTriggerHint(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeuseractivemodetriggerhint%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeUserActiveModeTriggerInstruction(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclustericdmanagement/readattributeuseractivemodetriggerinstruction%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustericdmanagement)*