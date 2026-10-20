# MTRClusterWiFiNetworkDiagnostics

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
class MTRClusterWiFiNetworkDiagnostics
```

```objc
@interface MTRClusterWiFiNetworkDiagnostics : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterwifinetworkdiagnostics/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterwifinetworkdiagnostics/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributeattributelist%28with%29.md)
- [func readAttributeBSSID(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributebssid%28with%29-ckgu.md)
- [func readAttributeBeaconLostCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributebeaconlostcount%28with%29.md)
- [func readAttributeBeaconRxCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributebeaconrxcount%28with%29.md)
- [func readAttributeBssid(with: MTRReadParams?) -> [String : Any]](./mtrclusterwifinetworkdiagnostics/readattributebssid%28with%29-6zw56.md)
- [func readAttributeChannelNumber(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributechannelnumber%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentMaxRate(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributecurrentmaxrate%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeOverrunCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributeoverruncount%28with%29.md)
- [func readAttributePacketMulticastRxCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributepacketmulticastrxcount%28with%29.md)
- [func readAttributePacketMulticastTxCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributepacketmulticasttxcount%28with%29.md)
- [func readAttributePacketUnicastRxCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributepacketunicastrxcount%28with%29.md)
- [func readAttributePacketUnicastTxCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributepacketunicasttxcount%28with%29.md)
- [func readAttributeRSSI(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributerssi%28with%29-8yq7w.md)
- [func readAttributeRssi(with: MTRReadParams?) -> [String : Any]](./mtrclusterwifinetworkdiagnostics/readattributerssi%28with%29-939pp.md)
- [func readAttributeSecurityType(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributesecuritytype%28with%29.md)
- [func readAttributeWiFiVersion(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkdiagnostics/readattributewifiversion%28with%29.md)
- [func resetCounts(with: MTRWiFiNetworkDiagnosticsClusterResetCountsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwifinetworkdiagnostics/resetcounts%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func resetCounts(with: MTRWiFiNetworkDiagnosticsClusterResetCountsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterwifinetworkdiagnostics/resetcounts%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func resetCounts(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwifinetworkdiagnostics/resetcounts%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func resetCounts(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterwifinetworkdiagnostics/resetcounts%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterwifinetworkdiagnostics)*