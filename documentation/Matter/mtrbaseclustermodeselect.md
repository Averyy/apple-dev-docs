# MTRBaseClusterModeSelect

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRBaseClusterModeSelect
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclustermodeselect/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclustermodeselect/init(device:endpointid:queue:).md)
### Instance Methods
- [func changeToMode(with: MTRModeSelectClusterChangeToModeParams, completion: ((any Error)?) -> Void)](mtrbaseclustermodeselect/changetomode(with:completion:).md)
- [func changeToMode(with: MTRModeSelectClusterChangeToModeParams, completionHandler: ((any Error)?) -> Void)](mtrbaseclustermodeselect/changetomode(with:completionhandler:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeattributelist(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeCurrentMode(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributecurrentmode(completion:).md)
- [func readAttributeCurrentMode(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributecurrentmode(completionhandler:).md)
- [func readAttributeDescription(completion: (String?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributedescription(completion:).md)
- [func readAttributeDescription(completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributedescription(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeOnMode(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeonmode(completion:).md)
- [func readAttributeOnMode(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeonmode(completionhandler:).md)
- [func readAttributeStandardNamespace(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributestandardnamespace(completion:).md)
- [func readAttributeStandardNamespace(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributestandardnamespace(completionhandler:).md)
- [func readAttributeStartUpMode(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributestartupmode(completion:).md)
- [func readAttributeStartUpMode(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributestartupmode(completionhandler:).md)
- [func readAttributeSupportedModes(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributesupportedmodes(completion:).md)
- [func readAttributeSupportedModes(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributesupportedmodes(completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentMode(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributecurrentmode(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentMode(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributecurrentmode(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDescription(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributedescription(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDescription(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributedescription(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOnMode(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributeonmode(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOnMode(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributeonmode(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeStandardNamespace(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributestandardnamespace(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeStandardNamespace(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributestandardnamespace(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeStartUpMode(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributestartupmode(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeStartUpMode(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributestartupmode(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSupportedModes(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributesupportedmodes(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSupportedModes(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/subscribeattributesupportedmodes(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func writeAttributeOnMode(withValue: NSNumber?, completion: ((any Error)?) -> Void)](mtrbaseclustermodeselect/writeattributeonmode(withvalue:completion:).md)
- [func writeAttributeOnMode(withValue: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrbaseclustermodeselect/writeattributeonmode(withvalue:completionhandler:).md)
- [func writeAttributeOnMode(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclustermodeselect/writeattributeonmode(withvalue:params:completion:).md)
- [func writeAttributeOnMode(withValue: NSNumber?, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclustermodeselect/writeattributeonmode(withvalue:params:completionhandler:).md)
- [func writeAttributeStartUpMode(withValue: NSNumber?, completion: ((any Error)?) -> Void)](mtrbaseclustermodeselect/writeattributestartupmode(withvalue:completion:).md)
- [func writeAttributeStartUpMode(withValue: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrbaseclustermodeselect/writeattributestartupmode(withvalue:completionhandler:).md)
- [func writeAttributeStartUpMode(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclustermodeselect/writeattributestartupmode(withvalue:params:completion:).md)
- [func writeAttributeStartUpMode(withValue: NSNumber?, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclustermodeselect/writeattributestartupmode(withvalue:params:completionhandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCurrentMode(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributecurrentmode(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeCurrentMode(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributecurrentmode(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDescription(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (String?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributedescription(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeDescription(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributedescription(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOnMode(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeonmode(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeOnMode(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributeonmode(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeStandardNamespace(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributestandardnamespace(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeStandardNamespace(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributestandardnamespace(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeStartUpMode(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributestartupmode(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeStartUpMode(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributestartupmode(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSupportedModes(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributesupportedmodes(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeSupportedModes(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclustermodeselect/readattributesupportedmodes(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermodeselect)*