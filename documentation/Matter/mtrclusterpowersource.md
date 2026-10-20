# MTRClusterPowerSource

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
class MTRClusterPowerSource
```

```objc
@interface MTRClusterPowerSource : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterpowersource/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterpowersource/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeActiveBatChargeFaults(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributeactivebatchargefaults%28with%29.md)
- [func readAttributeActiveBatFaults(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributeactivebatfaults%28with%29.md)
- [func readAttributeActiveWiredFaults(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributeactivewiredfaults%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributeattributelist%28with%29.md)
- [func readAttributeBatANSIDesignation(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatansidesignation%28with%29.md)
- [func readAttributeBatApprovedChemistry(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatapprovedchemistry%28with%29.md)
- [func readAttributeBatCapacity(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatcapacity%28with%29.md)
- [func readAttributeBatChargeLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatchargelevel%28with%29.md)
- [func readAttributeBatChargeState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatchargestate%28with%29.md)
- [func readAttributeBatChargingCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatchargingcurrent%28with%29.md)
- [func readAttributeBatCommonDesignation(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatcommondesignation%28with%29.md)
- [func readAttributeBatFunctionalWhileCharging(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatfunctionalwhilecharging%28with%29.md)
- [func readAttributeBatIECDesignation(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatiecdesignation%28with%29.md)
- [func readAttributeBatPercentRemaining(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatpercentremaining%28with%29.md)
- [func readAttributeBatPresent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatpresent%28with%29.md)
- [func readAttributeBatQuantity(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatquantity%28with%29.md)
- [func readAttributeBatReplaceability(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatreplaceability%28with%29.md)
- [func readAttributeBatReplacementDescription(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatreplacementdescription%28with%29.md)
- [func readAttributeBatReplacementNeeded(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatreplacementneeded%28with%29.md)
- [func readAttributeBatTimeRemaining(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebattimeremaining%28with%29.md)
- [func readAttributeBatTimeToFullCharge(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebattimetofullcharge%28with%29.md)
- [func readAttributeBatVoltage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributebatvoltage%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributeclusterrevision%28with%29.md)
- [func readAttributeDescription(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributedescription%28with%29.md)
- [func readAttributeEndpointList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributeendpointlist%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeOrder(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributeorder%28with%29.md)
- [func readAttributeStatus(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributestatus%28with%29.md)
- [func readAttributeWiredAssessedCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributewiredassessedcurrent%28with%29.md)
- [func readAttributeWiredAssessedInputFrequency(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributewiredassessedinputfrequency%28with%29.md)
- [func readAttributeWiredAssessedInputVoltage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributewiredassessedinputvoltage%28with%29.md)
- [func readAttributeWiredCurrentType(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributewiredcurrenttype%28with%29.md)
- [func readAttributeWiredMaximumCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributewiredmaximumcurrent%28with%29.md)
- [func readAttributeWiredNominalVoltage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributewirednominalvoltage%28with%29.md)
- [func readAttributeWiredPresent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpowersource/readattributewiredpresent%28with%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterpowersource)*