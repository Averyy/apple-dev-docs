# MTRBaseClusterTemperatureControl

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRBaseClusterTemperatureControl : MTRGenericBaseCluster
```

#### Overview

Attributes and commands for configuring the temperature control, and reporting temperature.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclustertemperaturecontrol/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributeclusterrevision%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeMaxTemperature(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributemaxtemperature%28completion%29.md)
- [func readAttributeMinTemperature(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributemintemperature%28completion%29.md)
- [func readAttributeSelectedTemperatureLevel(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributeselectedtemperaturelevel%28completion%29.md)
- [func readAttributeStep(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributestep%28completion%29.md)
- [func readAttributeSupportedTemperatureLevels(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributesupportedtemperaturelevels%28completion%29.md)
- [func readAttributeTemperatureSetpoint(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributetemperaturesetpoint%28completion%29.md)
- [func setTemperatureWith(MTRTemperatureControlClusterSetTemperatureParams?, completion: ((any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/settemperaturewith%28_,completion%29.md)
  Command SetTemperature
- [func setTemperatureWithCompletion(((any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/settemperaturewithcompletion%28_%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMaxTemperature(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/subscribeattributemaxtemperature%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMinTemperature(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/subscribeattributemintemperature%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSelectedTemperatureLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/subscribeattributeselectedtemperaturelevel%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeStep(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/subscribeattributestep%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSupportedTemperatureLevels(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/subscribeattributesupportedtemperaturelevels%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeTemperatureSetpoint(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/subscribeattributetemperaturesetpoint%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMaxTemperature(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributemaxtemperature%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMinTemperature(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributemintemperature%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSelectedTemperatureLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributeselectedtemperaturelevel%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeStep(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributestep%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSupportedTemperatureLevels(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributesupportedtemperaturelevels%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeTemperatureSetpoint(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclustertemperaturecontrol/readattributetemperaturesetpoint%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertemperaturecontrol)*