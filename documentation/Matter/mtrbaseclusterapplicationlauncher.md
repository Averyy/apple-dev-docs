# MTRBaseClusterApplicationLauncher

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
class MTRBaseClusterApplicationLauncher
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusterapplicationlauncher/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterapplicationlauncher/init(device:endpointid:queue:).md)
### Instance Methods
- [func hideApp(completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/hideapp(completion:).md)
- [func hideApp(with: MTRApplicationLauncherClusterHideAppParams?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/hideapp(with:completion:).md)
- [func hideApp(with: MTRApplicationLauncherClusterHideAppParams?, completionHandler: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/hideapp(with:completionhandler:).md)
- [func launchApp(completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/launchapp(completion:).md)
- [func launchApp(with: MTRApplicationLauncherClusterLaunchAppParams?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/launchapp(with:completion:).md)
- [func launchApp(with: MTRApplicationLauncherClusterLaunchAppParams?, completionHandler: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/launchapp(with:completionhandler:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributeattributelist(completionhandler:).md)
- [func readAttributeCatalogList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributecataloglist(completion:).md)
- [func readAttributeCatalogList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributecataloglist(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeCurrentApp(completion: (MTRApplicationLauncherClusterApplicationEPStruct?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributecurrentapp(completion:).md)
- [func readAttributeCurrentApp(completionHandler: (MTRApplicationLauncherClusterApplicationEP?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributecurrentapp(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributegeneratedcommandlist(completionhandler:).md)
- [func stopApp(completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/stopapp(completion:).md)
- [func stopApp(with: MTRApplicationLauncherClusterStopAppParams?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/stopapp(with:completion:).md)
- [func stopApp(with: MTRApplicationLauncherClusterStopAppParams?, completionHandler: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/stopapp(with:completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCatalogList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributecataloglist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCatalogList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributecataloglist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentApp(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRApplicationLauncherClusterApplicationEPStruct?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributecurrentapp(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentApp(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRApplicationLauncherClusterApplicationEP?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributecurrentapp(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func writeAttributeCurrentApp(withValue: MTRApplicationLauncherClusterApplicationEPStruct?, completion: MTRStatusCompletion)](mtrbaseclusterapplicationlauncher/writeattributecurrentapp(withvalue:completion:).md)
- [func writeAttributeCurrentApp(withValue: MTRApplicationLauncherClusterApplicationEP?, completionHandler: MTRStatusCompletion)](mtrbaseclusterapplicationlauncher/writeattributecurrentapp(withvalue:completionhandler:).md)
- [func writeAttributeCurrentApp(withValue: MTRApplicationLauncherClusterApplicationEPStruct?, params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterapplicationlauncher/writeattributecurrentapp(withvalue:params:completion:).md)
- [func writeAttributeCurrentApp(withValue: MTRApplicationLauncherClusterApplicationEP?, params: MTRWriteParams?, completionHandler: MTRStatusCompletion)](mtrbaseclusterapplicationlauncher/writeattributecurrentapp(withvalue:params:completionhandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCatalogList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributecataloglist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeCatalogList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributecataloglist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCurrentApp(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (MTRApplicationLauncherClusterApplicationEP?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributecurrentapp(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeCurrentApp(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRApplicationLauncherClusterApplicationEPStruct?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributecurrentapp(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterapplicationlauncher/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterapplicationlauncher)*