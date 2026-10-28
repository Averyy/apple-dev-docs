# MTRBaseClusterMicrowaveOvenControl

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Microwave Oven Control

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
class MTRBaseClusterMicrowaveOvenControl
```

```objc
@interface MTRBaseClusterMicrowaveOvenControl : MTRGenericBaseCluster
```

## Overview

Attributes and commands for configuring the microwave oven control, and reporting cooking stats.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclustermicrowaveovencontrol/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func addMoreTime(with: MTRMicrowaveOvenControlClusterAddMoreTimeParams, completion: ((any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/addmoretime%28with,completion%29.md)
  Command AddMoreTime
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributeclusterrevision%28completion%29.md)
- [func readAttributeCookTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributecooktime%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeMaxCookTime(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributemaxcooktime%28completion%29.md)
- [func readAttributeMaxPower(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributemaxpower%28completion%29.md)
- [func readAttributeMinPower(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributeminpower%28completion%29.md)
- [func readAttributePowerSetting(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributepowersetting%28completion%29.md)
- [func readAttributePowerStep(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributepowerstep%28completion%29.md)
- [func readAttributeWattRating(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributewattrating%28completion%29.md)
- [func setCookingParametersWith(MTRMicrowaveOvenControlClusterSetCookingParametersParams?, completion: ((any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/setcookingparameterswith%28_,completion%29.md)
  Command SetCookingParameters
- [func setCookingParametersWithCompletion(((any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/setcookingparameterswithcompletion%28_%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCookTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/subscribeattributecooktime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMaxCookTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/subscribeattributemaxcooktime%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMaxPower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/subscribeattributemaxpower%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMinPower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/subscribeattributeminpower%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePowerSetting(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/subscribeattributepowersetting%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePowerStep(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/subscribeattributepowerstep%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeWattRating(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/subscribeattributewattrating%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCookTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributecooktime%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMaxCookTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributemaxcooktime%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMaxPower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributemaxpower%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMinPower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributeminpower%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePowerSetting(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributepowersetting%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePowerStep(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributepowerstep%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeWattRating(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustermicrowaveovencontrol/readattributewattrating%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermicrowaveovencontrol)*