# MTRBaseClusterApplicationLauncher

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRBaseClusterApplicationLauncher : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusterapplicationlauncher/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterapplicationlauncher/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func hideApp(completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/hideapp%28completion%29.md)
- [func hideApp(with: MTRApplicationLauncherClusterHideAppParams?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/hideapp%28with,completion%29.md)
- [func hideApp(with: MTRApplicationLauncherClusterHideAppParams?, completionHandler: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/hideapp%28with,completionhandler%29.md)
- [func launchApp(completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/launchapp%28completion%29.md)
- [func launchApp(with: MTRApplicationLauncherClusterLaunchAppParams?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/launchapp%28with,completion%29.md)
- [func launchApp(with: MTRApplicationLauncherClusterLaunchAppParams?, completionHandler: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/launchapp%28with,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeCatalogList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributecataloglist%28completion%29.md)
- [func readAttributeCatalogList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributecataloglist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeCurrentApp(completion: (MTRApplicationLauncherClusterApplicationEPStruct?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributecurrentapp%28completion%29.md)
- [func readAttributeCurrentApp(completionHandler: (MTRApplicationLauncherClusterApplicationEP?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributecurrentapp%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func stopApp(completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/stopapp%28completion%29.md)
- [func stopApp(with: MTRApplicationLauncherClusterStopAppParams?, completion: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/stopapp%28with,completion%29.md)
- [func stopApp(with: MTRApplicationLauncherClusterStopAppParams?, completionHandler: (MTRApplicationLauncherClusterLauncherResponseParams?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/stopapp%28with,completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCatalogList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributecataloglist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCatalogList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributecataloglist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentApp(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRApplicationLauncherClusterApplicationEPStruct?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributecurrentapp%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCurrentApp(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRApplicationLauncherClusterApplicationEP?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributecurrentapp%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeCurrentApp(withValue: MTRApplicationLauncherClusterApplicationEPStruct?, completion: ((any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/writeattributecurrentapp%28withvalue,completion%29.md)
- [func writeAttributeCurrentApp(withValue: MTRApplicationLauncherClusterApplicationEP?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/writeattributecurrentapp%28withvalue,completionhandler%29.md)
- [func writeAttributeCurrentApp(withValue: MTRApplicationLauncherClusterApplicationEPStruct?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/writeattributecurrentapp%28withvalue,params,completion%29.md)
- [func writeAttributeCurrentApp(withValue: MTRApplicationLauncherClusterApplicationEP?, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/writeattributecurrentapp%28withvalue,params,completionhandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCatalogList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributecataloglist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeCatalogList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributecataloglist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCurrentApp(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (MTRApplicationLauncherClusterApplicationEP?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributecurrentapp%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeCurrentApp(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRApplicationLauncherClusterApplicationEPStruct?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributecurrentapp%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterapplicationlauncher/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterapplicationlauncher)*