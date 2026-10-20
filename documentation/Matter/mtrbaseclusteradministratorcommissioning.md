# MTRBaseClusterAdministratorCommissioning

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
class MTRBaseClusterAdministratorCommissioning
```

```objc
@interface MTRBaseClusterAdministratorCommissioning : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusteradministratorcommissioning/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusteradministratorcommissioning/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func openBasicCommissioningWindow(with: MTRAdministratorCommissioningClusterOpenBasicCommissioningWindowParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/openbasiccommissioningwindow%28with,completion%29.md)
- [func openBasicCommissioningWindow(with: MTRAdministratorCommissioningClusterOpenBasicCommissioningWindowParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/openbasiccommissioningwindow%28with,completionhandler%29.md)
- [func openWindow(with: MTRAdministratorCommissioningClusterOpenCommissioningWindowParams, completion: ((any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/openwindow%28with,completion%29.md)
- [func openWindow(with: MTRAdministratorCommissioningClusterOpenCommissioningWindowParams, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/openwindow%28with,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAdminFabricIndex(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeadminfabricindex%28completion%29.md)
- [func readAttributeAdminFabricIndex(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeadminfabricindex%28completionhandler%29.md)
- [func readAttributeAdminVendorId(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeadminvendorid%28completion%29.md)
- [func readAttributeAdminVendorId(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeadminvendorid%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeWindowStatus(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributewindowstatus%28completion%29.md)
- [func readAttributeWindowStatus(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributewindowstatus%28completionhandler%29.md)
- [func revokeCommissioning(completion: ((any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/revokecommissioning%28completion%29.md)
- [func revokeCommissioning(completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/revokecommissioning%28completionhandler%29.md)
- [func revokeCommissioning(with: MTRAdministratorCommissioningClusterRevokeCommissioningParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/revokecommissioning%28with,completion%29.md)
- [func revokeCommissioning(with: MTRAdministratorCommissioningClusterRevokeCommissioningParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/revokecommissioning%28with,completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAdminFabricIndex(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributeadminfabricindex%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAdminFabricIndex(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributeadminfabricindex%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAdminVendorId(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributeadminvendorid%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAdminVendorId(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributeadminvendorid%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeWindowStatus(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributewindowstatus%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeWindowStatus(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/subscribeattributewindowstatus%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAdminFabricIndex(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeadminfabricindex%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAdminFabricIndex(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeadminfabricindex%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAdminVendorId(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeadminvendorid%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAdminVendorId(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeadminvendorid%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeWindowStatus(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributewindowstatus%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeWindowStatus(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusteradministratorcommissioning/readattributewindowstatus%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteradministratorcommissioning)*