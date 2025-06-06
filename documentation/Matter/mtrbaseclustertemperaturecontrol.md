# MTRBaseClusterTemperatureControl

**Framework**: Matter  
**Kind**: class

Cluster Temperature Control

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
class MTRBaseClusterTemperatureControl
```

#### Overview

Attributes and commands for configuring the temperature control, and reporting temperature.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclustertemperaturecontrol/init(device:endpointid:queue:).md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributeclusterrevision(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeMaxTemperature(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributemaxtemperature(completion:).md)
- [func readAttributeMinTemperature(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributemintemperature(completion:).md)
- [func readAttributeSelectedTemperatureLevel(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributeselectedtemperaturelevel(completion:).md)
- [func readAttributeStep(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributestep(completion:).md)
- [func readAttributeSupportedTemperatureLevels(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributesupportedtemperaturelevels(completion:).md)
- [func readAttributeTemperatureSetpoint(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributetemperaturesetpoint(completion:).md)
- [func setTemperatureWith(MTRTemperatureControlClusterSetTemperatureParams?, completion: MTRStatusCompletion)](mtrbaseclustertemperaturecontrol/settemperaturewith(_:completion:).md)
  Command SetTemperature
- [func setTemperatureWithCompletion(MTRStatusCompletion)](mtrbaseclustertemperaturecontrol/settemperaturewithcompletion(_:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMaxTemperature(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/subscribeattributemaxtemperature(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMinTemperature(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/subscribeattributemintemperature(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSelectedTemperatureLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/subscribeattributeselectedtemperaturelevel(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeStep(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/subscribeattributestep(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSupportedTemperatureLevels(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/subscribeattributesupportedtemperaturelevels(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeTemperatureSetpoint(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/subscribeattributetemperaturesetpoint(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMaxTemperature(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributemaxtemperature(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMinTemperature(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributemintemperature(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSelectedTemperatureLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributeselectedtemperaturelevel(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeStep(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributestep(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSupportedTemperatureLevels(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributesupportedtemperaturelevels(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeTemperatureSetpoint(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustertemperaturecontrol/readattributetemperaturesetpoint(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertemperaturecontrol)*