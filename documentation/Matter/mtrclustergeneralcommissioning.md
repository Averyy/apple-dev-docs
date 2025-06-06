# MTRClusterGeneralCommissioning

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
class MTRClusterGeneralCommissioning
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclustergeneralcommissioning/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustergeneralcommissioning/init(device:endpointid:queue:).md)
### Instance Methods
- [func armFailSafe(with: MTRGeneralCommissioningClusterArmFailSafeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralCommissioningClusterArmFailSafeResponseParams?, (any Error)?) -> Void)](mtrclustergeneralcommissioning/armfailsafe(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func armFailSafe(with: MTRGeneralCommissioningClusterArmFailSafeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGeneralCommissioningClusterArmFailSafeResponseParams?, (any Error)?) -> Void)](mtrclustergeneralcommissioning/armfailsafe(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func commissioningComplete(with: MTRGeneralCommissioningClusterCommissioningCompleteParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](mtrclustergeneralcommissioning/commissioningcomplete(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func commissioningComplete(with: MTRGeneralCommissioningClusterCommissioningCompleteParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](mtrclustergeneralcommissioning/commissioningcomplete(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func commissioningComplete(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](mtrclustergeneralcommissioning/commissioningcomplete(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func commissioningComplete(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGeneralCommissioningClusterCommissioningCompleteResponseParams?, (any Error)?) -> Void)](mtrclustergeneralcommissioning/commissioningcomplete(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneralcommissioning/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneralcommissioning/readattributeattributelist(with:).md)
- [func readAttributeBasicCommissioningInfo(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneralcommissioning/readattributebasiccommissioninginfo(with:).md)
- [func readAttributeBreadcrumb(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneralcommissioning/readattributebreadcrumb(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneralcommissioning/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneralcommissioning/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneralcommissioning/readattributegeneratedcommandlist(with:).md)
- [func readAttributeLocationCapability(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneralcommissioning/readattributelocationcapability(with:).md)
- [func readAttributeRegulatoryConfig(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneralcommissioning/readattributeregulatoryconfig(with:).md)
- [func readAttributeSupportsConcurrentConnection(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneralcommissioning/readattributesupportsconcurrentconnection(with:).md)
- [func setRegulatoryConfigWith(MTRGeneralCommissioningClusterSetRegulatoryConfigParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralCommissioningClusterSetRegulatoryConfigResponseParams?, (any Error)?) -> Void)](mtrclustergeneralcommissioning/setregulatoryconfigwith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func setRegulatoryConfigWith(MTRGeneralCommissioningClusterSetRegulatoryConfigParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGeneralCommissioningClusterSetRegulatoryConfigResponseParams?, (any Error)?) -> Void)](mtrclustergeneralcommissioning/setregulatoryconfigwith(_:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func writeAttributeBreadcrumb(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustergeneralcommissioning/writeattributebreadcrumb(withvalue:expectedvalueinterval:).md)
- [func writeAttributeBreadcrumb(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustergeneralcommissioning/writeattributebreadcrumb(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustergeneralcommissioning)*