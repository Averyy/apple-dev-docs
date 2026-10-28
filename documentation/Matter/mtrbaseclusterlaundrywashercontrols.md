# MTRBaseClusterLaundryWasherControls

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Laundry Washer Controls

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
class MTRBaseClusterLaundryWasherControls
```

```objc
@interface MTRBaseClusterLaundryWasherControls : MTRGenericBaseCluster
```

## Overview

This cluster supports remotely monitoring and controlling the different types of functionality available to a washing device, such as a washing machine.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterlaundrywashercontrols/init%28device,endpointid,queue%29.md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributeclusterrevision%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeNumberOfRinses(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributenumberofrinses%28completion%29.md)
- [func readAttributeSpinSpeedCurrent(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributespinspeedcurrent%28completion%29.md)
- [func readAttributeSpinSpeeds(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributespinspeeds%28completion%29.md)
- [func readAttributeSupportedRinses(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributesupportedrinses%28completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNumberOfRinses(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/subscribeattributenumberofrinses%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSpinSpeedCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/subscribeattributespinspeedcurrent%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSpinSpeeds(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/subscribeattributespinspeeds%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSupportedRinses(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/subscribeattributesupportedrinses%28with,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeNumberOfRinses(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/writeattributenumberofrinses%28withvalue,completion%29.md)
- [func writeAttributeNumberOfRinses(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/writeattributenumberofrinses%28withvalue,params,completion%29.md)
- [func writeAttributeSpinSpeedCurrent(withValue: NSNumber?, completion: ((any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/writeattributespinspeedcurrent%28withvalue,completion%29.md)
- [func writeAttributeSpinSpeedCurrent(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/writeattributespinspeedcurrent%28withvalue,params,completion%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeNumberOfRinses(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributenumberofrinses%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSpinSpeedCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributespinspeedcurrent%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSpinSpeeds(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributespinspeeds%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSupportedRinses(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterlaundrywashercontrols/readattributesupportedrinses%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterlaundrywashercontrols)*