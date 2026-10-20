# MTRClusterNetworkCommissioning

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
class MTRClusterNetworkCommissioning
```

```objc
@interface MTRClusterNetworkCommissioning : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusternetworkcommissioning/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusternetworkcommissioning/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func addOrUpdateThreadNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateThreadNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrclusternetworkcommissioning/addorupdatethreadnetwork%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func addOrUpdateThreadNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateThreadNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrclusternetworkcommissioning/addorupdatethreadnetwork%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func addOrUpdateWiFiNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateWiFiNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrclusternetworkcommissioning/addorupdatewifinetwork%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func addOrUpdateWiFiNetwork(with: MTRNetworkCommissioningClusterAddOrUpdateWiFiNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrclusternetworkcommissioning/addorupdatewifinetwork%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func connectNetwork(with: MTRNetworkCommissioningClusterConnectNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterConnectNetworkResponseParams?, (any Error)?) -> Void)](./mtrclusternetworkcommissioning/connectnetwork%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func connectNetwork(with: MTRNetworkCommissioningClusterConnectNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRNetworkCommissioningClusterConnectNetworkResponseParams?, (any Error)?) -> Void)](./mtrclusternetworkcommissioning/connectnetwork%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributeclusterrevision%28with%29.md)
- [func readAttributeConnectMaxTimeSeconds(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributeconnectmaxtimeseconds%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeInterfaceEnabled(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributeinterfaceenabled%28with%29.md)
- [func readAttributeLastConnectErrorValue(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributelastconnecterrorvalue%28with%29.md)
- [func readAttributeLastNetworkID(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributelastnetworkid%28with%29.md)
- [func readAttributeLastNetworkingStatus(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributelastnetworkingstatus%28with%29.md)
- [func readAttributeMaxNetworks(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributemaxnetworks%28with%29.md)
- [func readAttributeNetworks(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributenetworks%28with%29.md)
- [func readAttributeScanMaxTimeSeconds(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributescanmaxtimeseconds%28with%29.md)
- [func removeNetwork(with: MTRNetworkCommissioningClusterRemoveNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrclusternetworkcommissioning/removenetwork%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func removeNetwork(with: MTRNetworkCommissioningClusterRemoveNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrclusternetworkcommissioning/removenetwork%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func reorderNetwork(with: MTRNetworkCommissioningClusterReorderNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrclusternetworkcommissioning/reordernetwork%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func reorderNetwork(with: MTRNetworkCommissioningClusterReorderNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)](./mtrclusternetworkcommissioning/reordernetwork%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func scanNetworks(with: MTRNetworkCommissioningClusterScanNetworksParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterScanNetworksResponseParams?, (any Error)?) -> Void)](./mtrclusternetworkcommissioning/scannetworks%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func scanNetworks(with: MTRNetworkCommissioningClusterScanNetworksParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRNetworkCommissioningClusterScanNetworksResponseParams?, (any Error)?) -> Void)](./mtrclusternetworkcommissioning/scannetworks%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func scanNetworks(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRNetworkCommissioningClusterScanNetworksResponseParams?, (any Error)?) -> Void)](./mtrclusternetworkcommissioning/scannetworks%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func writeAttributeInterfaceEnabled(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusternetworkcommissioning/writeattributeinterfaceenabled%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeInterfaceEnabled(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusternetworkcommissioning/writeattributeinterfaceenabled%28withvalue,expectedvalueinterval,params%29.md)
- [func readAttributeSupportedThreadFeatures(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributesupportedthreadfeatures%28with%29.md)
- [func readAttributeSupportedWiFiBands(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributesupportedwifibands%28with%29.md)
- [func readAttributeThreadVersion(with: MTRReadParams?) -> [String : Any]?](./mtrclusternetworkcommissioning/readattributethreadversion%28with%29.md)

## Relationships

### Inherits From
- [MTRGenericCluster](./mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusternetworkcommissioning)*