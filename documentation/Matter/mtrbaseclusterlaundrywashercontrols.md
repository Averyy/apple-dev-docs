# MTRBaseClusterLaundryWasherControls

**Framework**: Matter  
**Kind**: class

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

#### Overview

This cluster supports remotely monitoring and controlling the different types of functionality available to a washing device, such as a washing machine.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterlaundrywashercontrols/init(device:endpointid:queue:).md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributeclusterrevision(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeNumberOfRinses(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributenumberofrinses(completion:).md)
- [func readAttributeSpinSpeedCurrent(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributespinspeedcurrent(completion:).md)
- [func readAttributeSpinSpeeds(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributespinspeeds(completion:).md)
- [func readAttributeSupportedRinses(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributesupportedrinses(completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNumberOfRinses(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/subscribeattributenumberofrinses(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSpinSpeedCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/subscribeattributespinspeedcurrent(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSpinSpeeds(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/subscribeattributespinspeeds(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSupportedRinses(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/subscribeattributesupportedrinses(with:subscriptionestablished:reporthandler:).md)
- [func writeAttributeNumberOfRinses(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/writeattributenumberofrinses(withvalue:completion:).md)
- [func writeAttributeNumberOfRinses(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/writeattributenumberofrinses(withvalue:params:completion:).md)
- [func writeAttributeSpinSpeedCurrent(withValue: NSNumber?, completion: ((any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/writeattributespinspeedcurrent(withvalue:completion:).md)
- [func writeAttributeSpinSpeedCurrent(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/writeattributespinspeedcurrent(withvalue:params:completion:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeNumberOfRinses(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributenumberofrinses(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSpinSpeedCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributespinspeedcurrent(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSpinSpeeds(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributespinspeeds(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSupportedRinses(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterlaundrywashercontrols/readattributesupportedrinses(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterlaundrywashercontrols)*