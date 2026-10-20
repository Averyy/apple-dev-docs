# MTRClusterBallastConfiguration

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
class MTRClusterBallastConfiguration
```

```objc
@interface MTRClusterBallastConfiguration : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterballastconfiguration/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterballastconfiguration/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributeattributelist%28with%29.md)
- [func readAttributeBallastFactorAdjustment(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributeballastfactoradjustment%28with%29.md)
- [func readAttributeBallastStatus(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributeballaststatus%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeIntrinsicBalanceFactor(with: MTRReadParams?) -> [String : Any]](./mtrclusterballastconfiguration/readattributeintrinsicbalancefactor%28with%29.md)
- [func readAttributeIntrinsicBallastFactor(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributeintrinsicballastfactor%28with%29.md)
- [func readAttributeLampAlarmMode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributelampalarmmode%28with%29.md)
- [func readAttributeLampBurnHours(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributelampburnhours%28with%29.md)
- [func readAttributeLampBurnHoursTripPoint(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributelampburnhourstrippoint%28with%29.md)
- [func readAttributeLampManufacturer(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributelampmanufacturer%28with%29.md)
- [func readAttributeLampQuantity(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributelampquantity%28with%29.md)
- [func readAttributeLampRatedHours(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributelampratedhours%28with%29.md)
- [func readAttributeLampType(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributelamptype%28with%29.md)
- [func readAttributeMaxLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributemaxlevel%28with%29.md)
- [func readAttributeMinLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributeminlevel%28with%29.md)
- [func readAttributePhysicalMaxLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributephysicalmaxlevel%28with%29.md)
- [func readAttributePhysicalMinLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterballastconfiguration/readattributephysicalminlevel%28with%29.md)
- [func writeAttributeBallastFactorAdjustment(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterballastconfiguration/writeattributeballastfactoradjustment%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeBallastFactorAdjustment(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterballastconfiguration/writeattributeballastfactoradjustment%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeIntrinsicBalanceFactor(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterballastconfiguration/writeattributeintrinsicbalancefactor%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeIntrinsicBalanceFactor(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterballastconfiguration/writeattributeintrinsicbalancefactor%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeIntrinsicBallastFactor(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterballastconfiguration/writeattributeintrinsicballastfactor%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeIntrinsicBallastFactor(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterballastconfiguration/writeattributeintrinsicballastfactor%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeLampAlarmMode(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterballastconfiguration/writeattributelampalarmmode%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLampAlarmMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterballastconfiguration/writeattributelampalarmmode%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeLampBurnHours(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterballastconfiguration/writeattributelampburnhours%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLampBurnHours(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterballastconfiguration/writeattributelampburnhours%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeLampBurnHoursTripPoint(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterballastconfiguration/writeattributelampburnhourstrippoint%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLampBurnHoursTripPoint(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterballastconfiguration/writeattributelampburnhourstrippoint%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeLampManufacturer(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterballastconfiguration/writeattributelampmanufacturer%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLampManufacturer(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterballastconfiguration/writeattributelampmanufacturer%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeLampRatedHours(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterballastconfiguration/writeattributelampratedhours%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLampRatedHours(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterballastconfiguration/writeattributelampratedhours%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeLampType(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterballastconfiguration/writeattributelamptype%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLampType(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterballastconfiguration/writeattributelamptype%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeMaxLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterballastconfiguration/writeattributemaxlevel%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeMaxLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterballastconfiguration/writeattributemaxlevel%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeMinLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterballastconfiguration/writeattributeminlevel%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeMinLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterballastconfiguration/writeattributeminlevel%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterballastconfiguration)*