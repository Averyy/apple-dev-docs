# MTRBaseClusterNetworkCommissioning

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
class MTRBaseClusterNetworkCommissioning
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrbaseclusternetworkcommissioning/init(device:endpoint:queue:).md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusternetworkcommissioning/init(device:endpointid:queue:).md)
### Instance Methods
- [func addOrUpdateThreadNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateThreadNetworkParams, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/addorupdatethreadnetwork(with:completion:).md)
- [func addOrUpdateThreadNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateThreadNetworkParams, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/addorupdatethreadnetwork(with:completionhandler:).md)
- [func addOrUpdateWiFiNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateWiFiNetworkParams, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/addorupdatewifinetwork(with:completion:).md)
- [func addOrUpdateWiFiNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateWiFiNetworkParams, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/addorupdatewifinetwork(with:completionhandler:).md)
- [func connectNetwork(with: MTRNetworkCommissioningClusterConnectNetworkParams, completion: (MTRNetworkCommissioningClusterConnectNetworkResponseParams?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/connectnetwork(with:completion:).md)
- [func connectNetwork(with: MTRNetworkCommissioningClusterConnectNetworkParams, completionHandler: (MTRNetworkCommissioningClusterConnectNetworkResponseParams?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/connectnetwork(with:completionhandler:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeacceptedcommandlist(completionhandler:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeattributelist(completion:).md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeattributelist(completionhandler:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeclusterrevision(completion:).md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeclusterrevision(completionhandler:).md)
- [func readAttributeConnectMaxTimeSeconds(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeconnectmaxtimeseconds(completion:).md)
- [func readAttributeConnectMaxTimeSeconds(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeconnectmaxtimeseconds(completionhandler:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributefeaturemap(completion:).md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributefeaturemap(completionhandler:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributegeneratedcommandlist(completionhandler:).md)
- [func readAttributeInterfaceEnabled(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeinterfaceenabled(completion:).md)
- [func readAttributeInterfaceEnabled(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeinterfaceenabled(completionhandler:).md)
- [func readAttributeLastConnectErrorValue(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributelastconnecterrorvalue(completion:).md)
- [func readAttributeLastConnectErrorValue(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributelastconnecterrorvalue(completionhandler:).md)
- [func readAttributeLastNetworkID(completion: (Data?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributelastnetworkid(completion:).md)
- [func readAttributeLastNetworkID(completionHandler: (Data?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributelastnetworkid(completionhandler:).md)
- [func readAttributeLastNetworkingStatus(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributelastnetworkingstatus(completion:).md)
- [func readAttributeLastNetworkingStatus(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributelastnetworkingstatus(completionhandler:).md)
- [func readAttributeMaxNetworks(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributemaxnetworks(completion:).md)
- [func readAttributeMaxNetworks(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributemaxnetworks(completionhandler:).md)
- [func readAttributeNetworks(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributenetworks(completion:).md)
- [func readAttributeNetworks(completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributenetworks(completionhandler:).md)
- [func readAttributeScanMaxTimeSeconds(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributescanmaxtimeseconds(completion:).md)
- [func readAttributeScanMaxTimeSeconds(completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributescanmaxtimeseconds(completionhandler:).md)
- [func removeNetwork(with: MTRNetworkCommissioningClusterRemoveNetworkParams, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/removenetwork(with:completion:).md)
- [func removeNetwork(with: MTRNetworkCommissioningClusterRemoveNetworkParams, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/removenetwork(with:completionhandler:).md)
- [func reorderNetwork(with: MTRNetworkCommissioningClusterReorderNetworkParams, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/reordernetwork(with:completion:).md)
- [func reorderNetwork(with: MTRNetworkCommissioningClusterReorderNetworkParams, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/reordernetwork(with:completionhandler:).md)
- [func scanNetworks(completion: (MTRNetworkCommissioningClusterScanNetworksResponseParams?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/scannetworks(completion:).md)
- [func scanNetworks(with: MTRNetworkCommissioningClusterScanNetworksParams?, completion: (MTRNetworkCommissioningClusterScanNetworksResponseParams?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/scannetworks(with:completion:).md)
- [func scanNetworks(with: MTRNetworkCommissioningClusterScanNetworksParams?, completionHandler: (MTRNetworkCommissioningClusterScanNetworksResponseParams?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/scannetworks(with:completionhandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributeacceptedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributeattributelist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributeclusterrevision(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeConnectMaxTimeSeconds(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributeconnectmaxtimeseconds(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeConnectMaxTimeSeconds(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributeconnectmaxtimeseconds(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributefeaturemap(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributegeneratedcommandlist(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeInterfaceEnabled(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributeinterfaceenabled(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeInterfaceEnabled(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributeinterfaceenabled(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLastConnectErrorValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributelastconnecterrorvalue(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLastConnectErrorValue(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributelastconnecterrorvalue(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLastNetworkID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (Data?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributelastnetworkid(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLastNetworkID(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (Data?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributelastnetworkid(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLastNetworkingStatus(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributelastnetworkingstatus(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLastNetworkingStatus(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributelastnetworkingstatus(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMaxNetworks(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributemaxnetworks(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMaxNetworks(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributemaxnetworks(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNetworks(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributenetworks(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNetworks(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributenetworks(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeScanMaxTimeSeconds(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributescanmaxtimeseconds(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeScanMaxTimeSeconds(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributescanmaxtimeseconds(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:).md)
- [func writeAttributeInterfaceEnabled(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/writeattributeinterfaceenabled(withvalue:completion:).md)
- [func writeAttributeInterfaceEnabled(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/writeattributeinterfaceenabled(withvalue:completionhandler:).md)
- [func writeAttributeInterfaceEnabled(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/writeattributeinterfaceenabled(withvalue:params:completion:).md)
- [func writeAttributeInterfaceEnabled(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/writeattributeinterfaceenabled(withvalue:params:completionhandler:).md)
- [func readAttributeSupportedThreadFeatures(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributesupportedthreadfeatures(completion:).md)
- [func readAttributeSupportedWiFiBands(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributesupportedwifibands(completion:).md)
- [func readAttributeThreadVersion(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributethreadversion(completion:).md)
- [func subscribeAttributeSupportedThreadFeatures(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributesupportedthreadfeatures(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSupportedWiFiBands(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributesupportedwifibands(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeThreadVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/subscribeattributethreadversion(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeacceptedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeattributelist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeclusterrevision(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeConnectMaxTimeSeconds(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeconnectmaxtimeseconds(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeConnectMaxTimeSeconds(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeconnectmaxtimeseconds(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributefeaturemap(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributegeneratedcommandlist(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeInterfaceEnabled(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeinterfaceenabled(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeInterfaceEnabled(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributeinterfaceenabled(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeLastConnectErrorValue(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributelastconnecterrorvalue(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeLastConnectErrorValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributelastconnecterrorvalue(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeLastNetworkID(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (Data?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributelastnetworkid(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeLastNetworkID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (Data?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributelastnetworkid(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeLastNetworkingStatus(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributelastnetworkingstatus(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeLastNetworkingStatus(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributelastnetworkingstatus(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMaxNetworks(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributemaxnetworks(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeMaxNetworks(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributemaxnetworks(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeNetworks(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributenetworks(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeNetworks(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributenetworks(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeScanMaxTimeSeconds(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributescanmaxtimeseconds(withattributecache:endpoint:queue:completionhandler:).md)
- [class func readAttributeScanMaxTimeSeconds(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributescanmaxtimeseconds(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSupportedThreadFeatures(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributesupportedthreadfeatures(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSupportedWiFiBands(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributesupportedwifibands(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeThreadVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusternetworkcommissioning/readattributethreadversion(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusternetworkcommissioning)*