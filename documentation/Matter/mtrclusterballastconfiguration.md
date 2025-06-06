# MTRClusterBallastConfiguration

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
class MTRClusterBallastConfiguration
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterballastconfiguration/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterballastconfiguration/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributeattributelist(with:).md)
- [func readAttributeBallastFactorAdjustment(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributeballastfactoradjustment(with:).md)
- [func readAttributeBallastStatus(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributeballaststatus(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributegeneratedcommandlist(with:).md)
- [func readAttributeIntrinsicBalanceFactor(with: MTRReadParams?) -> [String : Any]](mtrclusterballastconfiguration/readattributeintrinsicbalancefactor(with:).md)
- [func readAttributeIntrinsicBallastFactor(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributeintrinsicballastfactor(with:).md)
- [func readAttributeLampAlarmMode(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributelampalarmmode(with:).md)
- [func readAttributeLampBurnHours(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributelampburnhours(with:).md)
- [func readAttributeLampBurnHoursTripPoint(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributelampburnhourstrippoint(with:).md)
- [func readAttributeLampManufacturer(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributelampmanufacturer(with:).md)
- [func readAttributeLampQuantity(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributelampquantity(with:).md)
- [func readAttributeLampRatedHours(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributelampratedhours(with:).md)
- [func readAttributeLampType(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributelamptype(with:).md)
- [func readAttributeMaxLevel(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributemaxlevel(with:).md)
- [func readAttributeMinLevel(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributeminlevel(with:).md)
- [func readAttributePhysicalMaxLevel(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributephysicalmaxlevel(with:).md)
- [func readAttributePhysicalMinLevel(with: MTRReadParams?) -> [String : Any]?](mtrclusterballastconfiguration/readattributephysicalminlevel(with:).md)
- [func writeAttributeBallastFactorAdjustment(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterballastconfiguration/writeattributeballastfactoradjustment(withvalue:expectedvalueinterval:).md)
- [func writeAttributeBallastFactorAdjustment(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterballastconfiguration/writeattributeballastfactoradjustment(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeIntrinsicBalanceFactor(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterballastconfiguration/writeattributeintrinsicbalancefactor(withvalue:expectedvalueinterval:).md)
- [func writeAttributeIntrinsicBalanceFactor(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterballastconfiguration/writeattributeintrinsicbalancefactor(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeIntrinsicBallastFactor(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterballastconfiguration/writeattributeintrinsicballastfactor(withvalue:expectedvalueinterval:).md)
- [func writeAttributeIntrinsicBallastFactor(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterballastconfiguration/writeattributeintrinsicballastfactor(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeLampAlarmMode(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterballastconfiguration/writeattributelampalarmmode(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLampAlarmMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterballastconfiguration/writeattributelampalarmmode(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeLampBurnHours(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterballastconfiguration/writeattributelampburnhours(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLampBurnHours(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterballastconfiguration/writeattributelampburnhours(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeLampBurnHoursTripPoint(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterballastconfiguration/writeattributelampburnhourstrippoint(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLampBurnHoursTripPoint(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterballastconfiguration/writeattributelampburnhourstrippoint(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeLampManufacturer(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterballastconfiguration/writeattributelampmanufacturer(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLampManufacturer(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterballastconfiguration/writeattributelampmanufacturer(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeLampRatedHours(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterballastconfiguration/writeattributelampratedhours(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLampRatedHours(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterballastconfiguration/writeattributelampratedhours(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeLampType(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterballastconfiguration/writeattributelamptype(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLampType(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterballastconfiguration/writeattributelamptype(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeMaxLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterballastconfiguration/writeattributemaxlevel(withvalue:expectedvalueinterval:).md)
- [func writeAttributeMaxLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterballastconfiguration/writeattributemaxlevel(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeMinLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterballastconfiguration/writeattributeminlevel(withvalue:expectedvalueinterval:).md)
- [func writeAttributeMinLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterballastconfiguration/writeattributeminlevel(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterballastconfiguration)*