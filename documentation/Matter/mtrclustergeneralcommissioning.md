# MTRClusterGeneralCommissioning

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
class MTRClusterGeneralCommissioning
```

```objc
@interface MTRClusterGeneralCommissioning : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclustergeneralcommissioning/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustergeneralcommissioning/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func armFailSafe(with: MTRGeneralCommissioningClusterArmFailSafeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralCommissioningClusterArmFailSafeResponseParams?, (any Error)?) -> Void)](./mtrclustergeneralcommissioning/armfailsafe%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func armFailSafe(with: MTRGeneralCommissioningClusterArmFailSafeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGeneralCommissioningClusterArmFailSafeResponseParams?, (any Error)?) -> Void)](./mtrclustergeneralcommissioning/armfailsafe%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func commissioningComplete(with: MTRGeneralCommissioningClusterCommissioningCompleteParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](./mtrclustergeneralcommissioning/commissioningcomplete%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func commissioningComplete(with: MTRGeneralCommissioningClusterCommissioningCompleteParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](./mtrclustergeneralcommissioning/commissioningcomplete%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func commissioningComplete(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](./mtrclustergeneralcommissioning/commissioningcomplete%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func commissioningComplete(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](./mtrclustergeneralcommissioning/commissioningcomplete%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneralcommissioning/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneralcommissioning/readattributeattributelist%28with%29.md)
- [func readAttributeBasicCommissioningInfo(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneralcommissioning/readattributebasiccommissioninginfo%28with%29.md)
- [func readAttributeBreadcrumb(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneralcommissioning/readattributebreadcrumb%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneralcommissioning/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneralcommissioning/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneralcommissioning/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeLocationCapability(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneralcommissioning/readattributelocationcapability%28with%29.md)
- [func readAttributeRegulatoryConfig(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneralcommissioning/readattributeregulatoryconfig%28with%29.md)
- [func readAttributeSupportsConcurrentConnection(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneralcommissioning/readattributesupportsconcurrentconnection%28with%29.md)
- [func setRegulatoryConfigWith(MTRGeneralCommissioningClusterSetRegulatoryConfigParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralCommissioningClusterSetRegulatoryConfigResponseParams?, (any Error)?) -> Void)](./mtrclustergeneralcommissioning/setregulatoryconfigwith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setRegulatoryConfigWith(MTRGeneralCommissioningClusterSetRegulatoryConfigParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGeneralCommissioningClusterSetRegulatoryConfigResponseParams?, (any Error)?) -> Void)](./mtrclustergeneralcommissioning/setregulatoryconfigwith%28_,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func writeAttributeBreadcrumb(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustergeneralcommissioning/writeattributebreadcrumb%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeBreadcrumb(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustergeneralcommissioning/writeattributebreadcrumb%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustergeneralcommissioning)*