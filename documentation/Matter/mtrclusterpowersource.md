# MTRClusterPowerSource

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
class MTRClusterPowerSource
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterpowersource/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterpowersource/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributeacceptedcommandlist(with:).md)
- [func readAttributeActiveBatChargeFaults(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributeactivebatchargefaults(with:).md)
- [func readAttributeActiveBatFaults(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributeactivebatfaults(with:).md)
- [func readAttributeActiveWiredFaults(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributeactivewiredfaults(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributeattributelist(with:).md)
- [func readAttributeBatANSIDesignation(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatansidesignation(with:).md)
- [func readAttributeBatApprovedChemistry(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatapprovedchemistry(with:).md)
- [func readAttributeBatCapacity(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatcapacity(with:).md)
- [func readAttributeBatChargeLevel(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatchargelevel(with:).md)
- [func readAttributeBatChargeState(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatchargestate(with:).md)
- [func readAttributeBatChargingCurrent(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatchargingcurrent(with:).md)
- [func readAttributeBatCommonDesignation(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatcommondesignation(with:).md)
- [func readAttributeBatFunctionalWhileCharging(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatfunctionalwhilecharging(with:).md)
- [func readAttributeBatIECDesignation(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatiecdesignation(with:).md)
- [func readAttributeBatPercentRemaining(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatpercentremaining(with:).md)
- [func readAttributeBatPresent(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatpresent(with:).md)
- [func readAttributeBatQuantity(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatquantity(with:).md)
- [func readAttributeBatReplaceability(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatreplaceability(with:).md)
- [func readAttributeBatReplacementDescription(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatreplacementdescription(with:).md)
- [func readAttributeBatReplacementNeeded(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatreplacementneeded(with:).md)
- [func readAttributeBatTimeRemaining(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebattimeremaining(with:).md)
- [func readAttributeBatTimeToFullCharge(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebattimetofullcharge(with:).md)
- [func readAttributeBatVoltage(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributebatvoltage(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributeclusterrevision(with:).md)
- [func readAttributeDescription(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributedescription(with:).md)
- [func readAttributeEndpointList(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributeendpointlist(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributegeneratedcommandlist(with:).md)
- [func readAttributeOrder(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributeorder(with:).md)
- [func readAttributeStatus(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributestatus(with:).md)
- [func readAttributeWiredAssessedCurrent(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributewiredassessedcurrent(with:).md)
- [func readAttributeWiredAssessedInputFrequency(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributewiredassessedinputfrequency(with:).md)
- [func readAttributeWiredAssessedInputVoltage(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributewiredassessedinputvoltage(with:).md)
- [func readAttributeWiredCurrentType(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributewiredcurrenttype(with:).md)
- [func readAttributeWiredMaximumCurrent(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributewiredmaximumcurrent(with:).md)
- [func readAttributeWiredNominalVoltage(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributewirednominalvoltage(with:).md)
- [func readAttributeWiredPresent(with: MTRReadParams?) -> [String : Any]?](mtrclusterpowersource/readattributewiredpresent(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterpowersource)*