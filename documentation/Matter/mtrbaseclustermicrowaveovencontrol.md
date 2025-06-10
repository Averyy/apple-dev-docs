# MTRBaseClusterMicrowaveOvenControl

**Framework**: Matter  
**Kind**: class

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

#### Overview

Attributes and commands for configuring the microwave oven control, and reporting cooking stats.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclustermicrowaveovencontrol/init(device:endpointid:queue:).md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func addMoreTime(with: MTRMicrowaveOvenControlClusterAddMoreTimeParams, completion: ((any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/addmoretime(with:completion:).md)
  Command AddMoreTime
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributeclusterrevision(completion:).md)
- [func readAttributeCookTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributecooktime(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeMaxCookTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributemaxcooktime(completion:).md)
- [func readAttributeMaxPower(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributemaxpower(completion:).md)
- [func readAttributeMinPower(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributeminpower(completion:).md)
- [func readAttributePowerSetting(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributepowersetting(completion:).md)
- [func readAttributePowerStep(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributepowerstep(completion:).md)
- [func readAttributeWattRating(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributewattrating(completion:).md)
- [func setCookingParametersWith(MTRMicrowaveOvenControlClusterSetCookingParametersParams?, completion: ((any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/setcookingparameterswith(_:completion:).md)
  Command SetCookingParameters
- [func setCookingParametersWithCompletion(((any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/setcookingparameterswithcompletion(_:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCookTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/subscribeattributecooktime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMaxCookTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/subscribeattributemaxcooktime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMaxPower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/subscribeattributemaxpower(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMinPower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/subscribeattributeminpower(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePowerSetting(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/subscribeattributepowersetting(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePowerStep(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/subscribeattributepowerstep(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeWattRating(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/subscribeattributewattrating(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCookTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributecooktime(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMaxCookTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributemaxcooktime(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMaxPower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributemaxpower(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMinPower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributeminpower(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePowerSetting(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributepowersetting(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePowerStep(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributepowerstep(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeWattRating(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermicrowaveovencontrol/readattributewattrating(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermicrowaveovencontrol)*