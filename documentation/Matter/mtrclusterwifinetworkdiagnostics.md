# MTRClusterWiFiNetworkDiagnostics

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
class MTRClusterWiFiNetworkDiagnostics
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterwifinetworkdiagnostics/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterwifinetworkdiagnostics/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributeattributelist(with:).md)
- [func readAttributeBSSID(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributebssid(with:)-ckgu.md)
- [func readAttributeBeaconLostCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributebeaconlostcount(with:).md)
- [func readAttributeBeaconRxCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributebeaconrxcount(with:).md)
- [func readAttributeBssid(with: MTRReadParams?) -> [String : Any]](mtrclusterwifinetworkdiagnostics/readattributebssid(with:)-6zw56.md)
- [func readAttributeChannelNumber(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributechannelnumber(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentMaxRate(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributecurrentmaxrate(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributegeneratedcommandlist(with:).md)
- [func readAttributeOverrunCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributeoverruncount(with:).md)
- [func readAttributePacketMulticastRxCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributepacketmulticastrxcount(with:).md)
- [func readAttributePacketMulticastTxCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributepacketmulticasttxcount(with:).md)
- [func readAttributePacketUnicastRxCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributepacketunicastrxcount(with:).md)
- [func readAttributePacketUnicastTxCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributepacketunicasttxcount(with:).md)
- [func readAttributeRSSI(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributerssi(with:)-8yq7w.md)
- [func readAttributeRssi(with: MTRReadParams?) -> [String : Any]](mtrclusterwifinetworkdiagnostics/readattributerssi(with:)-939pp.md)
- [func readAttributeSecurityType(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributesecuritytype(with:).md)
- [func readAttributeWiFiVersion(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkdiagnostics/readattributewifiversion(with:).md)
- [func resetCounts(with: MTRWiFiNetworkDiagnosticsClusterResetCountsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwifinetworkdiagnostics/resetcounts(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func resetCounts(with: MTRWiFiNetworkDiagnosticsClusterResetCountsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterwifinetworkdiagnostics/resetcounts(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func resetCounts(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwifinetworkdiagnostics/resetcounts(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func resetCounts(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterwifinetworkdiagnostics/resetcounts(withexpectedvalues:expectedvalueinterval:completionhandler:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterwifinetworkdiagnostics)*