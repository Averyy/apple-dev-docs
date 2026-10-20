# MTRClusterOccupancySensing

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
class MTRClusterOccupancySensing
```

```objc
@interface MTRClusterOccupancySensing : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusteroccupancysensing/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusteroccupancysensing/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeOccupancy(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributeoccupancy%28with%29.md)
- [func readAttributeOccupancySensorType(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributeoccupancysensortype%28with%29.md)
- [func readAttributeOccupancySensorTypeBitmap(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributeoccupancysensortypebitmap%28with%29.md)
- [func readAttributePIROccupiedToUnoccupiedDelay(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributepiroccupiedtounoccupieddelay%28with%29-8y6de.md)
- [func readAttributePIRUnoccupiedToOccupiedDelay(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributepirunoccupiedtooccupieddelay%28with%29-9921w.md)
- [func readAttributePIRUnoccupiedToOccupiedThreshold(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributepirunoccupiedtooccupiedthreshold%28with%29-4hcda.md)
- [func readAttributePhysicalContactOccupiedToUnoccupiedDelay(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributephysicalcontactoccupiedtounoccupieddelay%28with%29.md)
- [func readAttributePhysicalContactUnoccupiedToOccupiedDelay(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributephysicalcontactunoccupiedtooccupieddelay%28with%29.md)
- [func readAttributePhysicalContactUnoccupiedToOccupiedThreshold(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributephysicalcontactunoccupiedtooccupiedthreshold%28with%29.md)
- [func readAttributePirOccupiedToUnoccupiedDelay(with: MTRReadParams?) -> [String : Any]](./mtrclusteroccupancysensing/readattributepiroccupiedtounoccupieddelay%28with%29-34lvb.md)
- [func readAttributePirUnoccupiedToOccupiedDelay(with: MTRReadParams?) -> [String : Any]](./mtrclusteroccupancysensing/readattributepirunoccupiedtooccupieddelay%28with%29-689um.md)
- [func readAttributePirUnoccupiedToOccupiedThreshold(with: MTRReadParams?) -> [String : Any]](./mtrclusteroccupancysensing/readattributepirunoccupiedtooccupiedthreshold%28with%29-9lalt.md)
- [func readAttributeUltrasonicOccupiedToUnoccupiedDelay(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributeultrasonicoccupiedtounoccupieddelay%28with%29.md)
- [func readAttributeUltrasonicUnoccupiedToOccupiedDelay(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributeultrasonicunoccupiedtooccupieddelay%28with%29.md)
- [func readAttributeUltrasonicUnoccupiedToOccupiedThreshold(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributeultrasonicunoccupiedtooccupiedthreshold%28with%29.md)
- [func writeAttributePIROccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteroccupancysensing/writeattributepiroccupiedtounoccupieddelay%28withvalue,expectedvalueinterval%29-7uivi.md)
- [func writeAttributePIROccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteroccupancysensing/writeattributepiroccupiedtounoccupieddelay%28withvalue,expectedvalueinterval,params%29-5qnw2.md)
- [func writeAttributePIRUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupieddelay%28withvalue,expectedvalueinterval%29-4e9dc.md)
- [func writeAttributePIRUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupieddelay%28withvalue,expectedvalueinterval,params%29-1lbjc.md)
- [func writeAttributePIRUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupiedthreshold%28withvalue,expectedvalueinterval%29-1gpdu.md)
- [func writeAttributePIRUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupiedthreshold%28withvalue,expectedvalueinterval,params%29-7cch4.md)
- [func writeAttributePhysicalContactOccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteroccupancysensing/writeattributephysicalcontactoccupiedtounoccupieddelay%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributePhysicalContactOccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteroccupancysensing/writeattributephysicalcontactoccupiedtounoccupieddelay%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributePhysicalContactUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteroccupancysensing/writeattributephysicalcontactunoccupiedtooccupieddelay%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributePhysicalContactUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteroccupancysensing/writeattributephysicalcontactunoccupiedtooccupieddelay%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributePhysicalContactUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteroccupancysensing/writeattributephysicalcontactunoccupiedtooccupiedthreshold%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributePhysicalContactUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteroccupancysensing/writeattributephysicalcontactunoccupiedtooccupiedthreshold%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributePirOccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteroccupancysensing/writeattributepiroccupiedtounoccupieddelay%28withvalue,expectedvalueinterval%29-464r9.md)
- [func writeAttributePirOccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteroccupancysensing/writeattributepiroccupiedtounoccupieddelay%28withvalue,expectedvalueinterval,params%29-7ksgk.md)
- [func writeAttributePirUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupieddelay%28withvalue,expectedvalueinterval%29-1zbkq.md)
- [func writeAttributePirUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupieddelay%28withvalue,expectedvalueinterval,params%29-d0k3.md)
- [func writeAttributePirUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupiedthreshold%28withvalue,expectedvalueinterval%29-6neal.md)
- [func writeAttributePirUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteroccupancysensing/writeattributepirunoccupiedtooccupiedthreshold%28withvalue,expectedvalueinterval,params%29-7e46a.md)
- [func writeAttributeUltrasonicOccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteroccupancysensing/writeattributeultrasonicoccupiedtounoccupieddelay%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeUltrasonicOccupiedToUnoccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteroccupancysensing/writeattributeultrasonicoccupiedtounoccupieddelay%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeUltrasonicUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteroccupancysensing/writeattributeultrasonicunoccupiedtooccupieddelay%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeUltrasonicUnoccupiedToOccupiedDelay(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteroccupancysensing/writeattributeultrasonicunoccupiedtooccupieddelay%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeUltrasonicUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteroccupancysensing/writeattributeultrasonicunoccupiedtooccupiedthreshold%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeUltrasonicUnoccupiedToOccupiedThreshold(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteroccupancysensing/writeattributeultrasonicunoccupiedtooccupiedthreshold%28withvalue,expectedvalueinterval,params%29.md)
- [func readAttributeHoldTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributeholdtime%28with%29.md)
- [func readAttributeHoldTimeLimits(with: MTRReadParams?) -> [String : Any]?](./mtrclusteroccupancysensing/readattributeholdtimelimits%28with%29.md)
- [func writeAttributeHoldTime(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteroccupancysensing/writeattributeholdtime%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeHoldTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteroccupancysensing/writeattributeholdtime%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteroccupancysensing)*