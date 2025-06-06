# MTRClusterNetworkCommissioning

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
class MTRClusterNetworkCommissioning
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusternetworkcommissioning/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusternetworkcommissioning/init(device:endpointid:queue:).md)
### Instance Methods
- [func addOrUpdateThreadNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateThreadNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrclusternetworkcommissioning/addorupdatethreadnetwork(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func addOrUpdateThreadNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateThreadNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrclusternetworkcommissioning/addorupdatethreadnetwork(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func addOrUpdateWiFiNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateWiFiNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrclusternetworkcommissioning/addorupdatewifinetwork(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func addOrUpdateWiFiNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateWiFiNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrclusternetworkcommissioning/addorupdatewifinetwork(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func connectNetwork(with: MTRNetworkCommissioningClusterConnectNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterConnectNetworkResponseParams?, (any Error)?) -> Void)](mtrclusternetworkcommissioning/connectnetwork(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func connectNetwork(with: MTRNetworkCommissioningClusterConnectNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRNetworkCommissioningClusterConnectNetworkResponseParams?, (any Error)?) -> Void)](mtrclusternetworkcommissioning/connectnetwork(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributeclusterrevision(with:).md)
- [func readAttributeConnectMaxTimeSeconds(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributeconnectmaxtimeseconds(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributegeneratedcommandlist(with:).md)
- [func readAttributeInterfaceEnabled(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributeinterfaceenabled(with:).md)
- [func readAttributeLastConnectErrorValue(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributelastconnecterrorvalue(with:).md)
- [func readAttributeLastNetworkID(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributelastnetworkid(with:).md)
- [func readAttributeLastNetworkingStatus(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributelastnetworkingstatus(with:).md)
- [func readAttributeMaxNetworks(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributemaxnetworks(with:).md)
- [func readAttributeNetworks(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributenetworks(with:).md)
- [func readAttributeScanMaxTimeSeconds(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributescanmaxtimeseconds(with:).md)
- [func removeNetwork(with: MTRNetworkCommissioningClusterRemoveNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrclusternetworkcommissioning/removenetwork(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func removeNetwork(with: MTRNetworkCommissioningClusterRemoveNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrclusternetworkcommissioning/removenetwork(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func reorderNetwork(with: MTRNetworkCommissioningClusterReorderNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrclusternetworkcommissioning/reordernetwork(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func reorderNetwork(with: MTRNetworkCommissioningClusterReorderNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](mtrclusternetworkcommissioning/reordernetwork(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func scanNetworks(with: MTRNetworkCommissioningClusterScanNetworksParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterScanNetworksResponseParams?, (any Error)?) -> Void)](mtrclusternetworkcommissioning/scannetworks(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func scanNetworks(with: MTRNetworkCommissioningClusterScanNetworksParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRNetworkCommissioningClusterScanNetworksResponseParams?, (any Error)?) -> Void)](mtrclusternetworkcommissioning/scannetworks(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func scanNetworks(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterScanNetworksResponseParams?, (any Error)?) -> Void)](mtrclusternetworkcommissioning/scannetworks(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func writeAttributeInterfaceEnabled(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusternetworkcommissioning/writeattributeinterfaceenabled(withvalue:expectedvalueinterval:).md)
- [func writeAttributeInterfaceEnabled(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusternetworkcommissioning/writeattributeinterfaceenabled(withvalue:expectedvalueinterval:params:).md)
- [func readAttributeSupportedThreadFeatures(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributesupportedthreadfeatures(with:).md)
- [func readAttributeSupportedWiFiBands(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributesupportedwifibands(with:).md)
- [func readAttributeThreadVersion(with: MTRReadParams?) -> [String : Any]?](mtrclusternetworkcommissioning/readattributethreadversion(with:).md)

## Relationships

### Inherits From
- [MTRGenericCluster](mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusternetworkcommissioning)*