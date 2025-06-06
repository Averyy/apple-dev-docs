# MTRClusterEthernetNetworkDiagnostics

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
class MTRClusterEthernetNetworkDiagnostics
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterethernetnetworkdiagnostics/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterethernetnetworkdiagnostics/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributeattributelist(with:).md)
- [func readAttributeCarrierDetect(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributecarrierdetect(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributeclusterrevision(with:).md)
- [func readAttributeCollisionCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributecollisioncount(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributefeaturemap(with:).md)
- [func readAttributeFullDuplex(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributefullduplex(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributegeneratedcommandlist(with:).md)
- [func readAttributeOverrunCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributeoverruncount(with:).md)
- [func readAttributePHYRate(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributephyrate(with:).md)
- [func readAttributePacketRxCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributepacketrxcount(with:).md)
- [func readAttributePacketTxCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributepackettxcount(with:).md)
- [func readAttributeTimeSinceReset(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributetimesincereset(with:).md)
- [func readAttributeTxErrCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterethernetnetworkdiagnostics/readattributetxerrcount(with:).md)
- [func resetCounts(with: MTREthernetNetworkDiagnosticsClusterResetCountsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterethernetnetworkdiagnostics/resetcounts(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func resetCounts(with: MTREthernetNetworkDiagnosticsClusterResetCountsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusterethernetnetworkdiagnostics/resetcounts(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func resetCounts(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterethernetnetworkdiagnostics/resetcounts(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func resetCounts(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusterethernetnetworkdiagnostics/resetcounts(withexpectedvalues:expectedvalueinterval:completionhandler:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterethernetnetworkdiagnostics)*