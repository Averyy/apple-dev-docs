# MTRBaseClusterOvenMode

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Oven Mode

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
class MTRBaseClusterOvenMode
```

```objc
@interface MTRBaseClusterOvenMode : MTRGenericBaseCluster
```

## Overview

Attributes and commands for selecting a mode from a list of supported options.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterovenmode/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func changeToMode(with: MTROvenModeClusterChangeToModeParams, completion: (MTROvenModeClusterChangeToModeResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/changetomode%28with,completion%29.md)
  Command ChangeToMode
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributeclusterrevision%28completion%29.md)
- [func readAttributeCurrentMode(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributecurrentmode%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeSupportedModes(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributesupportedmodes%28completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentMode(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/subscribeattributecurrentmode%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSupportedModes(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/subscribeattributesupportedmodes%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCurrentMode(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributecurrentmode%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSupportedModes(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterovenmode/readattributesupportedmodes%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterovenmode)*