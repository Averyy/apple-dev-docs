# MTRBaseClusterWiFiNetworkManagement

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Wi-Fi Network Management

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
class MTRBaseClusterWiFiNetworkManagement
```

```objc
@interface MTRBaseClusterWiFiNetworkManagement : MTRGenericBaseCluster
```

## Overview

Functionality to retrieve operational information about a managed Wi-Fi network.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterwifinetworkmanagement/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func networkPassphraseRequest(completion: (MTRWiFiNetworkManagementClusterNetworkPassphraseResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/networkpassphraserequest%28completion%29.md)
- [func networkPassphraseRequest(with: MTRWiFiNetworkManagementClusterNetworkPassphraseRequestParams?, completion: (MTRWiFiNetworkManagementClusterNetworkPassphraseResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/networkpassphraserequest%28with,completion%29.md)
  Command NetworkPassphraseRequest
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributeclusterrevision%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributePassphraseSurrogate(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributepassphrasesurrogate%28completion%29.md)
- [func readAttributeSSID(completion: (Data?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributessid%28completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePassphraseSurrogate(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/subscribeattributepassphrasesurrogate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSSID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (Data?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/subscribeattributessid%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePassphraseSurrogate(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributepassphrasesurrogate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSSID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (Data?, (any Error)?) -> Void)](./mtrbaseclusterwifinetworkmanagement/readattributessid%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterwifinetworkmanagement)*