# MTRBaseClusterNetworkCommissioning

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
class MTRBaseClusterNetworkCommissioning
```

```objc
@interface MTRBaseClusterNetworkCommissioning : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrbaseclusternetworkcommissioning/init%28device,endpoint,queue%29.md)
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusternetworkcommissioning/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func addOrUpdateThreadNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateThreadNetworkParams, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/addorupdatethreadnetwork%28with,completion%29.md)
- [func addOrUpdateThreadNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateThreadNetworkParams, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/addorupdatethreadnetwork%28with,completionhandler%29.md)
- [func addOrUpdateWiFiNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateWiFiNetworkParams, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/addorupdatewifinetwork%28with,completion%29.md)
- [func addOrUpdateWiFiNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateWiFiNetworkParams, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/addorupdatewifinetwork%28with,completionhandler%29.md)
- [func connectNetwork(with: MTRNetworkCommissioningClusterConnectNetworkParams, completion: (MTRNetworkCommissioningClusterConnectNetworkResponseParams?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/connectnetwork%28with,completion%29.md)
- [func connectNetwork(with: MTRNetworkCommissioningClusterConnectNetworkParams, completionHandler: (MTRNetworkCommissioningClusterConnectNetworkResponseParams?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/connectnetwork%28with,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAcceptedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeacceptedcommandlist%28completionhandler%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeattributelist%28completion%29.md)
- [func readAttributeAttributeList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeattributelist%28completionhandler%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeclusterrevision%28completion%29.md)
- [func readAttributeClusterRevision(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeclusterrevision%28completionhandler%29.md)
- [func readAttributeConnectMaxTimeSeconds(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeconnectmaxtimeseconds%28completion%29.md)
- [func readAttributeConnectMaxTimeSeconds(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeconnectmaxtimeseconds%28completionhandler%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributefeaturemap%28completion%29.md)
- [func readAttributeFeatureMap(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributefeaturemap%28completionhandler%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeGeneratedCommandList(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributegeneratedcommandlist%28completionhandler%29.md)
- [func readAttributeInterfaceEnabled(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeinterfaceenabled%28completion%29.md)
- [func readAttributeInterfaceEnabled(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeinterfaceenabled%28completionhandler%29.md)
- [func readAttributeLastConnectErrorValue(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributelastconnecterrorvalue%28completion%29.md)
- [func readAttributeLastConnectErrorValue(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributelastconnecterrorvalue%28completionhandler%29.md)
- [func readAttributeLastNetworkID(completion: (Data?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributelastnetworkid%28completion%29.md)
- [func readAttributeLastNetworkID(completionHandler: (Data?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributelastnetworkid%28completionhandler%29.md)
- [func readAttributeLastNetworkingStatus(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributelastnetworkingstatus%28completion%29.md)
- [func readAttributeLastNetworkingStatus(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributelastnetworkingstatus%28completionhandler%29.md)
- [func readAttributeMaxNetworks(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributemaxnetworks%28completion%29.md)
- [func readAttributeMaxNetworks(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributemaxnetworks%28completionhandler%29.md)
- [func readAttributeNetworks(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributenetworks%28completion%29.md)
- [func readAttributeNetworks(completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributenetworks%28completionhandler%29.md)
- [func readAttributeScanMaxTimeSeconds(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributescanmaxtimeseconds%28completion%29.md)
- [func readAttributeScanMaxTimeSeconds(completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributescanmaxtimeseconds%28completionhandler%29.md)
- [func removeNetwork(with: MTRNetworkCommissioningClusterRemoveNetworkParams, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/removenetwork%28with,completion%29.md)
- [func removeNetwork(with: MTRNetworkCommissioningClusterRemoveNetworkParams, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/removenetwork%28with,completionhandler%29.md)
- [func reorderNetwork(with: MTRNetworkCommissioningClusterReorderNetworkParams, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/reordernetwork%28with,completion%29.md)
- [func reorderNetwork(with: MTRNetworkCommissioningClusterReorderNetworkParams, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/reordernetwork%28with,completionhandler%29.md)
- [func scanNetworks(completion: (MTRNetworkCommissioningClusterScanNetworksResponseParams?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/scannetworks%28completion%29.md)
- [func scanNetworks(with: MTRNetworkCommissioningClusterScanNetworksParams?, completion: (MTRNetworkCommissioningClusterScanNetworksResponseParams?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/scannetworks%28with,completion%29.md)
- [func scanNetworks(with: MTRNetworkCommissioningClusterScanNetworksParams?, completionHandler: (MTRNetworkCommissioningClusterScanNetworksResponseParams?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/scannetworks%28with,completionhandler%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAcceptedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributeacceptedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributeattributelist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributeclusterrevision%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeConnectMaxTimeSeconds(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributeconnectmaxtimeseconds%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeConnectMaxTimeSeconds(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributeconnectmaxtimeseconds%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributefeaturemap%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributegeneratedcommandlist%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeInterfaceEnabled(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributeinterfaceenabled%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeInterfaceEnabled(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributeinterfaceenabled%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLastConnectErrorValue(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributelastconnecterrorvalue%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLastConnectErrorValue(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributelastconnecterrorvalue%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLastNetworkID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (Data?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributelastnetworkid%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLastNetworkID(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (Data?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributelastnetworkid%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLastNetworkingStatus(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributelastnetworkingstatus%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLastNetworkingStatus(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributelastnetworkingstatus%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMaxNetworks(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributemaxnetworks%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeMaxNetworks(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributemaxnetworks%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNetworks(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributenetworks%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNetworks(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributenetworks%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeScanMaxTimeSeconds(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributescanmaxtimeseconds%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeScanMaxTimeSeconds(withMinInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributescanmaxtimeseconds%28withmininterval,maxinterval,params,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeInterfaceEnabled(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/writeattributeinterfaceenabled%28withvalue,completion%29.md)
- [func writeAttributeInterfaceEnabled(withValue: NSNumber, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/writeattributeinterfaceenabled%28withvalue,completionhandler%29.md)
- [func writeAttributeInterfaceEnabled(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/writeattributeinterfaceenabled%28withvalue,params,completion%29.md)
- [func writeAttributeInterfaceEnabled(withValue: NSNumber, params: MTRWriteParams?, completionHandler: ((any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/writeattributeinterfaceenabled%28withvalue,params,completionhandler%29.md)
- [func readAttributeSupportedThreadFeatures(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributesupportedthreadfeatures%28completion%29.md)
- [func readAttributeSupportedWiFiBands(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributesupportedwifibands%28completion%29.md)
- [func readAttributeThreadVersion(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributethreadversion%28completion%29.md)
- [func subscribeAttributeSupportedThreadFeatures(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributesupportedthreadfeatures%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSupportedWiFiBands(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributesupportedwifibands%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeThreadVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/subscribeattributethreadversion%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeacceptedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeattributelist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeclusterrevision%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeConnectMaxTimeSeconds(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeconnectmaxtimeseconds%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeConnectMaxTimeSeconds(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeconnectmaxtimeseconds%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributefeaturemap%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributegeneratedcommandlist%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeInterfaceEnabled(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeinterfaceenabled%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeInterfaceEnabled(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributeinterfaceenabled%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeLastConnectErrorValue(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributelastconnecterrorvalue%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeLastConnectErrorValue(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributelastconnecterrorvalue%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeLastNetworkID(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (Data?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributelastnetworkid%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeLastNetworkID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (Data?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributelastnetworkid%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeLastNetworkingStatus(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributelastnetworkingstatus%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeLastNetworkingStatus(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributelastnetworkingstatus%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMaxNetworks(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributemaxnetworks%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeMaxNetworks(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributemaxnetworks%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeNetworks(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributenetworks%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeNetworks(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributenetworks%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeScanMaxTimeSeconds(withAttributeCache: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributescanmaxtimeseconds%28withattributecache,endpoint,queue,completionhandler%29.md)
- [class func readAttributeScanMaxTimeSeconds(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributescanmaxtimeseconds%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSupportedThreadFeatures(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributesupportedthreadfeatures%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSupportedWiFiBands(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributesupportedwifibands%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeThreadVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusternetworkcommissioning/readattributethreadversion%28withclusterstatecache,endpoint,queue,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusternetworkcommissioning)*