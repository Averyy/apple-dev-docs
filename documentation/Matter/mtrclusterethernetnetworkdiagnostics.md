# MTRClusterEthernetNetworkDiagnostics

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
class MTRClusterEthernetNetworkDiagnostics
```

```objc
@interface MTRClusterEthernetNetworkDiagnostics : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterethernetnetworkdiagnostics/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterethernetnetworkdiagnostics/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributeattributelist%28with%29.md)
- [func readAttributeCarrierDetect(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributecarrierdetect%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributeclusterrevision%28with%29.md)
- [func readAttributeCollisionCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributecollisioncount%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributefeaturemap%28with%29.md)
- [func readAttributeFullDuplex(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributefullduplex%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeOverrunCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributeoverruncount%28with%29.md)
- [func readAttributePHYRate(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributephyrate%28with%29.md)
- [func readAttributePacketRxCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributepacketrxcount%28with%29.md)
- [func readAttributePacketTxCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributepackettxcount%28with%29.md)
- [func readAttributeTimeSinceReset(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributetimesincereset%28with%29.md)
- [func readAttributeTxErrCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterethernetnetworkdiagnostics/readattributetxerrcount%28with%29.md)
- [func resetCounts(with: MTREthernetNetworkDiagnosticsClusterResetCountsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterethernetnetworkdiagnostics/resetcounts%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func resetCounts(with: MTREthernetNetworkDiagnosticsClusterResetCountsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterethernetnetworkdiagnostics/resetcounts%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func resetCounts(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterethernetnetworkdiagnostics/resetcounts%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func resetCounts(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterethernetnetworkdiagnostics/resetcounts%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterethernetnetworkdiagnostics)*