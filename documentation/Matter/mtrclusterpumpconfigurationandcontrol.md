# MTRClusterPumpConfigurationAndControl

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
class MTRClusterPumpConfigurationAndControl
```

```objc
@interface MTRClusterPumpConfigurationAndControl : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterpumpconfigurationandcontrol/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterpumpconfigurationandcontrol/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributeattributelist%28with%29.md)
- [func readAttributeCapacity(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributecapacity%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributeclusterrevision%28with%29.md)
- [func readAttributeControlMode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributecontrolmode%28with%29.md)
- [func readAttributeEffectiveControlMode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributeeffectivecontrolmode%28with%29.md)
- [func readAttributeEffectiveOperationMode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributeeffectiveoperationmode%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeLifetimeEnergyConsumed(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributelifetimeenergyconsumed%28with%29.md)
- [func readAttributeLifetimeRunningHours(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributelifetimerunninghours%28with%29.md)
- [func readAttributeMaxCompPressure(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributemaxcomppressure%28with%29.md)
- [func readAttributeMaxConstFlow(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributemaxconstflow%28with%29.md)
- [func readAttributeMaxConstPressure(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributemaxconstpressure%28with%29.md)
- [func readAttributeMaxConstSpeed(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributemaxconstspeed%28with%29.md)
- [func readAttributeMaxConstTemp(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributemaxconsttemp%28with%29.md)
- [func readAttributeMaxFlow(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributemaxflow%28with%29.md)
- [func readAttributeMaxPressure(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributemaxpressure%28with%29.md)
- [func readAttributeMaxSpeed(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributemaxspeed%28with%29.md)
- [func readAttributeMinCompPressure(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributemincomppressure%28with%29.md)
- [func readAttributeMinConstFlow(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributeminconstflow%28with%29.md)
- [func readAttributeMinConstPressure(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributeminconstpressure%28with%29.md)
- [func readAttributeMinConstSpeed(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributeminconstspeed%28with%29.md)
- [func readAttributeMinConstTemp(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributeminconsttemp%28with%29.md)
- [func readAttributeOperationMode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributeoperationmode%28with%29.md)
- [func readAttributePower(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributepower%28with%29.md)
- [func readAttributePumpStatus(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributepumpstatus%28with%29.md)
- [func readAttributeSpeed(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpumpconfigurationandcontrol/readattributespeed%28with%29.md)
- [func writeAttributeControlMode(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterpumpconfigurationandcontrol/writeattributecontrolmode%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeControlMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterpumpconfigurationandcontrol/writeattributecontrolmode%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeLifetimeEnergyConsumed(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterpumpconfigurationandcontrol/writeattributelifetimeenergyconsumed%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLifetimeEnergyConsumed(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterpumpconfigurationandcontrol/writeattributelifetimeenergyconsumed%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeLifetimeRunningHours(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterpumpconfigurationandcontrol/writeattributelifetimerunninghours%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLifetimeRunningHours(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterpumpconfigurationandcontrol/writeattributelifetimerunninghours%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOperationMode(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterpumpconfigurationandcontrol/writeattributeoperationmode%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOperationMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterpumpconfigurationandcontrol/writeattributeoperationmode%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterpumpconfigurationandcontrol)*