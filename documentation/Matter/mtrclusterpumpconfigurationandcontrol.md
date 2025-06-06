# MTRClusterPumpConfigurationAndControl

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
class MTRClusterPumpConfigurationAndControl
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterpumpconfigurationandcontrol/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterpumpconfigurationandcontrol/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributeattributelist(with:).md)
- [func readAttributeCapacity(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributecapacity(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributeclusterrevision(with:).md)
- [func readAttributeControlMode(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributecontrolmode(with:).md)
- [func readAttributeEffectiveControlMode(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributeeffectivecontrolmode(with:).md)
- [func readAttributeEffectiveOperationMode(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributeeffectiveoperationmode(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributegeneratedcommandlist(with:).md)
- [func readAttributeLifetimeEnergyConsumed(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributelifetimeenergyconsumed(with:).md)
- [func readAttributeLifetimeRunningHours(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributelifetimerunninghours(with:).md)
- [func readAttributeMaxCompPressure(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributemaxcomppressure(with:).md)
- [func readAttributeMaxConstFlow(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributemaxconstflow(with:).md)
- [func readAttributeMaxConstPressure(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributemaxconstpressure(with:).md)
- [func readAttributeMaxConstSpeed(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributemaxconstspeed(with:).md)
- [func readAttributeMaxConstTemp(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributemaxconsttemp(with:).md)
- [func readAttributeMaxFlow(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributemaxflow(with:).md)
- [func readAttributeMaxPressure(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributemaxpressure(with:).md)
- [func readAttributeMaxSpeed(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributemaxspeed(with:).md)
- [func readAttributeMinCompPressure(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributemincomppressure(with:).md)
- [func readAttributeMinConstFlow(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributeminconstflow(with:).md)
- [func readAttributeMinConstPressure(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributeminconstpressure(with:).md)
- [func readAttributeMinConstSpeed(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributeminconstspeed(with:).md)
- [func readAttributeMinConstTemp(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributeminconsttemp(with:).md)
- [func readAttributeOperationMode(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributeoperationmode(with:).md)
- [func readAttributePower(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributepower(with:).md)
- [func readAttributePumpStatus(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributepumpstatus(with:).md)
- [func readAttributeSpeed(with: MTRReadParams?) -> [String : Any]?](mtrclusterpumpconfigurationandcontrol/readattributespeed(with:).md)
- [func writeAttributeControlMode(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterpumpconfigurationandcontrol/writeattributecontrolmode(withvalue:expectedvalueinterval:).md)
- [func writeAttributeControlMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterpumpconfigurationandcontrol/writeattributecontrolmode(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeLifetimeEnergyConsumed(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterpumpconfigurationandcontrol/writeattributelifetimeenergyconsumed(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLifetimeEnergyConsumed(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterpumpconfigurationandcontrol/writeattributelifetimeenergyconsumed(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeLifetimeRunningHours(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterpumpconfigurationandcontrol/writeattributelifetimerunninghours(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLifetimeRunningHours(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterpumpconfigurationandcontrol/writeattributelifetimerunninghours(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeOperationMode(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterpumpconfigurationandcontrol/writeattributeoperationmode(withvalue:expectedvalueinterval:).md)
- [func writeAttributeOperationMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterpumpconfigurationandcontrol/writeattributeoperationmode(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterpumpconfigurationandcontrol)*