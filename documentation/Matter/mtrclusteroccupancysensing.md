# MTRClusterOccupancySensing

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
class MTRClusterOccupancySensing
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusteroccupancysensing/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusteroccupancysensing/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributegeneratedcommandlist(with:).md)
- [func readAttributeOccupancy(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributeoccupancy(with:).md)
- [func readAttributeOccupancySensorType(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributeoccupancysensortype(with:).md)
- [func readAttributeOccupancySensorTypeBitmap(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributeoccupancysensortypebitmap(with:).md)
- [func readAttributePIROccupiedToUnoccupiedDelay(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributepiroccupiedtounoccupieddelay(with:)-8y6de.md)
- [func readAttributePIRUnoccupiedToOccupiedDelay(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributepirunoccupiedtooccupieddelay(with:)-9921w.md)
- [func readAttributePIRUnoccupiedToOccupiedThreshold(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributepirunoccupiedtooccupiedthreshold(with:)-4hcda.md)
- [func readAttributePhysicalContactOccupiedToUnoccupiedDelay(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributephysicalcontactoccupiedtounoccupieddelay(with:).md)
- [func readAttributePhysicalContactUnoccupiedToOccupiedDelay(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributephysicalcontactunoccupiedtooccupieddelay(with:).md)
- [func readAttributePhysicalContactUnoccupiedToOccupiedThreshold(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributephysicalcontactunoccupiedtooccupiedthreshold(with:).md)
- [func readAttributePirOccupiedToUnoccupiedDelay(with: MTRReadParams?) -> [String : Any]](mtrclusteroccupancysensing/readattributepiroccupiedtounoccupieddelay(with:)-34lvb.md)
- [func readAttributePirUnoccupiedToOccupiedDelay(with: MTRReadParams?) -> [String : Any]](mtrclusteroccupancysensing/readattributepirunoccupiedtooccupieddelay(with:)-689um.md)
- [func readAttributePirUnoccupiedToOccupiedThreshold(with: MTRReadParams?) -> [String : Any]](mtrclusteroccupancysensing/readattributepirunoccupiedtooccupiedthreshold(with:)-9lalt.md)
- [func readAttributeUltrasonicOccupiedToUnoccupiedDelay(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributeultrasonicoccupiedtounoccupieddelay(with:).md)
- [func readAttributeUltrasonicUnoccupiedToOccupiedDelay(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributeultrasonicunoccupiedtooccupieddelay(with:).md)
- [func readAttributeUltrasonicUnoccupiedToOccupiedThreshold(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributeultrasonicunoccupiedtooccupiedthreshold(with:).md)
- [func writeAttributePIROccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteroccupancysensing/writeattributepiroccupiedtounoccupieddelay(withvalue:expectedvalueinterval:)-7uivi.md)
- [func writeAttributePIROccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteroccupancysensing/writeattributepiroccupiedtounoccupieddelay(withvalue:expectedvalueinterval:params:)-5qnw2.md)
- [func writeAttributePIRUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupieddelay(withvalue:expectedvalueinterval:)-4e9dc.md)
- [func writeAttributePIRUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupieddelay(withvalue:expectedvalueinterval:params:)-1lbjc.md)
- [func writeAttributePIRUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupiedthreshold(withvalue:expectedvalueinterval:)-1gpdu.md)
- [func writeAttributePIRUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupiedthreshold(withvalue:expectedvalueinterval:params:)-7cch4.md)
- [func writeAttributePhysicalContactOccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteroccupancysensing/writeattributephysicalcontactoccupiedtounoccupieddelay(withvalue:expectedvalueinterval:).md)
- [func writeAttributePhysicalContactOccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteroccupancysensing/writeattributephysicalcontactoccupiedtounoccupieddelay(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributePhysicalContactUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteroccupancysensing/writeattributephysicalcontactunoccupiedtooccupieddelay(withvalue:expectedvalueinterval:).md)
- [func writeAttributePhysicalContactUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteroccupancysensing/writeattributephysicalcontactunoccupiedtooccupieddelay(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributePhysicalContactUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteroccupancysensing/writeattributephysicalcontactunoccupiedtooccupiedthreshold(withvalue:expectedvalueinterval:).md)
- [func writeAttributePhysicalContactUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteroccupancysensing/writeattributephysicalcontactunoccupiedtooccupiedthreshold(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributePirOccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteroccupancysensing/writeattributepiroccupiedtounoccupieddelay(withvalue:expectedvalueinterval:)-464r9.md)
- [func writeAttributePirOccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteroccupancysensing/writeattributepiroccupiedtounoccupieddelay(withvalue:expectedvalueinterval:params:)-7ksgk.md)
- [func writeAttributePirUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupieddelay(withvalue:expectedvalueinterval:)-1zbkq.md)
- [func writeAttributePirUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupieddelay(withvalue:expectedvalueinterval:params:)-d0k3.md)
- [func writeAttributePirUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupiedthreshold(withvalue:expectedvalueinterval:)-6neal.md)
- [func writeAttributePirUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupiedthreshold(withvalue:expectedvalueinterval:params:)-7e46a.md)
- [func writeAttributeUltrasonicOccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteroccupancysensing/writeattributeultrasonicoccupiedtounoccupieddelay(withvalue:expectedvalueinterval:).md)
- [func writeAttributeUltrasonicOccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteroccupancysensing/writeattributeultrasonicoccupiedtounoccupieddelay(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeUltrasonicUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteroccupancysensing/writeattributeultrasonicunoccupiedtooccupieddelay(withvalue:expectedvalueinterval:).md)
- [func writeAttributeUltrasonicUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteroccupancysensing/writeattributeultrasonicunoccupiedtooccupieddelay(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeUltrasonicUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteroccupancysensing/writeattributeultrasonicunoccupiedtooccupiedthreshold(withvalue:expectedvalueinterval:).md)
- [func writeAttributeUltrasonicUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteroccupancysensing/writeattributeultrasonicunoccupiedtooccupiedthreshold(withvalue:expectedvalueinterval:params:).md)
- [func readAttributeHoldTime(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributeholdtime(with:).md)
- [func readAttributeHoldTimeLimits(with: MTRReadParams?) -> [String : Any]?](mtrclusteroccupancysensing/readattributeholdtimelimits(with:).md)
- [func writeAttributeHoldTime(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteroccupancysensing/writeattributeholdtime(withvalue:expectedvalueinterval:).md)
- [func writeAttributeHoldTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteroccupancysensing/writeattributeholdtime(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteroccupancysensing)*